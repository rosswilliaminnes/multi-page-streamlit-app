# importing os module
import os
  
  
# gives the path of demo.py
path = os.path.realpath(__file__)
print(path)
dir = os.path.dirname(path)
print(dir)

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly_express as px
import os 


path = os.path.realpath(__file__)
dir = os.path.dirname(path)

# read csv into a dataframe
df = pd.read_csv(dir+"/data/uploaded_data.csv")

#print(df.head())

print(df.head())