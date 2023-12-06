from src.wind_prediction.config.configuration import ConfigurationManager
from src.wind_prediction import logger
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from src.wind_prediction.utils.common import save_json
import numpy as np
import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
from pathlib import Path
from urllib.parse import urlparse


class ModelEvaluation:
    def __init__(self, config = ConfigurationManager):
        self.config = config

    def eval_metric(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r_squared = r2_score(actual,pred)

        return rmse, mae, r_squared

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column],axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_url)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)

            rmse, mae, r_squared  = self.eval_metric(test_y,predicted_qualities)

            scores = {
                    'rmse' : rmse,
                    'mae' : mae,
                    'r_squared' : r_squared
                }

            save_json(path=Path(self.config.metric_file_name),data=scores)
            mlflow.log_params(self.config.all_params)

            mlflow.log_metric('rmse',rmse)
            mlflow.log_metric('mae', mae)
            mlflow.log_metric('r_squared',r_squared)

            if tracking_url_type_store != 'file':
               mlflow.sklearn.log_model(model, "model", registered_model_name = 'ElasticNetModel')

            else:
                mlflow.sklearn.log_model(model, 'model')
