# data = {'age': '1', 'sex': '1', 'cp': '1', 'trestbps': '1', 'chol': '1', 'fbs': '1', 'restecg': '1', 'thalach': '1', 'exang': '1', 'oldpeak': '1', 'slope': '1', 'ca': '1', 'thal': '1'}

import pandas as pd
import numpy as np
import pickle

def data_extracter_cum_converter(data):
    extracted = data.items()
    col_names = (i[0] for i in extracted)
    values = (float(i[-1]) for i in extracted)
    converted = {i:j for i,j in zip(col_names,values)}
    return converted

def predictor(data):
    model = pickle.load(open('log_reg.pickle','rb'))
    converted = data_extracter_cum_converter(data)
    new_dataframe = pd.DataFrame([converted])
    prediction = model.predict(new_dataframe)[0]
    output = {'prediction':prediction}
    return output