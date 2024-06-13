import os
from pathlib import Path
from ChickenClassifier.entity.config_entity import DataIngestionConfig, EvaluationConfig, PrepareBaseModelConfig, PrepareCallbacksConfig, TrainingConfig
from ChickenClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from ChickenClassifier.utils.common import read_yaml, create_directories


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
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir= config.root_dir,
            base_model_path= config.base_model_path,
            updated_base_model_path= config.updated_base_model_path,
            params_image_size= self.params.IMAGE_SIZE,
            params_learning_rate= self.params.LEARNING_RATES,
            params_include_top= self.params.INCLUDE_TOP,
            params_weights= self.params.WEIGHTS,
            params_classes= self.params.CLASSES
        )

        return prepare_base_model_config
    
    def get_prepare_callbacks_config(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        # accessing only directory name without filename
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([
            Path(model_ckpt_dir),
            Path(config.tensorboard_root_log_dir)
            ])

        prepare_callback_config = PrepareCallbacksConfig(
            root_dir= config.root_dir,
            tensorboard_root_log_dir= config.tensorboard_root_log_dir,
            checkpoint_model_filepath= config.checkpoint_model_filepath
        )

        return prepare_callback_config
    
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        params = self.params
        basemodel_config = self.config.prepare_base_model
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "Chicken-fecal-images")

        create_directories([training.root_dir])

        training_config = TrainingConfig(
            root_dir= training.root_dir,
            trained_model_path= training.trained_model_path,
            updated_base_model_path= basemodel_config.updated_base_model_path,
            training_data= Path(training_data),
            params_epoch= params.EPOCHS,
            params_batch_size= params.BATCH_SIZE,
            params_is_augmentation= params.AUGMENTATION,
            params_image_size= params.IMAGE_SIZE
        )

        return training_config
    
    def get_validation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model= Path("artifacts/training/model.h5"),
            training_data= Path("artifacts/data_ingestion/Chicken-fecal-images"),
            all_params= self.params,
            params_image_size= self.params.IMAGE_SIZE,
            params_batch_size= self.params.BATCH_SIZE
        )

        return eval_config