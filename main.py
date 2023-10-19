from KidneyDiseaseClassifier.logging import logger
from KidneyDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline


logger.info("Welcome to logging")

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e  