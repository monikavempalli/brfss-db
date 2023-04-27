import pandas as pd
from  constants import CODES
import numpy as np


def clean_state(personal_info):
    personal_info['_STATE'].fillna(0,inplace = True)
    personal_info['_STATE'] = personal_info['_STATE'].astype(str).str.replace('\.0', '').astype(int)

    #personal_info['_STATE'] = personal_info['_STATE'].map(CODES['_STATE'])
    
    personal_info['SEX'].fillna(0,inplace = True)
    personal_info['SEX'] = personal_info['SEX'].astype(str).str.replace('\.0', '').astype(int)
    #personal_info['SEX'] = personal_info['SEX'].map(CODES["SEX"])
    
    personal_info['IMONTH'] = personal_info['IMONTH'].apply(lambda x: x.decode('utf-8')[2:4])
    personal_info['IDAY'] = personal_info['IDAY'].apply(lambda x: x.decode('utf-8')[2:4])
    personal_info['IYEAR'] = personal_info['IYEAR'].apply(lambda x: x.decode('utf-8')[2:6])
    
    personal_info['_RACE_G1'].fillna(0,inplace = True)
    personal_info['_RACE_G1'] = personal_info['_RACE_G1'].astype(str).str.replace('\.0', '').astype(int)
    #personal_info['_RACE_G1'] = personal_info['_RACE_G1'].map(CODES["_RACE_G1"])
    
    personal_info['MARITAL'].fillna(0,inplace = True)
    personal_info['MARITAL'] = personal_info['MARITAL'].astype(str).str.replace('\.0', '').astype(int)
    #personal_info['MARITAL'] = personal_info['MARITAL'].map(CODES["MARITAL"])

    personal_info['EMPLOY1'].fillna(0,inplace = True)
    personal_info['EMPLOY1'] = personal_info['EMPLOY1'].astype(str).str.replace('\.0', '').astype(int)
    #personal_info['EMPLOY1'] = personal_info['EMPLOY1'].map(CODES["EMPLOY1"])

    personal_info['EDUCA'].fillna(0,inplace = True)
    personal_info['EDUCA'] = personal_info['EDUCA'].astype(str).str.replace('\.0', '').astype(int)
    #personal_info['EDUCA'] = personal_info['EDUCA'].map(CODES["EDUCA"])

    personal_info['INCOME2'].fillna(0,inplace = True)
    personal_info['INCOME2'] = personal_info['INCOME2'].astype(str).str.replace('\.0', '').astype(int)
    #personal_info['INCOME2'] = personal_info['INCOME2'].map(CODES["INCOME2"])
    #print( personal_info.head()['_STATE'])
    #personal_info['_STATE'] = personal_info['_STATE'].fillna(None)
    print(personal_info.head())


    # personal_info['_STATE'] = personal_info['_STATE'].map(CODES["_STATE"])
    # personal_info['_STATE'] = personal_info['_STATE'].fillna(None)
    # print(personal_info.head())
    