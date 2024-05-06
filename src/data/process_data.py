import pandas as pd

students_csv = pd.read_csv('../../data/raw/students_scores.csv')
students_school_xlsx = pd.read_excel('../../data/raw/students.xlsx')

print(students_csv)
print(students_school_xlsx)

merged_data = pd.merge(students_csv, students_school_xlsx)
print(merged_data)

merged_data['AVG_subject'] = merged_data[['STEM_subjects', 'H_subjects']].mean(axis=1)
print(merged_data)
merged_data.drop(columns=merged_data.columns[0], axis=1, inplace=True)

merged_data.to_csv('../../data/processed/current_data.csv', index=False)