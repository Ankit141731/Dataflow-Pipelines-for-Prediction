import os , sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from src.utilities import *
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from src.constants import *
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

@dataclass
class ModelTrainerConfig:
    model_trainer_obj_filepath = os.path.join(
        CURRENT_DIR_KEY,
        ARTIFACT_DIR,
        ARTIFACT_DIR_KEY3,
        "model_trainer.pkl"
    )

class ModelTrain:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self , train_array , test_array):
        try:
            
            logging.info("splitting our data into dependent and independent features")

            X_train , y_train , X_test , y_test = (

                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1],

            )

            model = {
                "Random_forest" : RandomForestClassifier() ,
                "Decision_tree" : DecisionTreeClassifier() ,
                "Logistic_regression" : LogisticRegression()
            }

            parameters = {
                "Random_forest":{
                    "class_weight":["balanced"],
                    'n_estimators': [20, 50, 30],
                    'max_depth': [10, 8, 5],
                    'min_samples_split': [2, 5, 10],
                },
                "Decision_tree":{
                    "class_weight":["balanced"],
                    "criterion":['gini',"entropy","log_loss"],
                    "splitter":['best','random'],
                    "max_depth":[3,4,5,6],
                    "min_samples_split":[2,3,4,5],
                    "min_samples_leaf":[1,2,3],
                    "max_features":["auto","sqrt","log2"]
                },
                "Logistic_regression":{
                    "class_weight":["balanced"],
                    'penalty': ['l1', 'l2'],
                    'C': [0.001, 0.01, 0.1, 1, 10, 100],
                    'solver': ['liblinear', 'saga']
                }
            }

            model_report:dict = evaluate_model(
                X_train = X_train , X_test = X_test ,y_train = y_train  , y_test = y_test,
                models = model , params = parameters
            )

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = model[best_model_name]
            print(f"Best Model Found, Model Name is: {best_model_name},Accuracy_Score: {best_model_score}")
            print("\n***************************************************************************************\n")
            logging.info(f"best model found, Model Name is {best_model_name}, accuracy Score: {best_model_score}")


            save_object(file_path=self.model_trainer_config.model_trainer_obj_filepath,
                        obj = best_model
                        )
        except Exception as e:
            raise CustomException(e, sys)