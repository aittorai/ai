import math
from typing import Tuple

from aittor.app.invocations.baseinvocation import BaseInvocation, BaseInvocationOutput, invocation, invocation_output
from aittor.app.invocations.constants import LATENT_SCALE_FACTOR
from aittor.app.invocations.fields import FieldDescriptions, InputField, OutputField
from aittor.app.invocations.model import UNetField
from aittor.app.services.shared.invocation_context import InvocationContext
from aittor.backend.model_manager.config import BaseModelType


@invocation_output("ideal_size_output")
class IdealSizeOutput(BaseInvocationOutput):
    """Base class for invocations that output an image"""

    width: int = OutputField(description="The ideal width of the image (in pixels)")
    height: int = OutputField(description="The ideal height of the image (in pixels)")


@invocation(
    "ideal_size",
    title="Ideal Size",
    tags=["latents", "math", "ideal_size"],
    version="1.0.3",
)
class IdealSizeInvocation(BaseInvocation):
    """Calculates the ideal size for generation to avoid duplication"""

    width: int = InputField(default=1024, description="Final image width")
    height: int = InputField(default=576, description="Final image height")
    unet: UNetField = InputField(default=None, description=FieldDescriptions.unet)
    multiplier: float = InputField(
        default=1.0,
        description="Amount to multiply the model's dimensions by when calculating the ideal size (may result in "
        "initial generation artifacts if too large)",
    )

    def trim_to_multiple_of(self, *args: int, multiple_of: int = LATENT_SCALE_FACTOR) -> Tuple[int, ...]:
        return tuple((x - x % multiple_of) for x in args)

    def proceed(self, context: InvocationContext) -> IdealSizeOutput:
        unet_config = context.models.get_config(self.unet.unet.key)
        aspect = self.width / self.height
        dimension: float = 512
        if unet_config.base == BaseModelType.StableDiffusion2:
            dimension = 768
        elif unet_config.base == BaseModelType.StableDiffusionXL:
            dimension = 1024
        dimension = dimension * self.multiplier
        min_dimension = math.floor(dimension * 0.5)
        model_area = dimension * dimension  # hardcoded for now since all models are trained on square images

        if aspect > 1.0:
            init_height = max(min_dimension, math.sqrt(model_area / aspect))
            init_width = init_height * aspect
        else:
            init_width = max(min_dimension, math.sqrt(model_area * aspect))
            init_height = init_width / aspect

        scaled_width, scaled_height = self.trim_to_multiple_of(
            math.floor(init_width),
            math.floor(init_height),
        )

        return IdealSizeOutput(width=scaled_width, height=scaled_height)
