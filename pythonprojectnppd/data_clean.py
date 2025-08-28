#importing libraries
import pandas as pd
import numpy as np

#importing dataset
df = pd.read_csv('Messy_Employment_India_Dataset.csv')
print(df.head())

#checking missing values 
print("Missing values in each column")
print(df.isnull().sum())

#filling salary column with average value 
df['Monthly Salary (INR)'] = df['Monthly Salary (INR)'].fillna(df['Monthly Salary (INR)'].mean().astype(int))

#filling years of experience column with median value
df['Years of Experience'] = df['Years of Experience'].fillna(df['Years of Experience'].median())

#filling columns with mode value
df['Age Group'] = df['Age Group'].fillna(df['Age Group'].mode()[0])
df['Industry'] = df['Industry'].fillna(df['Industry'].mode()[0])
df['AI Risk'] = df['AI Risk'].fillna(df['AI Risk'].mode()[0])

#filling columns with unknown value
df['Education'] = df['Education'].fillna("Not Provided")
df['Location'] = df['Location'].fillna("Not Provided")
                                       
#filling salary column with loc      
df.loc[df['Status'].isna() & (df['Monthly Salary (INR)'] > 0), 'Status'] = "Employed"
df.loc[df['Status'].isna() & (df['Monthly Salary (INR)'] == 0), 'Status'] = "Unemployed"

#replacing and filling infinite numbers
df.replace([np.inf, -np.inf], np.nan, inplace = True)
df.fillna(df.mean , inplace = True)

#changing DataFrame to proper case
df = df.apply(lambda x: x.str.title() if x.dtype == "object" else x)

df['Age Group'] = df['Age Group'].str.replace('_', '-').str.replace(' ', '').str.replace('To', '-')

#removing duplicates
df.drop_duplicates(inplace = True)

#replacing negative salaries
df['Monthly Salary (INR)'] = np.where(df['Monthly Salary (INR)']< 0, df['Monthly Salary (INR)'].mean(), df['Monthly Salary (INR)'])     


df.to_csv("Cleaned_India_Employement_Dataset.csv", index=False)
print("Data Cleaning Completed! Saved as Cleaned_India_Employement_Dataset")
