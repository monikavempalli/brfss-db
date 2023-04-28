import mysql.connector
import pandas as pd
from  constants import state_dict,gender_dict, education_dict, race_dict, marital_status_dict, income_dict
from constants import health_condition_dict,healthcare_access_dict,age_dict
from constants import smoking_status_dict,alcohol_consumption_dict, physical_activity_dict, chronic_conditions_dict, pregnancy_chronic_conditions_dict


# Create a connection to the MySQL server
mydb = mysql.connector.connect(
  host="db-project-brfss.cwlbthrgopwy.us-east-2.rds.amazonaws.com",
  user="admin",
  password="Demo_123",
  database="BRFSS"
)

# Create cursor
mycursor = mydb.cursor()

# Read the LLCP dataset into a pandas dataframe

# Define a function to insert data into the Respondents table
def insert_respondent(data):

    state = None
    if data['_STATE']:
        state_str = str(data['_STATE']).replace('.0', '')
        state = state_dict.get(int(state_str)) if state_str.isdigit() else None

    gender = None
    if data['SEX']:
        gender_str = str(data['SEX']).replace('.0', '')
        gender = gender_dict.get(int(gender_str)) if gender_str.isdigit() else None

    age = None
    #print(data['_AGE_G'])
    if data['_AGE_G']:
        age_str = str(data['_AGE_G']).replace('.0', '')
        age = age_dict.get(int(age_str)) if age_str.isdigit() else None

    race = None
    if data['_RACE']:
        race_str = str(data['_RACE']).replace('.0', '')
        race = race_dict.get(int(race_str)) if race_str.isdigit() else None

    education = None
    if data['_EDUCAG']:
        edu_str = str(data['_EDUCAG']).replace('.0', '')
        education = education_dict.get(int(edu_str)) if edu_str.isdigit() else None

    marital_status = None
    if data['MARITAL']:
        status_str = str(data['MARITAL']).replace('.0', '')
        marital_status = marital_status_dict.get(int(status_str)) if status_str.isdigit() else None

    income = None
    if data['INCOME2']:
        income_str = str(data['INCOME2']).replace('.0', '')
        income = income_dict.get(int(income_str)) if income_str.isdigit() else None

    #print(state,gender,age, race,education, marital_status, income)
    
    sql = "INSERT INTO Respondents (state, gender, age, race, education, marital_status, income) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (state, gender, age, race, education, marital_status, income)
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.lastrowid


# Define a function to insert data into the Health Conditions table
def insert_health_conditions(data, respondent_id):
    general_health = None
    if data['GENHLTH']:
        health_str = str(data['GENHLTH']).replace('.0', '')
        general_health = health_condition_dict.get(int(health_str)) if health_str.isdigit() else None

    physical_health = None
    if data['PHYSHLTH']:
        physhlth_str = str(data['PHYSHLTH']).replace('.0', '')
        if physhlth_str.isdigit() and 1 <= int(physhlth_str) <=30:
            physical_health = int(physhlth_str)
        elif physhlth_str.isdigit() and int(physhlth_str) == 88:
            physical_health =0

    mental_health = None
    if data['MENTHLTH']:
        menthlth_str = str(data['MENTHLTH']).replace('.0', '')
        if menthlth_str.isdigit() and 1 <= int(menthlth_str) <=30:
            mental_health = int(menthlth_str)
        elif menthlth_str.isdigit() and int(menthlth_str) == 88:
            mental_health =0
        
    healthcare_access = None
    if data['MEDCOST']:
        access_str = str(data['MEDCOST']).replace('.0', '')
        healthcare_access = healthcare_access_dict.get(int(access_str)) if access_str.isdigit() else None
    #print(general_health,physical_health,mental_health,healthcare_access)

    sql = "INSERT INTO `Health_Conditions` (respondent_id, general_health, physical_health, mental_health, healthcare_access) VALUES (%s, %s, %s, %s, %s)"
    val = (respondent_id, general_health, physical_health, mental_health, healthcare_access)
    mycursor.execute(sql, val)
    mydb.commit()


# Define a function to insert data into the Lifestyle Factors table
def insert_lifestyle_factors(data, respondent_id):
    smoking_status = None
    if data['_SMOKER3']:
        smoker_str = str(data['_SMOKER3']).replace('.0', '')
        smoking_status = smoking_status_dict.get(int(smoker_str)) if smoker_str.isdigit() else None
    
    alcohol_consumption = None
    if data['_RFDRHV5']:
        alcohol_str = str(data['_RFDRHV5']).replace('.0', '')
        alcohol_consumption = alcohol_consumption_dict.get(int(alcohol_str)) if alcohol_str.isdigit() else None
    
    physical_activity = None
    if data['_PAINDX1']:
        activity_str = str(data['_PAINDX1']).replace('.0', '')
        physical_activity = physical_activity_dict.get(int(activity_str)) if activity_str.isdigit() else None
    
    ## To-do: SEDENTARY to eating habits
    eat_behaviour = None
    if data['FRUIT1'] or data['VEGETAB1']:
        fruit_str = str(data['FRUIT1']).replace('.0', '')
        veget_str = str(data['VEGETAB1']).replace('.0', '')

        if fruit_str.isdigit() and veget_str.isdigit():
            if (101<= int(fruit_str) <=199 or 201<= int(fruit_str) <=299 or 301<= int(fruit_str) <=399) and (101<= int(veget_str) <=199 or 201<= int(veget_str) <=299 or 301<= int(veget_str) <=399):
                eat_behaviour = "Good"
            else:
                eat_behaviour = "Bad"
        
    ## To-do: Sleep duration change to trouble sleeping
    trouble_sleep = None
    if data['ADSLEEP']:
        sleep_str = str(data['ADSLEEP']).replace('.0', '')
        if sleep_str.isdigit() and 1<= int(sleep_str) <=14:
            trouble_sleep = int(sleep_str)
        elif sleep_str.isdigit() and int(sleep_str) == 88:
            trouble_sleep = 0
    #print(smoking_status, alcohol_consumption, physical_activity, eat_behaviour, trouble_sleep)
    sql = "INSERT INTO `Lifestyle_Factors` (respondent_id, smoking_status, alcohol_consumption, physical_activity, eat_behaviour, trouble_sleep) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (respondent_id, smoking_status, alcohol_consumption, physical_activity, eat_behaviour, trouble_sleep)
    mycursor.execute(sql, val)
    mydb.commit()


