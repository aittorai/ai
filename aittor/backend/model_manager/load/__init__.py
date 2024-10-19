# Copyright (c) 2024 APP Development Team
"""
Init file for the model loader.
"""

from importlib import import_module
from pathlib import Path

from aittor.backend.model_manager.load.load_base import LoadedModel, LoadedModelWithoutConfig, ModelLoaderBase
from aittor.backend.model_manager.load.load_default import ModelLoader
from aittor.backend.model_manager.load.model_cache.model_cache_default import ModelCache
from aittor.backend.model_manager.load.model_loader_registry import ModelLoaderRegistry, ModelLoaderRegistryBase

# This registers the subclasses that implement loaders of specific model types
loaders = [x.stem for x in Path(Path(__file__).parent, "model_loaders").glob("*.py") if x.stem != "__init__"]
for module in loaders:
    import_module(f"{__package__}.model_loaders.{module}")

__all__ = [
    "LoadedModel",
    "LoadedModelWithoutConfig",
    "ModelCache",
    "ModelLoaderBase",
    "ModelLoader",
    "ModelLoaderRegistryBase",
    "ModelLoaderRegistry",
]
