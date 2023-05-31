import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import pickle

categorical_features = ['BoosterVersion',	'Orbit',	'LaunchSite',	'Outcome',	'Flights',	'GridFins',	'Reused',	'Legs',	'LandingPad', 'Serial']
numerical_features = ['Block',	'ReusedCount']
with st.container():
    dict1= {}
    for i in categorical_features:
        inp=st.write(input(f'Enter the {i}: '))
        dict1[i] = inp
    #print(dict1)
    df2= pd.DataFrame(dict1, index=[0])