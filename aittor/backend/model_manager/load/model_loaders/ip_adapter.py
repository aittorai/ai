# Copyright (c) 2024, APP Development Team
"""Class for IP Adapter model loading in app."""

from pathlib import Path
from typing import Optional

import torch

from aittor.backend.ip_adapter.ip_adapter import build_ip_adapter
from aittor.backend.model_manager import AnyModel, AnyModelConfig, BaseModelType, ModelFormat, ModelType, SubModelType
from aittor.backend.model_manager.load import ModelLoader, ModelLoaderRegistry
from aittor.backend.raw_model import RawModel


@ModelLoaderRegistry.register(base=BaseModelType.Any, type=ModelType.IPAdapter, format=ModelFormat.Aittor)
@ModelLoaderRegistry.register(base=BaseModelType.Any, type=ModelType.IPAdapter, format=ModelFormat.Checkpoint)
class IPAdapterAppLoader(ModelLoader):
    """Class to load IP Adapter diffusers models."""

    def _load_model(
        self,
        config: AnyModelConfig,
        submodel_type: Optional[SubModelType] = None,
    ) -> AnyModel:
        if submodel_type is not None:
            raise ValueError("There are no submodels in an IP-Adapter model.")
        model_path = Path(config.path)
        model: RawModel = build_ip_adapter(
            ip_adapter_ckpt_path=model_path,
            device=torch.device("cpu"),
            dtype=self._torch_dtype,
        )
        return model
