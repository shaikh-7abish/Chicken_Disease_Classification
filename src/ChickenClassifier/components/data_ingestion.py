import os
import urllib.request as request
import zipfile
from pathlib import Path
from src.ChickenClassifier.entity.config_entity import DataIngestionConfig
from src.ChickenClassifier import logger
from src.ChickenClassifier.utils.common import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_files):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_files
            )
            logger.info(f"{filename} downloaded! with following info: \n {headers}")

        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_files))}")

    
    def extract_zip_files(self):
        unzip_path = self.config.unzip_file
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_files, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)