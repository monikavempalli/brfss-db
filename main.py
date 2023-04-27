import pandas as pd
import constants
from data_cleaner import clean_state

def read_csv():
    df = pd.read_csv("/Users/mouni/Downloads/2015.csv", nrows=500)
    #print(df.head())
    personal_info = df[["_STATE", "IDATE", "IMONTH", "IDAY", "IYEAR", "SEX", "EDUCA", "INCOME2", "SEQNO", "_RACE_G1", "MARITAL", "EMPLOY1"]]
    read_personal_info(personal_info)

def read_personal_info(personal_info):
    #print(personal_info)
    state = clean_state(personal_info)

def main():
    print("Hello, world!")
    read_csv()
    
if __name__ == "__main__":
    main()