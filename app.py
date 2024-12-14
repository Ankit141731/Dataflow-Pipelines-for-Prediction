import streamlit as st
import numpy as np
import pandas as pd
from src.pipeline.Prediction_pipeline import *

st.title("Machine Learning Project") 




Age = st.slider("Select your Age" , 10 , 100)

Work_class = st.selectbox("Choose your work class" ,
                           [
                               "State Government", 
                               "Federal Government" ,
                               "Local Government" ,
                               "Private Sector" ,
                               "Self Employement Incorporated" ,
                               "Self employment not incorporated" ,
                               "Without any Pay", 
                               "Never Worked" ,

                            ])

Education =  st.selectbox("Choose Your Highest Qualification" ,
                         [
                             "Bachelors" ,
                             "Masters" ,
                             "Doctorate" ,
                             "Preschool" ,
                             "1st - 4th" ,
                             "5th - 6th" ,
                             "7th - 8th" ,
                             "9th" ,
                             "10th" ,
                             "11th" ,
                             "12th" ,
                             "Associate academic" ,
                             "High school Graduate" ,
                             "Some College" ,
                             "Associate in Vocational" ,
                             "Professional School"
                        
                         ])

Marital_Status = st.selectbox("Choose your Marital Status" ,
                              [
                                  "Divorced" ,
                                  "Maried - AF - Spouse" ,
                                  "Married - Civ - Spouse" ,
                                  "Married Spouse Absent" ,
                                  "Never Married" ,
                                  "Separated" ,
                                  "Widowed"
                              ])

Occupation = st.selectbox("Choose your occupation" ,
                          [
                              "Adm-clerical" ,
                              "Exec-managerial" ,
                              "Handlers-cleaners" ,
                              "Prof-specialty" ,
                              "Other-service" ,
                              "Sales" ,
                              "Craft-repair" ,
                              "Transport-moving" ,
                              "Farming-fishing" ,
                              "Machine-op-inspct" ,
                              "Tech-support" ,
                              "Protective-serv" ,
                              "Armed-Forces" ,
                              "Priv-house-serv" ,
                          ])

Relationship = st.selectbox("Choose your Relationships" ,
                            [
                                "Not-in-family" ,
                                "Husband" ,
                                "Wife" ,
                                "Own-child" ,
                                "Unmarried" ,
                                "Other-relative" ,
                            ])

Race = st.selectbox("Choose your race" ,
                    [
                        "White" ,
                        "Black" ,
                        "other" ,
                        "Asian-Pac-Islander" ,
                        "Amer-Indian-Eskimo" ,

                    ])

Sex = st.radio("Choose your Gender" , ["Male" , "Female"])

Capital_Gain  = st.number_input(
    label="Enter your Capital Gain:",
    min_value=0,  # Minimum value allowed
    max_value=None,  # No upper limit
    value=0,  # Default value
    step=1,  # Increment step
    format="%d"  # Format for integers
)

Capital_Loss = st.number_input(
    label = "Enter your Capital Loss:" ,
    min_value = 0 ,
    max_value = None ,
    value = 0,
    step = 1,
    format = "%d"
)

Hours_per_Week = st.number_input(
    label="Enter your hours per week:",
    min_value=0,  
    max_value=None,  
    value=0,  
    step=1,  
    format="%d"  
)

Native_Country = st.selectbox("Choose your Country",
                              [
    "United-States", "Cuba", "Jamaica", "India", "Mexico", "South", 
    "Puerto-Rico", "Honduras", "England", "Canada", "Germany", "Iran", 
    "Philippines", "Italy", "Poland", "Columbia", "Cambodia", "Thailand", 
    "Ecuador", "Laos", "Taiwan", "Haiti", "Portugal", "Dominican-Republic", 
    "El-Salvador", "France", "Guatemala", "China", "Japan", "Yugoslavia", 
    "Peru", "Outlying-US(Guam-USVI-etc)", "Scotland", "Trinadad-Tobago", 
    "Greece", "Nicaragua", "Vietnam", "Hong", "Ireland", "Hungary", 
    "Holand-Netherlands"
]

                              )


Feature_mapping_Work_class = {
                               "State Government" : 6 , 
                               "Federal Government" : 0 ,
                               "Local Government" :1 ,
                               "Private Sector": 3,
                               "Self Employement Incorporated" : 4 ,
                               "Self employment not incorporated":5 ,
                               "Without any Pay":7 , 
                               "Never Worked" : 2,

}

