from aittor.app.invocations.baseinvocation import BaseInvocation, invocation
from aittor.app.invocations.fields import FieldDescriptions, ImageField, InputField, WithBoard, WithMetadata
from aittor.app.invocations.primitives import ImageOutput
from aittor.app.services.shared.invocation_context import InvocationContext
from aittor.backend.image_util.pidi import PIDINetDetector
from aittor.backend.image_util.pidi.model import PiDiNet


@invocation(
    "pidi_edge_detection",
    title="PiDiNet Edge Detection",
    tags=["controlnet", "edge"],
    category="controlnet",
    version="1.0.0",
)
class PiDiNetEdgeDetectionInvocation(BaseInvocation, WithMetadata, WithBoard):
    """Generates an edge map using PiDiNet."""

    image: ImageField = InputField(description="The image to process")
    quantize_edges: bool = InputField(default=False, description=FieldDescriptions.safe_mode)
    scribble: bool = InputField(default=False, description=FieldDescriptions.scribble_mode)

    def proceed(self, context: InvocationContext) -> ImageOutput:
        image = context.images.get_pil(self.image.image_name, "RGB")
        loaded_model = context.models.load_remote_model(PIDINetDetector.get_model_url(), PIDINetDetector.load_model)

        with loaded_model as model:
            assert isinstance(model, PiDiNet)
            detector = PIDINetDetector(model)
            edge_map = detector.run(image=image, quantize_edges=self.quantize_edges, scribble=self.scribble)

        image_dto = context.images.save(image=edge_map)
        return ImageOutput.build(image_dto)
