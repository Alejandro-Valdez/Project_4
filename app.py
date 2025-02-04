import pandas as pd
import streamlit as st
import time
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


# these are stateful variables which are preserved as Streamlit reruns this script
st.header("Comparing Data Among Multiple Vehicles", divider="gray")
