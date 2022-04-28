import streamlit as st
import pandas as pd
import numpy as np

#title
st.title('Tweet Sentiment Analysis')
#markdown
st.markdown('This application is all about tweet sentiment analysis of airlines. We can analyse reviews of the passengers using this streamlit app.')
#sidebar
st.sidebar.title('Sentiment analysis of airlines')
# sidebar markdown 
st.sidebar.markdown("🛫We can analyse passengers review from this application.🛫")
#loading the data (the csv file is in the same folder)
#if the file is stored the copy the path and paste in read_csv method.
data=pd.read_csv('Hackathon 2/external_labelled_tweets_cleaned.csv')
#checkbox to show data 
if st.checkbox("Show Data"):
    st.write(data.head(50))
#subheader
st.sidebar.subheader('Tweets Analyser')
#radio buttons
tweets=st.sidebar.radio('Sentiment Type',('positive','negative','neutral'))
st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])
st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])
st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])
#selectbox + visualisation
# An optional string to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content.
## Multiple widgets of the same type may not share the same key.
