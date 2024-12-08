import os , sys
import logging
from datetime import datetime

LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd() , LOG_DIR)

os.makedirs(LOG_DIR , exist_ok = True)

CURRENT_TIME_STAMP = f'{datetime.now().strftime("%d-%m-%y-%H-%M-%S")}'

LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

LOG_FILE_PATH = os.path.join(LOG_DIR , LOG_FILE_NAME)

logging.basicConfig(
    filename = LOG_FILE_PATH ,
    filemode = "w" ,
    format = '[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO,
)
