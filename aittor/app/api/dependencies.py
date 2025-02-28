# Copyright (c) 2022 APP Development Team

import asyncio
from logging import Logger

import torch

from aittor.app.services.board_image_records.board_image_records_sqlite import SqliteBoardImageRecordStorage
from aittor.app.services.board_images.board_images_default import BoardImagesService
from aittor.app.services.board_records.board_records_sqlite import SqliteBoardRecordStorage
from aittor.app.services.boards.boards_default import BoardService
from aittor.app.services.bulk_download.bulk_download_default import BulkDownloadService
from aittor.app.services.config.config_default import AIAppConfig
from aittor.app.services.download.download_default import DownloadQueueService
from aittor.app.services.events.events_fastapievents import FastAPIEventService
from aittor.app.services.image_files.image_files_disk import DiskImageFileStorage
from aittor.app.services.image_records.image_records_sqlite import SqliteImageRecordStorage
from aittor.app.services.images.images_default import ImageService
from aittor.app.services.invocation_cache.invocation_cache_memory import MemoryInvocationCache
from aittor.app.services.invocation_services import InvocationServices
from aittor.app.services.invocation_stats.invocation_stats_default import InvocationStatsService
from aittor.app.services.operator import Operator
from aittor.app.services.model_images.model_images_default import ModelImageFileStorageDisk
from aittor.app.services.model_manager.model_manager_default import ModelManagerService
from aittor.app.services.model_records.model_records_sql import ModelRecordServiceSQL
from aittor.app.services.names.names_default import SimpleNameService
from aittor.app.services.object_serializer.object_serializer_disk import ObjectSerializerDisk
from aittor.app.services.object_serializer.object_serializer_forward_cache import ObjectSerializerForwardCache
from aittor.app.services.session_processor.session_processor_default import (
    DefaultSessionProcessor,
    DefaultSessionRunner,
)
from aittor.app.services.session_queue.session_queue_sqlite import SqliteSessionQueue
from aittor.app.services.shared.sqlite.sqlite_util import init_db
from aittor.app.services.style_preset_images.style_preset_images_disk import StylePresetImageFileStorageDisk
from aittor.app.services.style_preset_records.style_preset_records_sqlite import SqliteStylePresetRecordsStorage
from aittor.app.services.urls.urls_default import LocalUrlService
from aittor.app.services.workflow_records.workflow_records_sqlite import SqliteWorkflowRecordsStorage
from aittor.backend.stable_diffusion.diffusion.conditioning_data import ConditioningFieldData
from aittor.backend.util.logging import AppLogger
from aittor.version.release import __version__


# TODO: is there a better way to achieve this?
def check_internet() -> bool:
    """
    Return true if the internet is reachable.
    It does this by pinging huggingface.co.
    """
    import urllib.request

    host = "http://huggingface.co"
    try:
        urllib.request.urlopen(host, timeout=1)
        return True
    except Exception:
        return False


logger = AppLogger.get_logger()


class ApiDependencies:
    """Contains and initializes all dependencies for the API"""

    operator: Operator

    @staticmethod
    def initialize(
        config: AIAppConfig,
        event_handler_id: int,
        loop: asyncio.AbstractEventLoop,
        logger: Logger = logger,
    ) -> None:
        logger.info(f"App version {__version__}")
        logger.info(f"Root directory = {str(config.root_path)}")

        output_folder = config.outputs_path
        if output_folder is None:
            raise ValueError("Output folder is not set")

        image_files = DiskImageFileStorage(f"{output_folder}/images")

        model_images_folder = config.models_path
        style_presets_folder = config.style_presets_path

        db = init_db(config=config, logger=logger, image_files=image_files)

        configuration = config
        logger = logger

        board_image_records = SqliteBoardImageRecordStorage(db=db)
        board_images = BoardImagesService()
        board_records = SqliteBoardRecordStorage(db=db)
        boards = BoardService()
        events = FastAPIEventService(event_handler_id, loop=loop)
        bulk_download = BulkDownloadService()
        image_records = SqliteImageRecordStorage(db=db)
        images = ImageService()
        invocation_cache = MemoryInvocationCache(max_cache_size=config.node_cache_size)
        tensors = ObjectSerializerForwardCache(
            ObjectSerializerDisk[torch.Tensor](output_folder / "tensors", ephemeral=True)
        )
        conditioning = ObjectSerializerForwardCache(
            ObjectSerializerDisk[ConditioningFieldData](output_folder / "conditioning", ephemeral=True)
        )
        download_queue_service = DownloadQueueService(app_config=configuration, event_bus=events)
        model_images_service = ModelImageFileStorageDisk(model_images_folder / "model_images")
        model_manager = ModelManagerService.build_model_manager(
            app_config=configuration,
            model_record_service=ModelRecordServiceSQL(db=db, logger=logger),
            download_queue=download_queue_service,
            events=events,
        )
        names = SimpleNameService()
        performance_statistics = InvocationStatsService()
        session_processor = DefaultSessionProcessor(session_runner=DefaultSessionRunner())
        session_queue = SqliteSessionQueue(db=db)
        urls = LocalUrlService()
        workflow_records = SqliteWorkflowRecordsStorage(db=db)
        style_preset_records = SqliteStylePresetRecordsStorage(db=db)
        style_preset_image_files = StylePresetImageFileStorageDisk(style_presets_folder / "images")

        services = InvocationServices(
            board_image_records=board_image_records,
            board_images=board_images,
            board_records=board_records,
            boards=boards,
            bulk_download=bulk_download,
            configuration=configuration,
            events=events,
            image_files=image_files,
            image_records=image_records,
            images=images,
            invocation_cache=invocation_cache,
            logger=logger,
            model_images=model_images_service,
            model_manager=model_manager,
            download_queue=download_queue_service,
            names=names,
            performance_statistics=performance_statistics,
            session_processor=session_processor,
            session_queue=session_queue,
            urls=urls,
            workflow_records=workflow_records,
            tensors=tensors,
            conditioning=conditioning,
            style_preset_records=style_preset_records,
            style_preset_image_files=style_preset_image_files,
        )

        ApiDependencies.operator = Operator(services)
        db.clean()

    @staticmethod
    def shutdown() -> None:
        if ApiDependencies.operator:
            ApiDependencies.operator.stop()
