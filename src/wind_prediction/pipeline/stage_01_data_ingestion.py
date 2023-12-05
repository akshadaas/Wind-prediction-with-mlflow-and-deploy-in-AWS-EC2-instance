from src.wind_prediction.config.configuration import ConfigurationManager
from src.wind_prediction.components.data_ingestion import DataIngestion

from src.wind_prediction import logger

stage_name = 'Data Ingestion'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_config_data_ingestion()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f"******{stage_name} started******")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"******{stage_name} completed******")
    
    except Exception as e:
        logging.info(e)
