# Copyright (c) 2023 APP Development Team
"""Implementation of ModelManagerServiceBase."""

from typing import Optional

import torch
from typing_extensions import Self

from aittor.app.services.config.config_default import AIAppConfig
from aittor.app.services.download.download_base import DownloadQueueServiceBase
from aittor.app.services.events.events_base import EventServiceBase
from aittor.app.services.operator import Operator
from aittor.app.services.model_install.model_install_base import ModelInstallServiceBase
from aittor.app.services.model_install.model_install_default import ModelInstallService
from aittor.app.services.model_load.model_load_base import ModelLoadServiceBase
from aittor.app.services.model_load.model_load_default import ModelLoadService
from aittor.app.services.model_manager.model_manager_base import ModelManagerServiceBase
from aittor.app.services.model_records.model_records_base import ModelRecordServiceBase
from aittor.backend.model_manager.load import ModelCache, ModelLoaderRegistry
from aittor.backend.util.devices import TorchDevice
from aittor.backend.util.logging import AppLogger


class ModelManagerService(ModelManagerServiceBase):
    """
    The ModelManagerService handles various aspects of model installation, maintenance and loading.

    It bundles three distinct services:
    model_manager.store   -- Routines to manage the database of model configuration records.
    model_manager.install -- Routines to install, move and delete models.
    model_manager.load    -- Routines to load models into memory.
    """

    def __init__(
        self,
        store: ModelRecordServiceBase,
        install: ModelInstallServiceBase,
        load: ModelLoadServiceBase,
    ):
        self._store = store
        self._install = install
        self._load = load

    @property
    def store(self) -> ModelRecordServiceBase:
        return self._store

    @property
    def install(self) -> ModelInstallServiceBase:
        return self._install

    @property
    def load(self) -> ModelLoadServiceBase:
        return self._load

    def start(self, operator: Operator) -> None:
        for service in [self._store, self._install, self._load]:
            if hasattr(service, "start"):
                service.start(operator)

    def stop(self, operator: Operator) -> None:
        for service in [self._store, self._install, self._load]:
            if hasattr(service, "stop"):
                service.stop(operator)

    @classmethod
    def build_model_manager(
        cls,
        app_config: AIAppConfig,
        model_record_service: ModelRecordServiceBase,
        download_queue: DownloadQueueServiceBase,
        events: EventServiceBase,
        execution_device: Optional[torch.device] = None,
    ) -> Self:
        """
        Construct the model manager service instance.

        For simplicity, use this class method rather than the __init__ constructor.
        """
        logger = AppLogger.get_logger(cls.__name__)
        logger.setLevel(app_config.log_level.upper())

        ram_cache = ModelCache(
            max_cache_size=app_config.ram,
            max_vram_cache_size=app_config.vram,
            lazy_offloading=app_config.lazy_offload,
            logger=logger,
            execution_device=execution_device or TorchDevice.choose_torch_device(),
        )
        loader = ModelLoadService(
            app_config=app_config,
            ram_cache=ram_cache,
            registry=ModelLoaderRegistry,
        )
        installer = ModelInstallService(
            app_config=app_config,
            record_store=model_record_service,
            download_queue=download_queue,
            event_bus=events,
        )
        return cls(store=model_record_service, install=installer, load=loader)
