#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Load libraries and the dataset.
import pandas as pd
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
get_ipython().run_line_magic('matplotlib', 'inline')

import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode
import plotly.figure_factory as ff
from plotly import subplots
from plotly.subplots import make_subplots
init_notebook_mode(connected=True)

from datetime import date, datetime, timedelta
import time

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

from wordcloud import WordCloud
from collections import Counter

import os
for dirname, _, filenames in os.walk('input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

        
# Any results you write to the current directory are saved as output.

def resumetable(df):
    print(f"Dataset Shape: {df.shape}")
    summary = pd.DataFrame(df.dtypes, columns=['dtypes'])
    summary = summary.reset_index()
    summary['Name'] = summary['index']
    summary = summary[['Name','dtypes']]
    summary['Missing'] = df.isnull().sum().values    
    summary['Uniques'] = df.nunique().values

    return summary

df = pd.read_csv("/covid_19_data.csv",)

df.rename(columns={'Last Update': 'LastUpdate',
                   'ObservationDate':'Date',
                   'Country/Region': 'Country',
                   'Province/State': 'PS'},
         inplace=True)
df['Date'] = pd.to_datetime(df['Date']).dt.date

virus_cols=['Confirmed', 'Deaths', 'Recovered']

df = df[df[virus_cols].sum(axis=1)!=0]

df.loc[(df['PS'].isnull()) & (df.groupby('Country')['PS'].transform('nunique') == 0), 'PS'] =         df.loc[(df['PS'].isnull()) & (df.groupby('Country')['PS'].transform('nunique') == 0), 'Country'].to_numpy()

df['Country'] = np.where(df['Country']=='Mainland China', 'China', df['Country'])
df.dropna(inplace=True)

usecols=['Province/State', 'Country/Region', 'Lat', 'Long']
path= 'D:/Arman/Project/Corona/time_series_covid_19_'
csvs=['confirmed.csv', 'deaths.csv', 'recovered.csv']
coords_df = pd.concat([pd.read_csv(path + csv, usecols=usecols) for csv in csvs])
coords_df.rename(columns={'Country/Region': 'Country',
                          'Province/State': 'PS'}, 
                inplace=True)
coords_df['Country'] = np.where(coords_df['Country']=='Mainland china', 'China', coords_df['Country'])
coords_df = coords_df.drop_duplicates()
df = pd.merge(df, coords_df, on=['Country', 'PS'], how='left')

df = df.groupby(['PS', 'Country', 'Date']).agg({'Confirmed': 'sum',
                                                'Deaths': 'sum',
                                                'Recovered': 'sum',
                                                'Lat': 'max',
                                                'Long': 'max'}).reset_index()
df = df[df['Date']>date(2020,1,20)]


# In[6]:


dates = np.sort(df['Date'].unique())
data = [go.Scattergeo(
            locationmode='country names',
            lon = df.loc[df['Date']==dt, 'Long'],
            lat = df.loc[df['Date']==dt, 'Lat'],
            text = df.loc[df['Date']==dt, 'Country'] + ', ' + df.loc[df['Date']==dt, 'PS'] +   '-> Deaths: ' + df.loc[df['Date']==dt, 'Deaths'].astype(str) + ' Confirmed: ' + df.loc[df['Date']==dt,'Confirmed'].astype(str),
            mode = 'markers',
            marker = dict(
                size = (df.loc[df['Date']==dt,'Confirmed'])**(1/2.7)+3,
                opacity = 0.6,
                reversescale = True,
                autocolorscale = False,
                line = dict(
                    width=0.5,
                    color='rgba(0, 0, 0)'
                        ),
                #colorscale='rdgy', #'jet',rdylbu, 'oryel', 
                cmin=0,
                color=df.loc[df['Date']==dt,'Deaths'],
                cmax=df['Deaths'].max(),
                colorbar_title="Number of Deaths"
            )) 
        for dt in dates]


fig = go.Figure(
    data=data[0],
    layout=go.Layout(
        title = {'text': f'Corona Virus, {dates[0]}',
                                'y':0.98,
                                'x':0.5,
                                'xanchor': 'center',
                                'yanchor': 'top'},
        geo = dict(
            scope='world',
            projection_type='robinson',
            showland = True,
            landcolor = "rgb(252, 240, 220)",
            showcountries=True,
            showocean=True,
            oceancolor="rgb(219, 245, 255)",
            countrycolor = "rgb(128, 128, 128)",
            lakecolor ="rgb(219, 245, 255)",
            showrivers=True,
            showlakes=True,
            showcoastlines=True,
            countrywidth = 1,
            
            ),
     updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None])])]),
    
    frames=[go.Frame(data=dt, 
                     layout=go.Layout(
                          title={'text': f'Corona Virus, {date}',
                                'y':0.98,
                                'x':0.5,
                                'xanchor': 'center',
                                'yanchor': 'top'}
                           ))
            for dt,date in zip(data[1:],dates[1:])])

fig.show()


# In[7]:


china=df.loc[df['Country']=='China']
hubei=china.loc[china['PS']=='Hubei']
rest_of_china=china.loc[china['PS']!='Hubei'].groupby('Date').sum().reset_index()

china=china.groupby('Date').sum().reset_index()

agg_df=df.groupby(['Country', 'Date']).sum().reset_index()

rest_df=agg_df.loc[agg_df['Country']!='China'].groupby('Date').sum().reset_index()



