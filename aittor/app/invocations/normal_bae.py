from aittor.app.invocations.baseinvocation import BaseInvocation, invocation
from aittor.app.invocations.fields import ImageField, InputField, WithBoard, WithMetadata
from aittor.app.invocations.primitives import ImageOutput
from aittor.app.services.shared.invocation_context import InvocationContext
from aittor.backend.image_util.normal_bae import NormalMapDetector
from aittor.backend.image_util.normal_bae.nets.NNET import NNET


@invocation(
    "normal_map",
    title="Normal Map",
    tags=["controlnet", "normal"],
    category="controlnet",
    version="1.0.0",
)
class NormalMapInvocation(BaseInvocation, WithMetadata, WithBoard):
    """Generates a normal map."""

    image: ImageField = InputField(description="The image to process")

    def proceed(self, context: InvocationContext) -> ImageOutput:
        image = context.images.get_pil(self.image.image_name, "RGB")
        loaded_model = context.models.load_remote_model(NormalMapDetector.get_model_url(), NormalMapDetector.load_model)

        with loaded_model as model:
            assert isinstance(model, NNET)
            detector = NormalMapDetector(model)
            normal_map = detector.run(image=image)

        image_dto = context.images.save(image=normal_map)
        return ImageOutput.build(image_dto)
