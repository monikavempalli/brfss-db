CODES = {
    "SEX" :{
        0:"NULL",
        1: "Male",
        2: "Female"
    },
     "_STATE":{
    0:"NULL",
    1: 'Alabama',
    2: 'Alaska',
    4: 'Arizona',
    5: 'Arkansas',
    6: 'California',
    8: 'Colorado',
    9: 'Connecticut',
    10: 'Delaware',
    11: 'District of Columbia',
    12: 'Florida',
    13: 'Georgia',
    15: 'Hawaii',
    16: 'Idaho',
    17: 'Illinois',
    18: 'Indiana',
    19: 'Iowa',
    20: 'Kansas',
    21: 'Kentucky',
    22: 'Louisiana',
    23: 'Maine',
    24: 'Maryland',
    25: 'Massachusetts',
    26: 'Michigan',
    27: 'Minnesota',
    28: 'Mississippi',
    29: 'Missouri',
    30: 'Montana',
    31: 'Nebraska',
    32: 'Nevada',
    33: 'New Hampshire',
    34: 'New Jersey',
    35: 'New Mexico',
    36: 'New York',
    37: 'North Carolina',
    38: 'North Dakota',
    39: 'Ohio',
    40: 'Oklahoma',
    41: 'Oregon',
    42: 'Pennsylvania',
    44: 'Rhode Island',
    45: 'South Carolina',
    46: 'South Dakota',
    47: 'Tennessee',
    48: 'Texas',
    49: 'Utah',
    50: 'Vermont',
    51: 'Virginia',
    53: 'Washington',
    54: 'West Virginia',
    55: 'Wisconsin',
    56: 'Wyoming',
    66: 'Guam',
    72: 'Puerto Rico'
    },
    "EDUCA":{
    1: 'Never attended school or only kindergarten',
    2: 'Grades 1 through 8 (Elementary)',
    3: 'Grades 9 through 11 (Some high school)',
    4: 'Grade 12 or GED (High school graduate)',
    5: 'College 1 year to 3 years (Some college or technical school)',
    6: 'College 4 years or more (College graduate)',
    9: 'Refused'
    },
    "INCOME2":{
    0:"NULL",
    1: 'Less than $10,000',
    2: 'Less than $15,000 ($10,000 to less than $15,000)',
    3: 'Less than $20,000 ($15,000 to less than $20,000)',
    4: 'Less than $25,000 ($20,000 to less than $25,000)',
    5: 'Less than $35,000 ($25,000 to less than $35,000)',
    6: 'Less than $50,000 ($35,000 to less than $50,000)',
    7: 'Less than $75,000 ($50,000 to less than $75,000)',
    8: '$75,000 or more',
    77: 'Dont know/Not sure',
    99: 'Refused'  
    },
    "_RACE_G1":{
    0: "NULL",
    1: "White - Non-Hispanic",
    2: "Black - Non-Hispanic",
    3: "Hispanic",
    4: "Other race only, Non-Hispanic",
    5: "Multiracial, Non-Hispanic"
    },
    "MARITAL":{
    0:"NULL",
    1: 'Married',
    2: 'Divorced',
    3: 'Widowed',
    4: 'Separated',
    5: 'Never married',
    6: 'A member of an unmarried couple',
    9: 'Refused'
    },
    "EMPLOY1":{
        0:"NULL",
    1: "Employed for wages",
    2: "Self-employed",
    3: "Out of work for 1 year or more",
    4: "Out of work for less than 1 year",
    5: "A homemaker",
    6: "A student",
    7: "Retired",
    8: "Unable to work",
    9: "Refused"
    }
}

# Dictionary for state values
state_dict = {1: "Alabama", 2: "Alaska", 4: "Arizona", 5: "Arkansas", 6: "California", 8: "Colorado", 9: "Connecticut", 10: "Delaware", 11: "District of Columbia", 12: "Florida", 13: "Georgia", 15: "Hawaii", 16: "Idaho", 17: "Illinois", 18: "Indiana", 19: "Iowa", 20: "Kansas", 21: "Kentucky", 22: "Louisiana", 23: "Maine", 24: "Maryland", 25: "Massachusetts", 26: "Michigan", 27: "Minnesota", 28: "Mississippi", 29: "Missouri", 30: "Montana", 31: "Nebraska", 32: "Nevada", 33: "New Hampshire", 34: "New Jersey", 35: "New Mexico", 36: "New York", 37: "North Carolina", 38: "North Dakota", 39: "Ohio", 40: "Oklahoma", 41: "Oregon", 42: "Pennsylvania", 44: "Rhode Island", 45: "South Carolina", 46: "South Dakota", 47: "Tennessee", 48: "Texas", 49: "Utah", 50: "Vermont", 51: "Virginia", 53: "Washington", 54: "West Virginia", 55: "Wisconsin", 56: "Wyoming", 66:"Guam", 72: "Puerto Rico"}

# Dictionary for gender values
gender_dict = {1: "Male", 2: "Female"}

# Dictionary for race values
race_dict = {1: "White", 2: "Black", 3: "Native American", 4: "Asian", 5: "Pacific Islander", 6: "Other", 7: "Multiracial"}

# Dictionary for education values
education_dict = {1: "Less than high school", 2: "High school", 3: "Some college", 4: "College graduate"}

# Dictionary for marital status values
marital_status_dict = {1: "Married", 2: "Divorced", 3: "Widowed", 4: "Separated", 5: "Never married", 6: "Unmarried couple"}

# Dictionary for income values
income_dict = {1: "Less than $10,000", 2: "$10,000 to less than $15,000", 3: "$15,000 to less than $20,000", 4: "$20,000 to less than $25,000", 5: "$25,000 to less than $35,000", 6: "$35,000 to less than $50,000", 7: "$50,000 or more", 77: "Refused", 99: "Don't know"}

health_condition_dict = {
1: 'Excellent',
2: 'Very good',
3: 'Good',
4: 'Fair',
5: 'Poor',
7: 'Don’t know/Not Sure',
9: 'Refused'
}

healthcare_access_dict = {
    1: 'Yes',
    2: 'No',
    9: 'Not sure / Don\'t Know',
    7: 'Refused',
    99: 'Not answered'
}

smoking_status_dict = {
    1: 'Current smoker - now smokes every day',
    2: 'Current smoker - now smokes some days',
    3: 'Former smoker',
    4: 'Never smoked',
    7: 'Don’t know/Refused/Missing',
    9: 'Don’t know/Refused/Missing'
}

alcohol_consumption_dict = {
1: 'No',
2: 'Yes',
9: 'Don’t know/Refused/Missing'
}

physical_activity_dict = {
    1: 'Meet Aerobic Recommendations',
    2: 'Did Not Meet Aerobic Recommendations',
    9: 'Don’t know/Not Sure/Refused/Missing'
}

chronic_conditions_dict = {
    1: 'Yes',
    2: 'No',
    7: 'Don’t know/Not sure',
    9: 'Refused'
}

pregnancy_chronic_conditions_dict = {
    1: 'Yes',
    2: 'Yes, but female told only during pregnancy',
    3: 'No',
    4: 'No, pre-diabetes or borderline diabetes',
    7: 'Don’t know/Not Sure',
    9: 'Refused'
}

age_dict = {
    1: '18-24 years',
    2: '25-34 years',
    3: '35-44 years',
    4: '45-54 years',
    5: '55-64 years',
    6: '65-74 years',
    7: '75 years or older'
}

