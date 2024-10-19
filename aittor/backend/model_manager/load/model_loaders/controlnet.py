# Copyright (c) 2024, APP Development Team
"""Class for ControlNet model loading in app."""

from typing import Optional

from diffusers import ControlNetModel

from aittor.backend.model_manager import (
    AnyModel,
    AnyModelConfig,
)
from aittor.backend.model_manager.config import (
    BaseModelType,
    ControlNetCheckpointConfig,
    ModelFormat,
    ModelType,
    SubModelType,
)
from aittor.backend.model_manager.load.model_loader_registry import ModelLoaderRegistry
from aittor.backend.model_manager.load.model_loaders.generic_diffusers import GenericDiffusersLoader


@ModelLoaderRegistry.register(
    base=BaseModelType.StableDiffusion1, type=ModelType.ControlNet, format=ModelFormat.Diffusers
)
@ModelLoaderRegistry.register(
    base=BaseModelType.StableDiffusion1, type=ModelType.ControlNet, format=ModelFormat.Checkpoint
)
@ModelLoaderRegistry.register(
    base=BaseModelType.StableDiffusion2, type=ModelType.ControlNet, format=ModelFormat.Diffusers
)
@ModelLoaderRegistry.register(
    base=BaseModelType.StableDiffusion2, type=ModelType.ControlNet, format=ModelFormat.Checkpoint
)
@ModelLoaderRegistry.register(
    base=BaseModelType.StableDiffusionXL, type=ModelType.ControlNet, format=ModelFormat.Diffusers
)
@ModelLoaderRegistry.register(
    base=BaseModelType.StableDiffusionXL, type=ModelType.ControlNet, format=ModelFormat.Checkpoint
)
class ControlNetLoader(GenericDiffusersLoader):
    """Class to load ControlNet models."""

    def _load_model(
        self,
        config: AnyModelConfig,
        submodel_type: Optional[SubModelType] = None,
    ) -> AnyModel:
        if isinstance(config, ControlNetCheckpointConfig):
            return ControlNetModel.from_single_file(
                config.path,
                torch_dtype=self._torch_dtype,
            )
        else:
            return super()._load_model(config, submodel_type)
