from flask import request
from flask import Flask
from joblib import load
import pandas as pd

app = Flask(__name__)

model=load("../models/model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame.from_records(data)
    print(df)
    vhod = df.drop(["Dropout"], axis=1).columns

    predictions=model.predict(df[vhod])
    print(predictions)
    rounded_prediction = round(predictions, 2)
    return {'prediction': rounded_prediction}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
