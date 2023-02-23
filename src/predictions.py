import streamlit as st
import joblib
import numpy as np
import os

# set path of directory
'''path = os.path.realpath(__file__)
dir = os.path.dirname(path)
# change the reference to the data folder
dir = dir.replace('src', 'data')'''



# use this for predicting from non scaled data

def pred(data,saved_model):
    #this could be for a random forest or ols
    #that doesnt need scaling
    model = joblib.load(saved_model)
    return model.predict(data)

# use this for predicting from scaled data

def scaled_pred(data,saved_model,saved_model_scalar):
    model = joblib.load(saved_model)
    scalar = joblib.load(saved_model_scalar)
    scaled_data = scalar.transform(data)
    return model.predict(scaled_data)

