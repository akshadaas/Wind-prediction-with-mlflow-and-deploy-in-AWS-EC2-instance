from src.wind_prediction.config.configuration import ConfigurationManager
from src.wind_prediction.components.data_validation import DataValidation
from src.wind_prediction import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_config_data_validation()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_columns()
