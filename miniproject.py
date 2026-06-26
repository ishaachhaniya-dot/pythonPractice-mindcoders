import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv("students.csv")
    print("CSV Loaded Successfully")
except FileNotFoundError:
    print("File Not Found")
    exit()

# Remove extra spaces from column names
df.columns = df.columns.str.strip()
#check missing values
print(df.isnull().sum())
#fill missing values
print(df.fillna(0, inplace=True))

#calculate total marks
subjects = [
    'Math',
    'Science',
    'English',
    'Computer',
    'History'
]
df['total']=df[subjects].sum(axis=1)
print([['name','total']])

#calculare average
#number of subjects

df['Average'] = df[subjects].mean(axis=1)

#calculate grade
def get_grade(x):
    if x>=90:
        return'A+'
    elif x>=80:
        return 'A'
    elif x>=70:
        return 'B'
    elif x>=60:
        return 'C'
    else:
        return 'F'
#calculating grade
df['Grade'] = df['Average'].apply(get_grade)
print(df[['Name', 'Grade']])



