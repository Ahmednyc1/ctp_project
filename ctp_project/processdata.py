import cProfile
import pandas as pd
import numpy as np
# SEABORN IS A PLOTTING LIBRARY
import seaborn as sns
# MATPLOT LIB IS ALSO A PLOTTING LIBRARY
import matplotlib.pyplot as plt
import streamlit as st
from flask import Flask, render_template
import dash 
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import json
from datetime import datetime
import plotly.offline as pyo
import folium
import plotly.express as px
from folium.plugins import MarkerCluster
from statsmodels.api import qqplot
from dash import dash_table 
import dash_core_components as dcc
from dash import html 
from dash.dependencies import Input, Output
import plotly.offline as py 
import plotly.graph_objs as go
import json
df=pd.read_csv('MVC.csv')

def custom_aggregation(series):
    # Calculate the mode (most common factor)
    mode_factor = series.mode().iat[0] if len(series.mode()) > 0 else 'Unknown'
    
    # If the mode is "Unspecified," get the second most frequent value

    return mode_factor

# Assuming df is your original DataFrame
# Handle NaN values if necessary


# Group by 'ZIP CODE' and apply the custom aggregation function
zip_code_data = df.groupby('ZIP CODE')['CONTRIBUTING FACTOR VEHICLE 1'].agg(custom_aggregation).reset_index()
zip_code_data.to_csv('zip_code_data.csv', index=False, na_rep='Unknown', encoding='utf-8')

# Load GeoJSON file
