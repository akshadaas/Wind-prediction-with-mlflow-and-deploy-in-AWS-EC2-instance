from src.wind_prediction.config.configuration import ConfigurationManager
from src.wind_prediction.components.model_trainer import ModelTrainer

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_config_model_trainer()
        model_trainer = ModelTrainer(config = model_trainer_config)
        model_trainer.train()
        
