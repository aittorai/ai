from typing import Union

from aittor.backend.lora.layers.concatenated_lora_layer import ConcatenatedLoRALayer
from aittor.backend.lora.layers.full_layer import FullLayer
from aittor.backend.lora.layers.ia3_layer import IA3Layer
from aittor.backend.lora.layers.loha_layer import LoHALayer
from aittor.backend.lora.layers.lokr_layer import LoKRLayer
from aittor.backend.lora.layers.lora_layer import LoRALayer
from aittor.backend.lora.layers.norm_layer import NormLayer

AnyLoRALayer = Union[LoRALayer, LoHALayer, LoKRLayer, FullLayer, IA3Layer, NormLayer, ConcatenatedLoRALayer]
