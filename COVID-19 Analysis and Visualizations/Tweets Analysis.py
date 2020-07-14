#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Load libraries and the dataset.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from wordcloud import WordCloud
from collections import Counter

df_tweets = pd.read_csv("/tweets.csv", index_col=0)
df_tweets.rename(columns={'txt': 'tweets',
                         'dt':'date'}, inplace=True)

import re
def tweet_parser(text, pattern_regex):
    
    for pr in pattern_regex:
        text = re.sub(pr, ' ', text)
        
    return text.strip()

pattern_regex = ['\n', '\t', ':', ',', ';', '\.', '"', "''", 
                 '@.*?\s+', 'RT.*?\s+', 'http.*?\s+', 'https.*?\s+']

df_tweets['tidy_tweets'] = df_tweets.apply(lambda r: tweet_parser(r['tweets'], pattern_regex), axis=1)
df_tweets['date'] = pd.to_datetime(df_tweets['date']).dt.date

df_tweets['sentiment'] = df_tweets.apply(lambda r: TextBlob(r['tidy_tweets']).sentiment.polarity, axis=1)
df_tweets['sent_adj'] = np.where(df_tweets['sentiment']<0, 'Negative', np.where(df_tweets['sentiment']>0, 'Positive', 'Neutral'))
df_tweets['sent_adj'] = df_tweets['sent_adj'].astype('category')
sizes = df_tweets.groupby('sent_adj').size()

def render_wordcloud(df, sent='Positive'):
    
    color = {'Positive': 'Set2', 'Negative': 'RdGy', 'Neutral': 'Accent_r'}
    
    words = ' '.join([text for text in df.loc[df['sent_adj']==sent, 'tidy_tweets']])
    
    wordcloud = WordCloud(width=800, height=500, 
                          background_color='black',
                          max_font_size=100, 
                          relative_scaling=0.1, 
                          colormap=color[sent]).generate(words)

    plt.figure(figsize=(14, 10))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.title(sent + ' Wordcloud', fontsize=20)
    plt.axis('off')
    plt.show()
    
for s in ['Positive', 'Negative', 'Neutral']:
    render_wordcloud(df_tweets, s)

