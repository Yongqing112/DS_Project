import pandas as pd

def caculate(df, academic_year, column):
    dates = df[(df["學年度"] == academic_year)]
    numberOfPeople = 0
    for x in dates[column]:
        numberOfPeople += x

    a = {"學年度": academic_year, column: numberOfPeople}

    data = pd.DataFrame()
    data = pd.concat([data, pd.DataFrame([a])], ignore_index=True) 
    return data

def not_higher_education_and_not_get_job(df, data, start_academic_year, end_academic_year, columns):
    
    for column in columns:
        for year in range(start_academic_year, end_academic_year+1):
            temp = caculate(df, year, column)
            data = pd.concat([data, temp], ignore_index=True)
    return data