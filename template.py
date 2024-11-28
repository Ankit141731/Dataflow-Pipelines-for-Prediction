import os , sys
import logging
from pathlib import Path

PROJECT_NAME = "src"

list_of_files = [

    f"{PROJECT_NAME}/__init__.py" ,
    f"{PROJECT_NAME}/components/__init__.py" ,
    f"{PROJECT_NAME}/exception/__init__.py" ,
    f"{PROJECT_NAME}/logger/__init__.py" ,
    f"{PROJECT_NAME}/entities/__init__.py" ,
    f"{PROJECT_NAME}/utilities/__init__.py" ,
    f"{PROJECT_NAME}/configs/__init__.py" ,
    f"{PROJECT_NAME}/pipeline/__init__.py" ,
    f"{PROJECT_NAME}/constants/__init__.py" ,
    "app.py" ,
    "exception.py" ,
    "main.py" ,
    "logs.py" ,
    f"configs/config.yaml" ,
    "schema.yaml" ,
    "setup.py",
]

for file in list_of_files:
    filepath = Path(file)

    filedir , filename = os.path.split(filepath)

    if filedir == "":
        filedir = "."

    if filedir != "":
        os.makedirs(filedir , exist_ok = True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):

        os.makedirs(filedir , exist_ok = True)

        with open(filepath , "w") as f:
            pass

    else:
        logging.info(f"File already exists at :{filedir}")



