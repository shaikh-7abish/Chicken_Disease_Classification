from src.ChickenClassifier import logger
from src.ChickenClassifier.pipeline.stage_01_data_ingestion import STAGE_NAME, DataIngestionPipeline

if __name__ == '__main__':
    try:
        logger.info(f">>>>>-- {STAGE_NAME} started. --<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>-- {STAGE_NAME} successfully completed --<<<<<\n\nx====================x")
    except Exception as e:
        logger.exception(e)
        raise e