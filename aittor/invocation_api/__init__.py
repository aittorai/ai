"""
This file re-exports all the public API for invocations. This is the only file that should be imported by custom nodes.

TODO(psyche): Do we want to dogfood this?
"""

from aittor.app.invocations.baseinvocation import (
    BaseInvocation,
    BaseInvocationOutput,
    Classification,
    invocation,
    invocation_output,
)
from aittor.app.invocations.fields import (
    BoardField,
    BoundingBoxField,
    ColorField,
    ConditioningField,
    DenoiseMaskField,
    FieldDescriptions,
    FieldKind,
    ImageField,
    Input,
    InputField,
    LatentsField,
    MetadataField,
    OutputField,
    UIComponent,
    UIType,
    WithBoard,
    WithMetadata,
    WithWorkflow,
)
from aittor.app.invocations.metadata import MetadataItemField, MetadataItemOutput, MetadataOutput
from aittor.app.invocations.model import (
    CLIPField,
    CLIPOutput,
    LoRALoaderOutput,
    ModelIdentifierField,
    ModelLoaderOutput,
    SDXLLoRALoaderOutput,
    UNetField,
    UNetOutput,
    VAEField,
    VAEOutput,
)
from aittor.app.invocations.primitives import (
    BooleanCollectionOutput,
    BooleanOutput,
    BoundingBoxOutput,
    ColorCollectionOutput,
    ColorOutput,
    ConditioningCollectionOutput,
    ConditioningOutput,
    DenoiseMaskOutput,
    FloatCollectionOutput,
    FloatOutput,
    ImageCollectionOutput,
    ImageOutput,
    IntegerCollectionOutput,
    IntegerOutput,
    LatentsCollectionOutput,
    LatentsOutput,
    StringCollectionOutput,
    StringOutput,
)
from aittor.app.invocations.scheduler import SchedulerOutput
from aittor.app.services.boards.boards_common import BoardDTO
from aittor.app.services.config.config_default import AIAppConfig
from aittor.app.services.image_records.image_records_common import ImageCategory
from aittor.app.services.shared.invocation_context import InvocationContext
from aittor.app.services.workflow_records.workflow_records_common import WorkflowWithoutID
from aittor.app.util.misc import SEED_MAX, get_random_seed
from aittor.backend.model_manager.config import BaseModelType, ModelType, SubModelType
from aittor.backend.model_manager.load.load_base import LoadedModel
from aittor.backend.stable_diffusion.diffusers_pipeline import PipelineIntermediateState
from aittor.backend.stable_diffusion.diffusion.conditioning_data import (
    BasicConditioningInfo,
    ConditioningFieldData,
    SDXLConditioningInfo,
)
from aittor.backend.stable_diffusion.schedulers.schedulers import SCHEDULER_NAME_VALUES
from aittor.backend.util.devices import CPU_DEVICE, CUDA_DEVICE, MPS_DEVICE, choose_precision, choose_torch_device
from aittor.version import __version__

__all__ = [
    # aittor.app.invocations.baseinvocation
    "BaseInvocation",
    "BaseInvocationOutput",
    "Classification",
    "invocation",
    "invocation_output",
    # aittor.app.services.shared.invocation_context
    "InvocationContext",
    # aittor.app.invocations.fields
    "BoardField",
    "BoundingBoxField",
    "ColorField",
    "ConditioningField",
    "DenoiseMaskField",
    "FieldDescriptions",
    "FieldKind",
    "ImageField",
    "Input",
    "InputField",
    "LatentsField",
    "MetadataField",
    "OutputField",
    "UIComponent",
    "UIType",
    "WithBoard",
    "WithMetadata",
    "WithWorkflow",
    # aittor.app.invocations.scheduler
    "SchedulerOutput",
    # aittor.app.invocations.metadata
    "MetadataItemField",
    "MetadataItemOutput",
    "MetadataOutput",
    # aittor.app.invocations.model
    "ModelIdentifierField",
    "UNetField",
    "CLIPField",
    "VAEField",
    "UNetOutput",
    "VAEOutput",
    "CLIPOutput",
    "ModelLoaderOutput",
    "LoRALoaderOutput",
    "SDXLLoRALoaderOutput",
    # aittor.app.invocations.primitives
    "BooleanCollectionOutput",
    "BooleanOutput",
    "BoundingBoxOutput",
    "ColorCollectionOutput",
    "ColorOutput",
    "ConditioningCollectionOutput",
    "ConditioningOutput",
    "DenoiseMaskOutput",
    "FloatCollectionOutput",
    "FloatOutput",
    "ImageCollectionOutput",
    "ImageOutput",
    "IntegerCollectionOutput",
    "IntegerOutput",
    "LatentsCollectionOutput",
    "LatentsOutput",
    "StringCollectionOutput",
    "StringOutput",
    # aittor.app.services.image_records.image_records_common
    "ImageCategory",
    # aittor.app.services.boards.boards_common
    "BoardDTO",
    # aittor.backend.stable_diffusion.diffusion.conditioning_data
    "BasicConditioningInfo",
    "ConditioningFieldData",
    "SDXLConditioningInfo",
    # aittor.backend.stable_diffusion.diffusers_pipeline
    "PipelineIntermediateState",
    # aittor.app.services.workflow_records.workflow_records_common
    "WorkflowWithoutID",
    # aittor.app.services.config.config_default
    "AIAppConfig",
    # aittor.backend.model_management.model_manager
    "LoadedModel",
    # aittor.backend.model_management.models.base
    "BaseModelType",
    "ModelType",
    "SubModelType",
    # aittor.backend.stable_diffusion.schedulers.schedulers
    "SCHEDULER_NAME_VALUES",
    # aittor.version
    "__version__",
    # aittor.backend.util.devices
    "choose_precision",
    "choose_torch_device",
    "CPU_DEVICE",
    "CUDA_DEVICE",
    "MPS_DEVICE",
    # aittor.app.util.misc
    "SEED_MAX",
    "get_random_seed",
]
