import pandas as pd

def caculate(df, academic_year, school_type, column):
    datas = df[(df["學年度"] == academic_year)]
    datas = datas[df["學程別"] == school_type]
    numberOfPeople = 0
    for x in datas[column]:
        numberOfPeople += x

    a = {"學年度": academic_year, column: numberOfPeople}

    data = pd.DataFrame()
    data = pd.concat([data, pd.DataFrame([a])], ignore_index=True) 
    
    return data

def not_higher_education_and_not_get_job(df, data, start_academic_year, end_academic_year, school_type, columns):
    
    for column in columns:
        for year in range(start_academic_year, end_academic_year+1):
            temp = caculate(df, year, school_type, column)
            data = pd.concat([data, temp], ignore_index=True)
    return data

def caculate_percent(df, academic_year, school_type, people, column):
    datas = df[(df["學年度"] == academic_year)]
    datas = datas[(df["學程別"] == school_type)]
    numberOfPeople = 0
    for x in datas[column]:
        numberOfPeople += x
    
    total = people[(people["學年度"] == academic_year)]
    total = total[(people["學程別"] == school_type)]
    # print(total)
    percent = (numberOfPeople / total["總人數"]) * 100
    a = {"學年度": academic_year, "學程別": school_type, column: percent}

    data = pd.DataFrame()
    data = pd.concat([data, pd.DataFrame([a])], ignore_index=True) 
    
    return data

def not_higher_education_and_not_get_job_percent(df, data, start_academic_year, end_academic_year, school_types, people, column):
    
    for school_type in school_types:
        for year in range(start_academic_year, end_academic_year+1):
            temp = caculate_percent(df, year, school_type, people, column)
            data = pd.concat([data, temp], ignore_index=True)
    return data

def caculate_percent2(df, academic_year, school_type, people, column):
    datas = df[(df["學年度"] == academic_year)]
    datas = datas[(df["學程別"] == school_type)]
    numberOfPeople = 0
    for x in datas[column]:
        numberOfPeople += x
    
    total = people[(people["學年度"] == academic_year)]
    total = total[(people["學程別"] == school_type)]
    # print(total)
    percent = (numberOfPeople / total["總人數"]) * 100
    a = {"學年度": academic_year, column: percent}

    data = pd.DataFrame()
    data = pd.concat([data, pd.DataFrame([a])], ignore_index=True) 
    
    return data

def not_higher_education_and_not_get_job_percent2(df, data, start_academic_year, end_academic_year, school_types, people, column):
    
    for school_type in school_types:
        for year in range(start_academic_year, end_academic_year+1):
            temp = caculate_percent2(df, year, school_type, people, column)
            data = pd.concat([data, temp], ignore_index=True)
    return data