import streamlit as st
#import RAKE
from streamlit_option_menu import option_menu
from textblob import TextBlob
import pandas as pd
import googleapiclient.discovery
from streamlit_player import st_player
#import os
st.set_page_config(
    layout="wide",
    page_title="Analysis Tools | AImob",
    page_icon="Images/AI.png"
    )

with st.sidebar:
    selected = option_menu(
        menu_title= "AImob",
        options=["Analysis Tools"],
        icons=["tools"],
        default_index = 0,
        orientation= "vertical",
        menu_icon="cast",
        styles={
        "icon": {"font-size": "17px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"3px", "--hover-color": "#262730"}
    }
    )
    if selected =="Analysis Tools":
        st.title(f"About Analysis Tools")
        st.write(
            """
  **AI analytics** is the product of automating data analysis—a traditionally time-consuming and people-intensive task—using the power of today's artificial intelligence and machine learning technologies.\n

  **AImob** Facilitates with 3 Analysis Tools:\n
  🧰 Aspect Based Analysis\n
  🧰 Keywords Extractor\n
  🧰 Youtube comments Extractor

    """
        )
        st.write("\n\n")

st.image('Images/seo.png',width = 125)
st.title("""
AImob Analysis Tools
""")
st.subheader("1. Aspect Based Analysis")
txt = st.text_area('Text to analyze',placeholder="Enter Sentences to analyse text.")
st.write('\n\n')


text_sentiments = st.button('Analyze my Sentiments')
feedback = TextBlob(txt)
polar_v = feedback.sentiment.polarity


if text_sentiments:
    if 0 < polar_v <= 1:
        st.success("Great Positive Sentiments !!!", icon = "✅")
        st.balloons()
    elif polar_v < 0:
        st.error("Negative Sentiments",icon = "🚨")
    elif polar_v == 0:
        st.warning("Neutral or NO Sentiments !!!", icon="⚠️")

st.write('\n\n\n')
st.subheader("2. Keywords Finder")
key_sentence = st.text_area('Keyword Extractor',placeholder="Enter Sentences to find keyword.")
extract = st.button("Extract Keywors")
clear = st.button("Clear")
if extract:
    stop_dir = "pages\SmartStoplist.txt"
    rake_object = RAKE.Rake(stop_dir)
    keywords = rake_object.run(key_sentence)
    st.write(keywords)
if clear:
    key_sentence = " "


st.write('\n\n\n')
st.subheader("3. Youtube Comments Extractor (Data Set Generation)")
# st.success("""
# 💻 Tool is Under Development !
# # 🎯 Comming Soon
# """)


API_KEY = "AIzaSyD11w3w-K21PPZ7Cgus_NbAQfeluN2K9vQ"

API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

youtubelink = st.text_input("Enter Youtube video URL",placeholder="Enter link")
VIDEO_ID = youtubelink.replace('https://www.youtube.com/watch?v=','')
youtube = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, developerKey = API_KEY)
Download_comments  = st.button("Extract Comments")

if Download_comments:
    request = youtube.commentThreads().list(part="snippet,replies",videoId=VIDEO_ID,maxResults=100)
    response = request.execute()

    df = pd.json_normalize(response['items'])
    df.columns = df.columns.str.removeprefix('snippet.topLevelComment.').str.removeprefix('snippet.').str.removesuffix('.value').str.removesuffix('.comments')
    df.to_csv(f'comments-{VIDEO_ID}.csv', index=False)
    st_player(youtubelink)
    st.success("Comments extracted & saved in a csv file.")

