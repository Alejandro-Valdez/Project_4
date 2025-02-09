import pandas as pd
import streamlit as st
import time
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


# these are stateful variables which are preserved as Streamlit reruns this script
st.header("Comparing Data Among Multiple Vehicles")
vehicles_dt = pd.read_csv('/data/vehicles_us.csv') #assigns the vehicle dataset from Noteboooks to value 'vehicles_dt'
st.write(vehicles_dt.head())
# Making a histogram showing the information of how the transmission type of the vehicle 'corelates' to the days listed possibly showing what type of transmission is more or least desireable 

# Creating the information sets for the histogram to pull data from
p1 =vehicles_dt[vehicles_dt['transmission'] == 'automatic' ][ 'days_listed'] # Gathers data from the dataframe and pulls specifically the days listed from the cars the report to have 'automatic' transmission and assigns it
p2 = vehicles_dt[vehicles_dt['transmission'] == 'manual' ][ 'days_listed'] # Gathers data from the dataframe and pulls specifically the days listed from the cars the report to have 'manual' transmission and assigns it
p3 = vehicles_dt[vehicles_dt['transmission'] == 'other' ][ 'days_listed'] # Gathers data from the dataframe and pulls specifically the days listed from the cars the report to have 'other' transmission and assigns it


# Creating the histogram
fig = go.Figure()
fig.add_trace(go.Histogram(x=p1, name = 'Automatic')) # Assigning the data of 'Automatic' transmission to a specific traceable and toggable bars of one set color
fig.add_trace(go.Histogram(x=p2, name = 'Manual')) # Assigning the data of 'Manual' transmission to a specific traceable and toggable bars of one set color
fig.add_trace(go.Histogram(x=p3, name = 'Other'))# Assigning the data of 'Other' transmission to a specific traceable and toggable bars of one set color

# The two histograms are drawn on top of another


fig.update_layout(barmode='stack') # Updates the histogram to stack the bars on top of eachother
fig.update_layout(legend_title_text = "Transmission Type") # Updates the histogram legend to be titled 'Transmission Type'
fig.update_xaxes(title_text="Days Since Listed") # Updates the X Axis to be titled "Days Since Listed"
fig.update_yaxes(title_text="Amount") # Updates the Y axis to be title "Amount"
st.write(fig) # Displays the Chart
