from aittor.app.invocations.baseinvocation import BaseInvocation, invocation
from aittor.app.invocations.fields import ImageField, InputField, WithBoard, WithMetadata
from aittor.app.invocations.primitives import ImageOutput
from aittor.app.services.shared.invocation_context import InvocationContext
from aittor.backend.image_util.content_shuffle import content_shuffle


@invocation(
    "content_shuffle",
    title="Content Shuffle",
    tags=["controlnet", "normal"],
    category="controlnet",
    version="1.0.0",
)
class ContentShuffleInvocation(BaseInvocation, WithMetadata, WithBoard):
    """Shuffles the image, similar to a 'liquify' filter."""

    image: ImageField = InputField(description="The image to process")
    scale_factor: int = InputField(default=256, ge=0, description="The scale factor used for the shuffle")

    def proceed(self, context: InvocationContext) -> ImageOutput:
        image = context.images.get_pil(self.image.image_name, "RGB")
        output_image = content_shuffle(input_image=image, scale_factor=self.scale_factor)
        image_dto = context.images.save(image=output_image)
        return ImageOutput.build(image_dto)
