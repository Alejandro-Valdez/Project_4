import pandas as pd
import streamlit as st
import time
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


# these are stateful variables which are preserved as Streamlit reruns this script
st.header("Comparing Data Among Multiple Vehicles")

vehicles_dt = pd.read_csv('./data/vehicles_us.csv') #assigns the vehicle dataset from Noteboooks to value 'vehicles_dt'
vehicles_dt['brand'] = vehicles_dt['model'].str.split().str[0]
vehicles_dt.head()git 
st.write(vehicles_dt.head()) #displays the first five lines of the 'vehicles_dt' dataframe
# Making a histogram showing the information of how the transmission type of the vehicle 'corelates' to the days listed possibly showing what type of transmission is more or least desireable 

st.title("Days Since Car Was Listed VS the Transmission Type of the Car")

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

st.title('Cars Price in Comparison to its Odometer Reading by Brand')
check = st.checkbox('Toggle line for graph')
st.write('State of the check box:', check)

fig_sc = px.scatter(vehicles_dt, x="price", y="odometer", color="brand",
                  hover_data=['cylinders'])
fig_sc.update_layout(legend_title_text = "Brand") # Updates the histogram legend to be titled 'Transmission Type'
fig_sc.update_xaxes(title_text=" Price") # Updates the X Axis to be titled "Days Since Listed"
fig_sc.update_yaxes(title_text=" Odomoter") # Updates the Y axis to be title "Amount"
if check:
    fig_sc.add_trace(
    go.Scatter(
        x=[0, 200000],
        y=[0, 100000000],
        mode="lines",
        line=go.scatter.Line(color="gray"),
        showlegend=False)
)

st.write(fig_sc)