Feature_mapping_education = {
                             "Bachelors" : 13,
                             "Masters":14 ,
                             "Doctorate":16 ,
                             "Preschool" :1,
                             "1st - 4th":2 ,
                             "5th - 6th" :3,
                             "7th - 8th" :4,
                             "9th":5 ,
                             "10th":6 ,
                             "11th" : 7,
                             "12th":8 ,
                             "Associate academic" :12,
                             "High school Graduate":9 ,
                             "Some College":10 ,
                             "Associate in Vocational":11 ,
                             "Professional School":15
                

}

Feature_mappping_Marital_status = {
                                  "Divorced" :0,
                                  "Maried - AF - Spouse" :1,
                                  "Married - Civ - Spouse":2 ,
                                  "Married Spouse Absent":3 ,
                                  "Never Married" : 4,
                                  "Separated":5 ,
                                  "Widowed":6

}

Feature_mapping_Occupation = {

                              "Adm-clerical":0 ,
                              "Exec-managerial":3 ,
                              "Handlers-cleaners":5 ,
                              "Prof-specialty":9 ,
                              "Other-service": 7,
                              "Sales":11 ,
                              "Craft-repair":2 ,
                              "Transport-moving": 13,
                              "Farming-fishing": 4,
                              "Machine-op-inspct":6 ,
                              "Tech-support":12 ,
                              "Protective-serv":10 ,
                              "Armed-Forces":1 ,
                              "Priv-house-serv" :8,
}

Feature_mapping_Relationship = {
                                "Not-in-family":1 ,
                                "Husband":0 ,
                                "Wife": 5,
                                "Own-child":3 ,
                                "Unmarried": 4,
                                "Other-relative":2 ,
}

Feature_mapping_Race = {
                        "White":4 ,
                        "Black" :2,
                        "other":3 ,
                        "Asian-Pac-Islander":1 ,
                        "Amer-Indian-Eskimo":0 ,
}

Feature_mapping_sex = {
    "Female":0,
    "Male":1
}

Feature_mapping_countries = {
    "United-States": 38,
    "Cuba": 4,
    "Jamaica": 22,
    "India": 18,
    "Mexico": 25,
    "South": 34,
    "Puerto-Rico": 32,
    "Honduras": 15,
    "England": 8,
    "Canada": 1,
    "Germany": 10,
    "Iran": 19,
    "Philippines": 29,
    "Italy": 21,
    "Poland": 30,
    "Columbia": 3,
    "Cambodia": 0,
    "Thailand": 36,
    "Ecuador": 6,
    "Laos": 24,
    "Taiwan": 35,
    "Haiti": 13,
    "Portugal": 31,
    "Dominican-Republic": 5,
    "El-Salvador": 7,
    "France": 9,
    "Guatemala": 12,
    "China": 2,
    "Japan": 23,
    "Yugoslavia": 40,
    "Peru": 28,
    "Outlying-US(Guam-USVI-etc)": 27,
    "Scotland": 33,
    "Trinadad-Tobago": 37,
    "Greece": 11,
    "Nicaragua": 26,
    "Vietnam": 39,
    "Hong": 16,
    "Ireland": 20,
    "Hungary": 17,
    "Holand-Netherlands": 14
}

if st.button("Submit") :
    User_Input = CustomClass(
        Age,
        Feature_mapping_Work_class[Work_class],
        Feature_mapping_education[Education],
        Feature_mappping_Marital_status[Marital_Status],
        Feature_mapping_Occupation[Occupation],
        Feature_mapping_Relationship[Relationship],
        Feature_mapping_Race[Race],
        Feature_mapping_sex[Sex],
        Capital_Gain,
        Capital_Loss,
        Hours_per_Week,
        Feature_mapping_countries[Native_Country]
    

    )

    Feature_values = User_Input.get_data_DataFrame()

    Pipeline = PredictionPipeline()
    Prediction_value = Pipeline.predict(Feature_values)

    if Prediction_value == 1:
        st.info("Salary is More than 50 thousand dollars")
    elif Prediction_value == 0:
        st.warning("Salary is less than 50 thousand dollars")
    else:
        st.error("Try again After some time")




















