from __future__ import annotations

from contextlib import contextmanager
from typing import TYPE_CHECKING

from diffusers import UNet2DConditionModel

from aittor.backend.lora.lora_model_raw import LoRAModelRaw
from aittor.backend.lora.lora_patcher import LoRAPatcher
from aittor.backend.stable_diffusion.extensions.base import ExtensionBase

if TYPE_CHECKING:
    from aittor.app.invocations.model import ModelIdentifierField
    from aittor.app.services.shared.invocation_context import InvocationContext
    from aittor.backend.util.original_weights_storage import OriginalWeightsStorage


class LoRAExt(ExtensionBase):
    def __init__(
        self,
        node_context: InvocationContext,
        model_id: ModelIdentifierField,
        weight: float,
    ):
        super().__init__()
        self._node_context = node_context
        self._model_id = model_id
        self._weight = weight

    @contextmanager
    def patch_unet(self, unet: UNet2DConditionModel, original_weights: OriginalWeightsStorage):
        lora_model = self._node_context.models.load(self._model_id).model
        assert isinstance(lora_model, LoRAModelRaw)
        LoRAPatcher.apply_lora_patch(
            model=unet,
            prefix="lora_unet_",
            patch=lora_model,
            patch_weight=self._weight,
            original_weights=original_weights,
        )
        del lora_model

        yield
