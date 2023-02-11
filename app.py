import streamlit as st
import pandas as pd
import preprocessor,helper
import numpy as np

df = pd.read_csv('athlete_events.csv')
region = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df,region)
st.sidebar.title('Olympics Analysis')
user_menu = st.sidebar.radio(
    'Select as Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
)

# st.dataframe(df)

if user_menu == 'Medal Tally':
    st.sidebar.header('Medal Tally')
    years, country = helper.country_year_list(df)
    
    selected_year = st.sidebar.selectbox('Select Years',years)
    selected_country = st.sidebar.selectbox('Select Country',country)
    
    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    st.dataframe(medal_tally)

