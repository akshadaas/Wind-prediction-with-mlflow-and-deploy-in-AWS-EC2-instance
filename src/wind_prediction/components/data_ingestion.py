import os
from src.wind_prediction.utils.common import get_size
import urllib.request as request
import zipfile
from src.wind_prediction import logger
from src.wind_prediction.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_data(self):
        if not os.path.exists(self.config.local_file_path):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_file_path
            )

            logger.info(f'{filename} download! with following info {headers}')


        else:
            logger.info(f'file is already exists of size {get_size(Path(self.config.local_file_path))}')


    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_file_path) as f:
            f.extractall(unzip_path)

