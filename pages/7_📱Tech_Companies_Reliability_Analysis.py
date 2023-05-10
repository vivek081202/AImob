import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    layout="wide",
    page_title="Tech Companies Reliability Analysis | AImob",
    page_icon="Images/AI.png"
)

st.image('Images/buildings.png',width = 125)
st.title("Tech Companies Reliability Analysis")
# Load the dataset
# Upload CSV file
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # Display the dataset
    st.write("### Dataset:")
    st.write(df)

    # Calculate the reliability score for each company
    df['reliability_score'] = df['Reliability'] * df['Customer Satisfaction'] / 10

    # Display the reliability scores
    
    

    # Group the companies by industry
    industry_groups = df.groupby('Company')

    # Calculate the average reliability score for each industry
    industry_scores = industry_groups['reliability_score'].mean().sort_values(ascending=False)
    Customer_Satisfaction = industry_groups['Customer Satisfaction'].mean().sort_values(ascending=False)
    Brand_Reputation = industry_groups['Brand Reputation'].mean().sort_values(ascending=False)
    # Display the average reliability scores by industry
    Reliability_Scores, Industry_Scores = st.columns(2,gap="small")
    with Reliability_Scores:
        st.write("### Reliability Scores:")
        st.write(df[['Company', 'reliability_score']])
    with Industry_Scores:
        st.write("### Average Reliability Scores:")
        st.write(industry_scores)

    # Create a line chart of the average reliability scores by industry
    st.write("### Chart Analysis of Average Reliability Scores & other measures by Industry:")
    st.line_chart(industry_scores)
    CS, BR = st.columns(2,gap="medium")
    with CS:
        st.bar_chart(Customer_Satisfaction)
    with BR:
        st.bar_chart(Brand_Reputation)

    
    