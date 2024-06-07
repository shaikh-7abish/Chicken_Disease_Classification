from src.ChickenClassifier import logger
from src.ChickenClassifier.components import prepare_callback
from src.ChickenClassifier.components.training import Training
from src.ChickenClassifier.config.configuration import ConfigurationManager


STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = prepare_callback.PrepareCallback(config= prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config= training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list = callback_list
        )

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
