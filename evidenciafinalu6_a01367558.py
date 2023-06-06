import streamlit as st
import pandas as pd


st.title('Police Incident Reports from 2018 to 2020 in San Francisco')

df = pd.read_csv("https://drive.google.com/drive/u/0/folders/1Hd2HOFknGccrm11VSdDp5N9-ADkboWvZ")

st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')

mapa = pd.DataFrame()
mapa['lat'] = df['Latitude']
mapa['lon'] = df['Longitude']
mapa = mapa.dropna()
