
Project Overview-:
This project cleans and preprocesses a messy employment dataset from India. The raw dataset had missing values, inconsistent formatting, duplicates, and incorrect salary values.
After cleaning, the dataset is ready for analysis and saved as Cleaned_India_Employment_Dataset.csv.

Data Cleaning Steps Performed-:

Filled missing values
Salary → mean;
Years of Experience → median;
Age Group, Industry, AI Risk → mode;
Education & Location → "Not Provided";
Status → set as "Employed" or "Unemployed" based on salary;
Standardized and fixed data;
Converted text columns to proper case;
Fixed age group formatting (e.g., 20_to_30 → 20-30);
Removed duplicates;
Replaced negative or infinite salary values with average;
Exported cleaned dataset as Cleaned_India_Employment_Dataset.csv;


Files in Repository-:

Messy_Employment_India_Dataset.csv → Original dataset;
data_clean.py → Python script for cleaning;
Cleaned_India_Employment_Dataset.csv → Final cleaned dataset;
Cleaned_India_Employment_Dataset.csv → excel file dataset;

How to Run the Script-:

1. Clone the repository

git clone https://github.com/nehadimri9027/cleaned-employees-dataset-project.git
cd cleaned-employees-dataset-project


2. Install dependencies

pip install pandas numpy

3. Run the script

python data_clean.py


Cleaned dataset will be saved as Cleaned_India_Employment_Dataset.csv

Tech Stack-:
Python (Pandas, NumPy)
CSV dataset
