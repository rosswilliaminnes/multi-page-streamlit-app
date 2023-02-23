import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly_express as px
import os 

# set path of directory
path = os.path.realpath(__file__)
dir = os.path.dirname(path)
# change the reference to the data folder
dir = dir.replace('pages', 'data')

st.header("MGP Table")

#st.set_page_config(page_title="Table Demo")
df = pd.read_csv(dir+"/uploaded_data.csv")
st.write(df)
