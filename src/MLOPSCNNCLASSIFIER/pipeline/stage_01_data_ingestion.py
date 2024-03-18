from MLOPSCNNCLASSIFIER.entity.config_entity import DataIngestionConfig
from MLOPSCNNCLASSIFIER.components.data_ingestion import DataIngestion
from MLOPSCNNCLASSIFIER.config.configuration import ConfigurationManager
from MLOPSCNNCLASSIFIER import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config=ConfigurationManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

        except Exception as e:
            raise e 



if __name__ == "__main__":
    try:
        logger.info(f">>>> Starting Stage {STAGE_NAME} <<<<")
        pipeline = DataIngestionPipeline()
        pipeline.main()
        logger.info(f">>>> Completed stage {STAGE_NAME} <<<<\n\n x=======x")
    except Exception as e:
        logger.exception(e)