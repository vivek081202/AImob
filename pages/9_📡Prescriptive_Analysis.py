import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

st.set_page_config(
    layout="wide",
    page_title="Prescriptive Analysis | AImob",
    page_icon="Images/AI.png"
)

st.image('Images/analysis.png',width = 125)
st.title('Prescriptive Data Analysis')
uploaded_file = st.file_uploader("**Upload CSV file**", type=["csv"])

# # Load the e-commerce dataset
# def load_data(file_path=None):
#     if file_path:
#         data = pd.read_csv(file_path)
#     else:
#         data = pd.read_csv('ecommerce_data.csv')
#     return data

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # Clean the data
    df.dropna(inplace=True)
    df['revenue'] = df['price'] * df['quantity']

    # Sidebar inputs
    st.sidebar.title('Prescriptive Analysis')
    product_category = st.sidebar.selectbox('Select product category', df['category'].unique())
    inventory_level = st.sidebar.slider('Select inventory level', 0, 100, 50)

    # Subset the data based on user input
    df_subset = df[(df['category'] == product_category) & (df['inventory'] < inventory_level)]

    # Linear regression model
    model = LinearRegression()
    X = df_subset[['inventory', 'price']]
    y = df_subset['revenue']
    model.fit(X, y)

    # Predicted revenue
    predicted_revenue = model.predict([[inventory_level, df_subset['price'].mean()]])

    # Display insights

    st.subheader('Selected Product Category: ' + product_category)
    st.subheader('Selected Inventory Level: ' + str(inventory_level))
    with st.info('This is an informational message'):
        st.write('Predicted revenue with current inventory level and average price: $', predicted_revenue[0])
    
    #st.write('Predicted revenue with current inventory level and average price: $', predicted_revenue[0])

    # Visualizations
    st.subheader('Inventory vs Revenue')
    fig, ax = plt.subplots()
    sns.scatterplot(data=df_subset, x='inventory', y='revenue', ax=ax)
    sns.lineplot(x=df_subset['inventory'], y=model.predict(X), ax=ax)
    st.pyplot(fig)

    st.subheader('Inventory Distribution')
    inventory_hist = np.histogram(df['inventory'], bins=20)
    st.bar_chart(inventory_hist[0])

    st.subheader('Revenue by Category')
    cat_revenue = df.groupby('category')['revenue'].sum()
    st.bar_chart(cat_revenue)

    st.subheader('Top 10 Products by Revenue')
    top_products = df.groupby('product')['revenue'].sum().sort_values(ascending=False)[:10]
    st.bar_chart(top_products)

    st.subheader('Price vs Revenue')
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='price', y='revenue', ax=ax)
    st.pyplot(fig)


