#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter("ignore")

import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_dark"
from plotly.subplots import make_subplots
import seaborn as sns


from sklearn.model_selection import RandomizedSearchCV , train_test_split
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import datetime
plt.style.use('seaborn')
import math
import random
import time
import operator
covid19 = pd.read_csv('/covid_19.csv')
covid19['ObservationDate']=pd.to_datetime(covid19['ObservationDate'])
covid19['Last Update']=pd.to_datetime(covid19['Last Update'])
grouped = covid19.groupby('ObservationDate')['Last Update', 'Confirmed', 'Deaths'].sum().reset_index()



fig = px.line(grouped, x="ObservationDate", y="Confirmed", 
              title="Worldwide Confirmed Cases Over Time")
fig.show()

fig = px.line(grouped, x="ObservationDate", y="Confirmed", 
              title="Worldwide Confirmed Cases (Logarithmic Scale) Over Time", 
              log_y=True)
fig.show()


# In[3]:


fig = px.line(grouped, x="ObservationDate", y="Deaths", title="Worldwide Deaths Over Time",
             color_discrete_sequence=['#F42272'])
fig.show()

fig = px.line(grouped, x="ObservationDate", y="Deaths", title="Worldwide Deaths (Logarithmic Scale) Over Time", 
              log_y=True, color_discrete_sequence=['#F42272'])
fig.show()

