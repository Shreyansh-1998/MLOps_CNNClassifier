"""
This is end point of the project
"""
from src.MLOPSCNNCLASSIFIER import logger
from src.MLOPSCNNCLASSIFIER.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.MLOPSCNNCLASSIFIER.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from src.MLOPSCNNCLASSIFIER.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.MLOPSCNNCLASSIFIER.pipeline.stage_04_model_evaluation import EvaluationPipeline




STAGE_NAME = "Data Ingestion "

try:
    logger.info(f">>>> Starting Stage {STAGE_NAME} <<<<")
    pipeline = DataIngestionPipeline()
    pipeline.main()
    logger.info(f">>>> Completed stage {STAGE_NAME} <<<<\n\n x=======x")
except Exception as e:
    logger.exception(e)

STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f">>>> Starting Stage {STAGE_NAME} <<<<")
    pipeline = PrepareBaseModelPipeline()
    pipeline.main()
    logger.info(f">>>> Completed stage {STAGE_NAME} <<<<\n\n x=======x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training "

try:
    logger.info(f">>>> Starting Stage {STAGE_NAME} <<<<")
    pipeline = ModelTrainingPipeline()
    pipeline.main()
    logger.info(f">>>> Completed stage {STAGE_NAME} <<<<\n\n x=======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation"

try:
    logger.info(f">>>> Starting Stage {STAGE_NAME} <<<<")
    pipeline = EvaluationPipeline()
    pipeline.main()
    logger.info(f">>>> Completed stage {STAGE_NAME} <<<<\n\n x=======x")
except Exception as e:
    logger.exception(e)
    raise e
