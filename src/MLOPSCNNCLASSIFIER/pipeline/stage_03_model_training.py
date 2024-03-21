from src.MLOPSCNNCLASSIFIER import logger
from src.MLOPSCNNCLASSIFIER.config.configuration import ConfigurationManager
from src.MLOPSCNNCLASSIFIER.components.model_training import Training

STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config= ConfigurationManager()
            training_config= config.get_training_config()
            training=Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()
        except Exception as e:
            raise e