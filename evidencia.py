# -*- coding: utf-8 -*-
"""Evidencia.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pWV_K5Rf4UHoUGxUYrAGMfLq-ZklElm5
"""

import streamlit as st
import pandas as pd


st.title('Police Incident Reports from 2018 to 2020 in San Francisco')

df = pd.read_csv("Police_Department_Incident_Reports__2018_to_Present.csv")

st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')

mapa = pd.DataFrame()
mapa['Date'] = df['Incident Date']
mapa['Day'] = df['Incident Day of Week']
mapa['Police district'] = df['Police District']
mapa['Analysis neighborhood'] = df['Analysis Neighborhood']
mapa['Incident category'] = df['Incident Category']
mapa['Incident subcategory'] = df['Incident Subcategory']
mapa['Resolution'] = df['Resolution']
mapa['Latitude'] = df['Latitude']
mapa['Longitude'] = df['Longitude']
mapa = mapa.dropna()