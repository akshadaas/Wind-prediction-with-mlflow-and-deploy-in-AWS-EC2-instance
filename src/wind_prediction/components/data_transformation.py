from src.wind_prediction import logger
from src.wind_prediction.entity import DataTransformationConfig
import pandas as pd
from sklearn.model_selection import train_test_split
import os


class DataTransformation:
    def __init__(self, config = DataTransformationConfig):
        self.config = config


    def train_test_spliting(self):
        # you can EDA here

        data = pd.read_csv(self.config.data_path)
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,'train.csv'),index=False)
        test.to_csv(os.path.join(self.config.root_dir,'test.csv'),index=False)

        logger.info('Data is splitted into train and test sets.')
        logger.info(f'Train data shape : {train.shape}')
        logger.info(f'Test data shape : {test.shape}')

    


