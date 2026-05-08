import pandas as pd
import os

FILE_NAME = "students.csv"

def save_student(data):
    df = pd.DataFrame([data])
    
    if os.path.exists(FILE_NAME):
        df.to_csv(FILE_NAME, mode='a', header=False, index=False)
    else:
        df.to_csv(FILE_NAME, index=False)

def load_students():
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)
    return pd.DataFrame()

def get_all_students():
    df = load_students()
    if df.empty:
        return []
    return df.to_dict('records')

def search_student_by_name(name):
    df = load_students()
    if df.empty:
        return []
    result = df[df['name'].str.lower().str.contains(name.lower(), na=False)]
    return result.to_dict('records')