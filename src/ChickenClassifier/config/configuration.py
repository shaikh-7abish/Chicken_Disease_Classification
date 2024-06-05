from src.ChickenClassifier.entity.config_entity import DataIngestionConfig
from src.ChickenClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.ChickenClassifier.utils.common import read_yaml, create_directories


# creating a class for configuration manager
class ConfigurationManager:
    def __init__(
            self,
            config_filepath= CONFIG_FILE_PATH, # reading constant variables
            params_filepath= PARAMS_FILE_PATH):

        # reading configuration yaml file and params yaml file
        self.config = read_yaml(config_filepath)  
        self.params = read_yaml(params_filepath)

        # creating artifact directory
        create_directories([self.config.artifacts_root])
    
    # creating a function for configuring data ingestion variables
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # from config.yaml accessing data_ingestion data
        config = self.config.data_ingestion

        # creating artifacts/root directory
        create_directories([config.root_dir])

        # assigning values to a variable
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_files = config.local_data_files,
            unzip_file = config.unzip_dir
        )

        return data_ingestion_config