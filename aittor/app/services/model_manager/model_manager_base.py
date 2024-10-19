# Copyright (c) 2023 APP Development Team

from abc import ABC, abstractmethod

import torch
from typing_extensions import Self

from aittor.app.services.config.config_default import AIAppConfig
from aittor.app.services.download.download_base import DownloadQueueServiceBase
from aittor.app.services.events.events_base import EventServiceBase
from aittor.app.services.operator import Operator
from aittor.app.services.model_install.model_install_base import ModelInstallServiceBase
from aittor.app.services.model_load.model_load_base import ModelLoadServiceBase
from aittor.app.services.model_records.model_records_base import ModelRecordServiceBase


class ModelManagerServiceBase(ABC):
    """Abstract base class for the model manager service."""

    # attributes:
    # store: ModelRecordServiceBase = Field(description="An instance of the model record configuration service.")
    # install: ModelInstallServiceBase = Field(description="An instance of the model install service.")
    # load: ModelLoadServiceBase = Field(description="An instance of the model load service.")

    @classmethod
    @abstractmethod
    def build_model_manager(
        cls,
        app_config: AIAppConfig,
        model_record_service: ModelRecordServiceBase,
        download_queue: DownloadQueueServiceBase,
        events: EventServiceBase,
        execution_device: torch.device,
    ) -> Self:
        """
        Construct the model manager service instance.

        Use it rather than the __init__ constructor. This class
        method simplifies the construction considerably.
        """
        pass

    @property
    @abstractmethod
    def store(self) -> ModelRecordServiceBase:
        """Return the ModelRecordServiceBase used to store and retrieve configuration records."""
        pass

    @property
    @abstractmethod
    def load(self) -> ModelLoadServiceBase:
        """Return the ModelLoadServiceBase used to load models from their configuration records."""
        pass

    @property
    @abstractmethod
    def install(self) -> ModelInstallServiceBase:
        """Return the ModelInstallServiceBase used to download and manipulate model files."""
        pass

    @abstractmethod
    def start(self, operator: Operator) -> None:
        pass

    @abstractmethod
    def stop(self, operator: Operator) -> None:
        pass