# Define a function to insert data into the Chronic Conditions table
def insert_chronic_conditions(data, respondent_id):
    diabetes = None
    if data['DIABETE3']:
        diabetes_str = str(data['DIABETE3']).replace('.0', '')
        diabetes = pregnancy_chronic_conditions_dict.get(int(diabetes_str)) if diabetes_str.isdigit() else None

    asthma = None
    if data['ASTHMA3']:
        asthma_str = str(data['ASTHMA3']).replace('.0', '')
        asthma = chronic_conditions_dict.get(int(asthma_str)) if asthma_str.isdigit() else None

    high_blood_pressure = None
    if data['BPHIGH4']:
        high_blood_pressure_str = str(data['BPHIGH4']).replace('.0', '')
        high_blood_pressure = pregnancy_chronic_conditions_dict.get(int(high_blood_pressure_str)) if high_blood_pressure_str.isdigit() else None

    high_cholesterol = None
    if data['TOLDHI2']:
        high_cholesterol_str = str(data['TOLDHI2']).replace('.0', '')
        high_cholesterol = chronic_conditions_dict.get(int(high_cholesterol_str)) if high_cholesterol_str.isdigit() else None

    heart_disease = None
    if data['CVDCRHD4']:
        heart_disease_str = str(data['CVDCRHD4']).replace('.0', '')
        heart_disease = chronic_conditions_dict.get(int(heart_disease_str)) if heart_disease_str.isdigit() else None

    stroke = None
    if data['CVDSTRK3']:
        stroke_str = str(data['CVDSTRK3']).replace('.0', '')
        stroke = chronic_conditions_dict.get(int(stroke_str)) if stroke_str.isdigit() else None

    #print(diabetes, asthma, high_blood_pressure, high_cholesterol, heart_disease, stroke)
    sql = "INSERT INTO `Chronic_Conditions` (respondent_id, diabetes, asthma, high_blood_pressure, high_cholesterol, heart_disease, stroke) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (respondent_id, diabetes, asthma, high_blood_pressure, high_cholesterol, heart_disease, stroke)
    mycursor.execute(sql, val)
    mydb.commit()


# Define a function to insert data into the Health Screening table
def insert_health_screening(data, respondent_id):
    cholesterol_screening = None
    if data['BLOODCHO']:
        cholesterol_screening_str = str(data['BLOODCHO']).replace('.0', '')
        cholesterol_screening = chronic_conditions_dict.get(int(cholesterol_screening_str)) if cholesterol_screening_str.isdigit() else None

    blood_pressure_screening = None
    if data['PDIABTST']:
        blood_pressure_screening_str = str(data['PDIABTST']).replace('.0', '')
        blood_pressure_screening = chronic_conditions_dict.get(int(blood_pressure_screening_str)) if blood_pressure_screening_str.isdigit() else None

    cancer_screening = None
    if data['HADSIGM3']:
        cancer_screening_str = str(data['HADSIGM3']).replace('.0', '')
        cancer_screening = chronic_conditions_dict.get(int(cancer_screening_str)) if cancer_screening_str.isdigit() else None

    #print(cholesterol_screening, blood_pressure_screening, cancer_screening)
    sql = "INSERT INTO `Health_Screening` (respondent_id, cholesterol_screening, blood_pressure_screening, cancer_screening) VALUES (%s, %s, %s, %s)"
    val = (respondent_id, cholesterol_screening, blood_pressure_screening, cancer_screening)
    mycursor.execute(sql, val)
    mydb.commit()


    # Loop through the rows of the dataframe and insert data into the tables
chunk_size = 1000

csv_reader = pd.read_csv("/Users/mouni/Downloads/2015.csv", chunksize=chunk_size)
#df = pd.read_csv("/Users/mouni/Downloads/2015.csv", nrows=chunk_size)
iter = 1
for df in csv_reader:
    print("iteration:::", iter)
    for index, row in df.iterrows():
        respondent_id = insert_respondent(row)
        insert_health_conditions(row, respondent_id)
        insert_lifestyle_factors(row, respondent_id)
        insert_chronic_conditions(row, respondent_id)
        insert_health_screening(row, respondent_id)
        iter = iter + 1

   
