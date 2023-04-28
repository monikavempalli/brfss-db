import csv
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
  host="db-project-brfss.cwlbthrgopwy.us-east-2.rds.amazonaws.com",
  user="admin",
  password="Demo_123",
  database="BRFSS"
)
cursor = db.cursor()

# Create the tables
cursor.execute("""
CREATE TABLE Respondents (
  id INT PRIMARY KEY,
  state VARCHAR(2),
  gender VARCHAR(6),
  age INT,
  race VARCHAR(1),
  education VARCHAR(2),
  marital_status VARCHAR(1),
  income INT
)
""")
cursor.execute("""
CREATE TABLE Health_Conditions (
  id INT PRIMARY KEY,
  respondent_id INT,
  general_health INT,
  physical_health INT,
  mental_health INT,
  healthcare_access INT,
  FOREIGN KEY (respondent_id) REFERENCES Respondents(id)
)
""")
cursor.execute("""
CREATE TABLE Lifestyle_Factors (
  id INT PRIMARY KEY,
  respondent_id INT,
  smoking_status VARCHAR(2),
  alcohol_consumption VARCHAR(1),
  physical_activity VARCHAR(1),
  sedentary_behaviour VARCHAR(1),
  sleep_duration INT,
  FOREIGN KEY (respondent_id) REFERENCES Respondents(id)
)
""")
cursor.execute("""
CREATE TABLE Chronic_Conditions (
  id INT PRIMARY KEY,
  respondent_id INT,
  diabetes VARCHAR(1),
  asthma VARCHAR(1),
  high_blood_pressure VARCHAR(1),
  high_cholesterol VARCHAR(1),
  heart_disease VARCHAR(1),
  stroke VARCHAR(1),
  FOREIGN KEY (respondent_id) REFERENCES Respondents(id)
)
""")
cursor.execute("""
CREATE TABLE Health_Screening (
  id INT PRIMARY KEY,
  respondent_id INT,
  cholesterol_screening VARCHAR(1),
  blood_pressure_screening VARCHAR(1),
  cancer_screening VARCHAR(1),
  FOREIGN KEY (respondent_id) REFERENCES Respondents(id)
)
""")