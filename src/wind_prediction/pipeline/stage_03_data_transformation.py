from src.wind_prediction import logger
from src.wind_prediction.config.configuration import ConfigurationManager
from src.wind_prediction.components.data_transformation import DataTransformation

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_config_data_transformation()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_spliting()
