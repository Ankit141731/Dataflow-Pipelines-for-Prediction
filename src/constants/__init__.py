import os , sys
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%d-%m-%y-%H-%M-%S")

DATA_DIR = "Data"
DATA_DIR_KEY = "clean_data.csv"


CURRENT_DIR_KEY = os.getcwd()

CURRENT_TIME_STAMP = get_current_time()

ARTIFACT_DIR = "Artifact"
ARTIFACT_DIR_KEY1 = "Data_ingestion"
RAW_DATA_DIR = "Raw_data"
RAW_DATA_DIR_KEY = "Raw.csv"
DATA_SPLIT_DIR = "Data_Split"
DATA_SPLIT_DIR_KEY1 = "Train.csv"
DATA_SPLIT_DIR_KEY2 = "Test.csv"


ARTIFACT_DIR_KEY2 = "Data_transformation"