dates = np.sort(df['Date'].unique())
dt_range = [np.min(dates)-timedelta(days=1), np.max(dates)+timedelta(days=1)]

# Row 1
frames_hubei = [go.Scatter(x=hubei['Date'],
                           y=hubei.loc[hubei['Date']<=dt, 'Confirmed'],
                           name='Hubei, Confirmed',
                           legendgroup="21") for dt in dates]

frames_rchina = [go.Scatter(x=rest_of_china['Date'],
                           y=rest_of_china.loc[rest_of_china['Date']<=dt, 'Confirmed'],
                           name='Rest of China, Confirmed',
                           legendgroup="21") for dt in dates]


frames_world = [go.Scatter(x=rest_df['Date'],
                           y=rest_df.loc[rest_df['Date']<=dt, 'Confirmed'],
                           name='Rest of the World, Confirmed',
                           legendgroup="22") for dt in dates]


# Row 2
frames_china_d = [go.Scatter(x=china['Date'],
                           y=china.loc[china['Date']<=dt, 'Deaths'],
                           name='China, Deaths',
                           legendgroup="31") for dt in dates]

frames_china_r = [go.Scatter(x=china['Date'],
                           y=china.loc[china['Date']<=dt, 'Recovered'],
                           name='China, Recovered',
                           legendgroup="31") for dt in dates]


frames_world_d = [go.Scatter(x=rest_df['Date'],
                           y=rest_df.loc[rest_df['Date']<=dt, 'Deaths'],
                           name='Rest of World, Deaths',
                           legendgroup="32") for dt in dates]

frames_world_r = [go.Scatter(x=rest_df['Date'],
                           y=rest_df.loc[rest_df['Date']<=dt, 'Recovered'],
                           name='Rest of World, Recovered',
                           legendgroup="32") for dt in dates]




fig = make_subplots(
    rows=2, cols=2,
    specs=[[{}, {}],
           [{}, {}]],
    subplot_titles=("China, Confirmed", 'Rest of the World, Confirmed',
                    "China, Deaths & Recovered", 'Rest of the World, Deaths & Recovered'))


# Row 1: Confirmed
fig.add_trace(frames_hubei[0], row=1, col=1)
fig.add_trace(frames_rchina[0], row=1, col=1)
fig.add_trace(frames_world[0], row=1,col=2)


# Row 2: Deaths & Recovered
fig.add_trace(frames_china_d[0], row=2, col=1)
fig.add_trace(frames_china_r[0], row=2, col=1)
fig.add_trace(frames_world_d[0], row=2,col=2)
fig.add_trace(frames_world_r[0], row=2,col=2)


# Add Layout
fig.update_xaxes(showgrid=False)

fig.update_layout(
        title={
            'text': 'Corona Virus: Confirmed, Deaths & Recovered',
            'y':0.98,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        height=820,
        legend_orientation="h",
        #legend=dict(x=1, y=0.4),
        xaxis1=dict(range=dt_range, autorange=False),
        yaxis1=dict(range=[-10, hubei['Confirmed'].max()*1.1 ], autorange=False),
        xaxis2=dict(range=dt_range, autorange=False),
        yaxis2=dict(range=[-10, rest_df['Confirmed'].max()*1.1 ], autorange=False),
        xaxis3=dict(range=dt_range, autorange=False),
        yaxis3=dict(range=[-10, np.max([china['Recovered'].max(), china['Deaths'].max()])*1.1 ], autorange=False),
        xaxis4=dict(range=dt_range, autorange=False),
        yaxis4=dict(range=[-0.5, np.max([rest_df['Recovered'].max(), rest_df['Deaths'].max()])*1.1], autorange=False),
        )


frames = [dict(
               name = str(dt),
               data = [frames_hubei[i], frames_rchina[i], frames_world[i],
                       frames_china_d[i], frames_china_r[i],
                       frames_world_d[i], frames_world_r[i]
                       ],
               traces=[0, 1, 2, 3, 4 ,5 ,6, 7]
              ) for i, dt in enumerate(dates)]



updatemenus = [dict(type='buttons',
                    buttons=[dict(label='Play',
                                  method='animate',
                                  args=[[str(dt) for dt in dates[1:]], 
                                         dict(frame=dict(duration=500, redraw=False), 
                                              transition=dict(duration=0),
                                              easing='linear',
                                              fromcurrent=True,
                                              mode='immediate'
                                                                 )])],
                    direction= 'left', 
                    pad=dict(r= 10, t=85), 
                    showactive =True, x= 0.6, y= -0.1, xanchor= 'right', yanchor= 'top')
            ]

sliders = [{'yanchor': 'top',
            'xanchor': 'left', 
            'currentvalue': {'font': {'size': 16}, 'prefix': 'Date: ', 'visible': True, 'xanchor': 'right'},
            'transition': {'duration': 500.0, 'easing': 'linear'},
            'pad': {'b': 10, 't': 50}, 
            'len': 0.9, 'x': 0.1, 'y': -0.2, 
            'steps': [{'args': [[str(dt)], {'frame': {'duration': 500.0, 'easing': 'linear', 'redraw': False},
                                      'transition': {'duration': 0, 'easing': 'linear'}}], 
                       'label': str(dt), 'method': 'animate'} for dt in dates     
                    ]}]



fig.update(frames=frames),
fig.update_layout(updatemenus=updatemenus,
                  sliders=sliders);
fig.show() 

