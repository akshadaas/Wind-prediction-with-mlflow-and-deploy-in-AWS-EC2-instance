from src.wind_prediction import logger
from src.wind_prediction.config.configuration import ConfigurationManager
from src.wind_prediction.entity import ModelTrainerConfig
import pandas as pd
import joblib
import os
from sklearn.linear_model import ElasticNet

class ModelTrainer:
    def __init__(self,config = ConfigurationManager):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_path)
        test_data = pd.read_csv(self.config.test_path)

        train_x = train_data.drop([self.config.target_column],axis=1)
        test_x = test_data.drop([self.config.target_column],axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]


        lr = ElasticNet(alpha = self.config.alpha, l1_ratio = self.config.l1_ratio, random_state = 0 )
        lr.fit(train_x,train_y)

        joblib.dump(lr,os.path.join(self.config.root_dir,self.config.model_name))
