import streamlit as st
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob

st.set_page_config(
    layout="wide",
    page_title="Youtube Comments Analysis | AImob",
    page_icon="Images/AI.png"
)

# Define a function to clean the comments and perform sentiment analysis
def analyze_comments(comments):
    # Clean the comments by removing non-alphabetic characters and converting to lowercase
    comments = [comment.lower().replace('\n', ' ') for comment in comments]
    comments = [''.join(filter(str.isalpha, comment)) for comment in comments]

    # Analyze the sentiment of each comment using TextBlob
    sentiments = [TextBlob(comment).sentiment.polarity for comment in comments]

    # Count the number of positive, negative, and neutral comments
    pos_count = sum([1 for sentiment in sentiments if sentiment > 0])
    neg_count = sum([1 for sentiment in sentiments if sentiment < 0])
    neu_count = sum([1 for sentiment in sentiments if sentiment == 0])

    # Create a word cloud of the most common words in the comments
    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=STOPWORDS,
                          min_font_size=10).generate(' '.join(comments))

    return pos_count, neg_count, neu_count, wordcloud

# Set up the Streamlit app
st.image('Images/youtube.png',width = 125)
st.title('YouTube Comments Analysis')
st.write('**Upload a CSV file containing YouTube comments below:**')
csv_file = st.file_uploader('CSV File', type='csv')

# If the user has uploaded a file, process the comments and display the results
if csv_file is not None:
    st.write('Loading comments...')
    comments_df = pd.read_csv(csv_file)
    comments = comments_df['Text Original'].tolist()
    st.write(f'Analyzing {len(comments)} comments...')
    pos_count, neg_count, neu_count, wordcloud = analyze_comments(comments)
    st.write(f'Positive comments: {pos_count}')
    st.write(f'Negative comments: {neg_count}')
    st.write(f'Neutral comments: {neu_count}')
    st.write('Word cloud:')
    st.image(wordcloud.to_array())
    st.write("\n\n")
    st.header("Chart Analysis of Reviews")
    datalc = pd.DataFrame({
    'Positive Reviews': [pos_count],
    'Negative Reviews': [neg_count],
    'Neutral Reviews': [neu_count]
    })
    area, bar = st.columns(2,gap="medium")
    with area:
        st.header('Area Chart Analysis')
        st.area_chart(datalc)
    with bar:
        st.header('Bar Chart Analysis')
        st.bar_chart(datalc)
    #st.line_chart(pd.DataFrame(data=datalc))
