import streamlit as st
import pandas as pd
import numpy as np
import plotly as px
import plotly.figure_factory as ff
from bokeh.plotting import figure
import matplotlib.pyplot as plt

st.title('Police Incident Reports from 2018 to 2020 in San Francisco')

df = pd.read_csv("Police_Department_Incident_Reports__2018_to_Present.csv")

st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')

mapa = pd.DataFrame()
mapa['Date'] = df['Incident Date']
mapa['Day'] = df['Incident Day of Week']
mapa['Year'] = df['Incident Year']
mapa['Police District'] = df['Police District']
mapa['Neighborhood'] = df['Analysis Neighborhood']
mapa['Incident Category'] = df['Incident Category']
mapa['Incident Subcategory'] = df['Incident Subcategory']
mapa['Incident Description'] = df['Incident Description']
mapa['Resolution'] = df['Resolution']
mapa['lat'] = df['Latitude']
mapa['lon'] = df['Longitude']
mapa['Report Type'] = df['Report Type Description']
mapa = mapa.dropna()

subset_data2 = mapa
report_type_input = st.sidebar.multiselect(
'Report Type',
mapa.groupby('Report Type').count().reset_index()['Report Type'].tolist())
if len(report_type_input) > 0:
    subset_data2 = mapa[mapa['Report Type'].isin(report_type_input)]

subset_data1 = subset_data2
neighborhood_input = st.sidebar.multiselect(
'Neighborhood',
subset_data2.groupby('Neighborhood').count().reset_index()['Neighborhood'].tolist())
if len(neighborhood_input) > 0:
    subset_data1 = subset_data2[subset_data2['Neighborhood'].isin(neighborhood_input)]

subset_data = subset_data1
incident_input = st.sidebar.multiselect(
'Incident Category',
subset_data1.groupby('Incident Category').count().reset_index()['Incident Category'].tolist())
if len(incident_input) > 0:
    subset_data = subset_data1[subset_data1['Incident Category'].isin(incident_input)]
            
subset_data
  
st.markdown('It is important to mention that any police district can answer to any incident, the neighborhood in which it happened is not related to the police district.')

st.markdown('Crime locations in San Francisco')
st.map(subset_data)

st.markdown('Crimes ocurred per police district')
st.line_chart(subset_data['Police District'].value_counts())

st.markdown('Crimes ocurred per day of the week')
st.bar_chart(subset_data['Day'].value_counts())

st.markdown('Type of crimes committed')
st.line_chart(subset_data['Incident Category'].value_counts())

st.markdown('Resolution Satus')
st.line_chart(subset_data['Resolution'].value_counts())

agree = st.button('Click to see Incident Description')
if agree:
    st.markdown('Description of crimes committed')
    st.bar_chart(subset_data['Incident Description'].value_counts())
    
agree2 = st.button('Click to see Incident Date')
if agree2:
    st.markdown('Crimes committed Date')
    st.line_chart(subset_data['Date'].value_counts())

st.markdown('Incident Year')
fig1, ax1 = plt.subplots()
labels = subset_data['Year'].unique()
ax1.pie(subset_data['Year'].value_counts(), labels=labels, autopct='%1.1f%%', startangle=20)
st.pyplot(fig1)