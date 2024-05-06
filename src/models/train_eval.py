import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn import tree
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

df = pd.read_csv('../../data/processed/current_data.csv')

print(len(df))
df = df.iloc[:-1 , :]
print(len(df))

izhod="Dropout"
vhod=df.drop(["Dropout"], axis=1).columns

numeric_columns = df[vhod].select_dtypes(include=['float64', 'int64']).columns
categorical_columns = df[vhod].select_dtypes(include=['object']).columns

transformacija_numericnih = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

transformacija_kateoričnih = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', transformacija_numericnih, numeric_columns),
        ('cat', transformacija_kateoričnih, categorical_columns)
    ])

data_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', tree.DecisionTreeClassifier())
])

data_pipeline.fit(df[vhod], df[izhod])

model_path = '../../models/model.pkl'
joblib.dump(data_pipeline, model_path)
