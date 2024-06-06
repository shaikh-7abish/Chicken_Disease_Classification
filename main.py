from ChickenClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from ChickenClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from ChickenClassifier import logger

STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>>>-- {STAGE_NAME} started. --<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>-- {STAGE_NAME} successfully completed --<<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e
    
STAGE_NAME = 'Prepare Base Model Stage'
try:
    logger.info(f">>>>>-- {STAGE_NAME} started. --<<<<<")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>>-- {STAGE_NAME} successfully completed --<<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e