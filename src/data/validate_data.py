import pandas as pd

current_data = pd.read_csv('../../data/processed/current_data.csv')
reference_data = pd.read_csv('../../data/processed/reference_dataset.csv')

number_of_cols_current=len(current_data.axes[1])
number_of_cols_reference=len(reference_data.axes[1])

if number_of_cols_current==number_of_cols_reference:
    if reference_data.equals(current_data):
        print("SUCCESS: Datasets have the same column length, have the same columns names and same column types.")
    else:
        print("ERROR: Datasets have the same column length, but do not have the same columns names and same column types.")
else:
    print("ERROR: Datasets do not have the same column length, so they cannot have the same column names and types.")

## This returns "Datasets do not have the same column lenght", as current_data has AVG_subject and reference_data does not