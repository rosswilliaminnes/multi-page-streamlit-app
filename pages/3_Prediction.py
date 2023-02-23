import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly_express as px
import os 

from src.predictions import scaled_pred

# set path of directory
path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir = dir.replace('pages', 'data')

# set file path of saved model and scalar for model if applicable
model_name = "ridge_model.sav"
scaled_file_name = "ridge_scalar.sav"
saved_model = dir+"/"+model_name
saved_model_scalar = dir+"/"+scaled_file_name

# code for the page

st.title("Predict MPG")
st.markdown("Enter values below to see the MPG prediction")


number1 = st.number_input('displacement',value=300)
st.write('The current number is ', number1)

number2 = st.number_input('horsepower',value=130)
st.write('The current number is ', number2)

number3 = st.number_input('weight',value=3500)
st.write('The current number is ', number3)

number4 = st.number_input('acceleration',value=12)
st.write('The current number is ', number4)

number5 = st.number_input('model year',value=70)
st.write('The current number is ', number5)




option = st.selectbox(
    'number of cylinders',
    ('4 cyln', '8 cyln', '6 cyln', '3 cyln', '5 cyln'))
st.write('You selected:', option)

option2 = st.selectbox(
    'origin',
    ('origin one', 'origin two', 'origin three'))

st.write('You selected:', option2)

if option == '4 cyln':
    number6 = 1 
    number7 = 0 
    number8 = 0
    number9 = 0
    number10 = 0
elif option == '8 cyln':
    number6 = 0 
    number7 = 1 
    number8 = 0
    number9 = 0
    number10 = 0
elif option == '6 cyln':
    number6 = 0 
    number7 = 0 
    number8 = 1
    number9 = 0
    number10 = 0
elif option == '3 cyln':
    number6 = 0 
    number7 = 0 
    number8 = 0
    number9 = 1
    number10 = 0
elif option == '5 cyln':
    number6 = 0 
    number7 = 0 
    number8 = 0
    number9 = 0
    number10 = 1

if option2 == 'origin one':
    number11 = 1 
    number12 = 0 
    number13 = 0
elif option2 == 'origin two':
    number11 = 0 
    number12 = 1 
    number13 = 0
elif option2 == 'origin three':
    number11 = 0 
    number12 = 0 
    number13 = 1

st.write(number6, number7, number8, number9, number10, number11, number12, number13)



if st.sidebar.button("Predict MPG"):
    result = scaled_pred(np.array([[number1, number2, number3, number4, number5, 
    number6, number7, number8, number9, number10, number11, number12, number13]]),saved_model,saved_model_scalar)
    st.sidebar.text(round(result[0],2))




