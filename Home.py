import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly_express as px
import os 

# set path of directory
path = os.path.realpath(__file__)
dir = os.path.dirname(path)

st.set_page_config(
    page_title="Simple Multi Page App Example"
)



st.title("Simple Multi Page App Example")
st.subheader("Using the MPG dataset")

#st.sidebar.title('Navigation')
st.sidebar.success("Select Page Above")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.to_csv(dir+"/data/uploaded_data.csv")