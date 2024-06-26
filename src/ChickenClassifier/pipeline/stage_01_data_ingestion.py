from ChickenClassifier.config.configuration import ConfigurationManager
from ChickenClassifier.components.data_ingestion import DataIngestion
from ChickenClassifier import logger

STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config= data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_files()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>-- {STAGE_NAME} started. --<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>-- {STAGE_NAME} successfully completed --<<<<<\n\nx====================x")
    except Exception as e:
        logger.exception(e)
        raise e