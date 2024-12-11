import os , sys
from src.components.Data_Ingestion import *
from src.components.Data_transformation import *
from src.components.Model_Trainer import *
from src.logger import logging
from src.exception import CustomException



if __name__ == "__main__":

    data_ingestion = DataIngestion()
    train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_array, test_array , _ = data_transformation.initiate_data_transformation(train_data_path , test_data_path)

    model_trainer = ModelTrain()
    print(model_trainer.initiate_model_trainer(train_array,test_array))