import os , sys
from src.exception import CustomException
from src.logger import logging
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from src.constants import *
from src.configs.configuration import *
from dataclasses import dataclass
from src.components.Data_transformation import *

class DataIngestionConfig:
    def __init__(self):
        self.raw_data_path = RAW_DATASET_PATH
        self.train_data_path = TRAIN_DATASET_PATH
        self.test_data_Path = TEST_DATASET_PATH

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            
            df = pd.read_csv(DATASET_PATH)

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok = True)
            df.to_csv(self.data_ingestion_config.raw_data_path , header = True)

            df_train , df_test = train_test_split(df , test_size = 0.2 , random_state = 42)

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path), exist_ok = True)
            df_train.to_csv(self.data_ingestion_config.train_data_path , header = True)

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path), exist_ok = True)
            df_test.to_csv(self.data_ingestion_config.test_data_Path , header = True)

            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_Path 
            )


        except Exception as e:
            raise CustomException(e , sys)
        
if __name__ == "__main__":

    data_ingestion = DataIngestion()
    train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_array, test_array , _ = data_transformation.initiate_data_transformation(train_data_path , test_data_path)





        
    
