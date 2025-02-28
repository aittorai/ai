import einops
import torch

from aittor.app.invocations.baseinvocation import BaseInvocation, invocation
from aittor.app.invocations.fields import (
    FieldDescriptions,
    ImageField,
    Input,
    InputField,
)
from aittor.app.invocations.model import VAEField
from aittor.app.invocations.primitives import LatentsOutput
from aittor.app.services.shared.invocation_context import InvocationContext
from aittor.backend.flux.modules.autoencoder import AutoEncoder
from aittor.backend.model_manager import LoadedModel
from aittor.backend.stable_diffusion.diffusers_pipeline import image_resized_to_grid_as_tensor
from aittor.backend.util.devices import TorchDevice


@invocation(
    "flux_vae_encode",
    title="FLUX Image to Latents",
    tags=["latents", "image", "vae", "i2l", "flux"],
    category="latents",
    version="1.0.0",
)
class FluxVaeEncodeInvocation(BaseInvocation):
    """Encodes an image into latents."""

    image: ImageField = InputField(
        description="The image to encode.",
    )
    vae: VAEField = InputField(
        description=FieldDescriptions.vae,
        input=Input.Connection,
    )

    @staticmethod
    def vae_encode(vae_info: LoadedModel, image_tensor: torch.Tensor) -> torch.Tensor:
        # TODO(ryand): Expose seed parameter at the invocation level.
        # TODO(ryand): Write a util function for generating random tensors that is consistent across devices / dtypes.
        # There's a starting point in get_noise(...), but it needs to be extracted and generalized. This function
        # should be used for VAE encode sampling.
        generator = torch.Generator(device=TorchDevice.choose_torch_device()).manual_seed(0)
        with vae_info as vae:
            assert isinstance(vae, AutoEncoder)
            image_tensor = image_tensor.to(
                device=TorchDevice.choose_torch_device(), dtype=TorchDevice.choose_torch_dtype()
            )
            latents = vae.encode(image_tensor, sample=True, generator=generator)
            return latents

    @torch.no_grad()
    def proceed(self, context: InvocationContext) -> LatentsOutput:
        image = context.images.get_pil(self.image.image_name)

        vae_info = context.models.load(self.vae.vae)

        image_tensor = image_resized_to_grid_as_tensor(image.convert("RGB"))
        if image_tensor.dim() == 3:
            image_tensor = einops.rearrange(image_tensor, "c h w -> 1 c h w")

        latents = self.vae_encode(vae_info=vae_info, image_tensor=image_tensor)

        latents = latents.to("cpu")
        name = context.tensors.save(tensor=latents)
        return LatentsOutput.build(latents_name=name, latents=latents, seed=None)
