from MLOPSCNNCLASSIFIER.config.configuration import ConfigurationManager
from MLOPSCNNCLASSIFIER.components.model_evaluation_mlflow import Evaluation
from MLOPSCNNCLASSIFIER import logger

STAGE_NAME = "Model Evaluation"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager=ConfigurationManager()
        eval_config=config_manager.get_evaluation_config()
        evaluation=Evaluation(eval_config)
        evaluation.evaluation()
        #evaluation.log_into_mlflow()  


if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e