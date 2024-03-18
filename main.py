"""
This is end point of the project
"""
from src.MLOPSCNNCLASSIFIER import logger
from src.MLOPSCNNCLASSIFIER.pipeline.stage_01_data_ingestion import DataIngestionPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>> Starting Stage {STAGE_NAME} <<<<")
    pipeline = DataIngestionPipeline()
    pipeline.main()
    logger.info(f">>>> Completed stage {STAGE_NAME} <<<<\n\n x=======x")
except Exception as e:
    logger.exception(e)
