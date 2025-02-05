import pandas as pd
import streamlit as st
import time
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


# these are stateful variables which are preserved as Streamlit reruns this script
st.header("Comparing Data Among Multiple Vehicles")
vehicles_dt = pd.read_csv('./data/vehicles_us.csv') #assigns the vehicle dataset from Noteboooks to value 'vehicles_dt'
st.write(vehicles_dt.head())
