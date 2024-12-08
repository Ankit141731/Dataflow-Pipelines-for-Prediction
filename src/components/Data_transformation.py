import os , sys
import numpy as np
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from src.utilities import save_object
from src.constants import *

@dataclass
class DataTransformationConfig :

        preprocessor_obj_file_path = os.path.join(
            CURRENT_DIR_KEY , 
            ARTIFACT_DIR ,
            ARTIFACT_DIR_KEY2,
            "preprocessor.pkl"
            )
        
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_tranformation_obj(self):
        try:

            logging.info("Data transformation started")

            numerical_features = [ 'age', 'workclass',  
            'education_num', 'marital_status','occupation', 'relationship', 'race', 'sex', 'capital_gain',
            'capital_loss', 'hours_per_week', 'native_country'
                                   ]
            numerical_features_pipeline = Pipeline(
                steps = [
                    ("impute" , SimpleImputer(strategy = "median")) ,
                    ("scaler" ,StandardScaler())
                    ]
            )

            preprocessor = ColumnTransformer([
                ("numerical_features_pipeline" , numerical_features_pipeline , numerical_features)
            ])

            return preprocessor

        except Exception as e:
            raise CustomException(e , sys)
        

    def detect_outlier(self ,col , df):
        try:

            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)

            IQR = Q3 - Q1

            upper_limit = Q3 + 1.5 * IQR
            lowwer_limit = Q1 - 1.5 * IQR

            df.loc[(df[col]>upper_limit), col] = upper_limit
            df.loc[(df[col]<lowwer_limit), col] = lowwer_limit

            return df

        except Exception as e:
            raise CustomException(e , sys)
        
    def initiate_data_transformation(self , train_path , test_path):

        try:
            
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            numerical_features = ['age', 'workclass',  'education_num', 'marital_status',
            'occupation', 'relationship', 'race', 'sex', 'capital_gain',
            'capital_loss', 'hours_per_week', 'native_country']

            for column in numerical_features:
                self.detect_outlier(col = column , df = train_df)

            for column in numerical_features:
                self.detect_outlier(col = column , df = test_df)

            preprocessor_obj = self.get_data_tranformation_obj()

            target_column = "income"
            dropping_columns = [target_column]

            logging.info("splitting data into independent and dependent features")

            input_features_train_df = train_df.drop(dropping_columns , axis = 1)
            target_feature_train_df = train_df[target_column]

            input_features_test_df = test_df.drop(dropping_columns  , axis = 1)
            target_feature_test_df = test_df[target_column]

            logging.info("apply tranformation on our train and test data")

            input_featues_train_array = preprocessor_obj.fit_transform(input_features_train_df)
            input_features_test_array = preprocessor_obj.transform(input_features_test_df)

            train_array = np.c_[input_featues_train_array , np.array(target_feature_train_df)]
            test_array = np.c_[input_features_test_array , np.array(target_feature_test_df)]

            save_object(file_path = self.data_transformation_config.preprocessor_obj_file_path ,
                        obj = preprocessor_obj)
            
            return (train_array,
                    test_array,
                    self.data_transformation_config.preprocessor_obj_file_path)

        except Exception as e:
            raise CustomException(e , sys)


