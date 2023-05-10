# import python libraries
import streamlit as st
import numpy as np
#import mysql.connector
from streamlit_option_menu import option_menu

# set page configurations
st.set_page_config(
    layout="wide",
    page_title="Home | AImob",
    page_icon="Images/AI.png"
    )

with st.sidebar:
    selected = option_menu(
        menu_title= "AImob",
        options=["Home","Contact","Signup","Login"],
        icons=["house","envelope","door-open","key"],
        default_index=0,
        orientation= "vertical",
        menu_icon="cast",
        styles={
        "icon": {"font-size": "17px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"3px", "--hover-color": "#262730"}
    }
    )
    if selected =="Home":
        st.title(f"About AImob")
        st.write(
            """
  *AImob* is web based tool which facilitates integrated AI tools for sentiment analysis & report generation.\n
  **AImob** is extremely useful web application integrated & combined report generation & sentiment analysis on e – commerce products & services as it allows us to gain an overview of the wider public opinion behind certain trends & tastes. AI Tools like public opinion analytics, statistical graph-based report generation & trend analysis make analytics process quicker and easier than ever before, thanks to real-time monitoring capabilities. 
    """
        )
    if selected =="Analysis Tools":
        st.title(f"You have selected {selected}")
    if selected =="Documentation":
        st.title(f"You have selected {selected}")
    if selected =="Contact":
        st.write("\n\n")
        st.write("""
            # Contact Us   """)
        with st.form("Contact"):
            CName = st.text_input('Name',placeholder='Enter Name')
            CPhone = st.text_input('Mobile',placeholder='Enter Mobile')
            CEmail = st.text_input('Email',placeholder='Enter Email')
            CMessage = st.text_area('Message',placeholder='Enter Your Message Here...')
            st.write("\n\n")
            Contact_submit = st.form_submit_button('Submit')
        st.write("\n\n")    
    if selected =="Signup":
        st.write("\n\n")
        st.write("""
        # Hello 👋, Sign Up Here    """)
        with st.form("Registeration"):
            def init_connection():
                return mysql.connector.connect(**st.secrets["mysql"])

            conn = init_connection()
            RName = st.text_input('Name',placeholder='Enter Name')
            RPhone = st.text_input('Mobile',placeholder='Enter Mobile')
            REmail = st.text_input('Email',placeholder='Enter Email')
            RPassword = st.text_input('Password',placeholder='Enter Password',type="password")
            st.write("\n\n")
            Signup = st.form_submit_button('Register Me')
            if Signup:
                cursor = conn.cursor()
                sql = f"""INSERT INTO register(
                Fname,Phone,Email,Pass)
                VALUES ('{RName}', '{RPhone}','{REmail}','{RPassword}')"""
                cursor.execute(sql)
                conn.commit()
                st.success("Congratulations! You are part of AImob", icon = "✅")

    if selected =="Login":
        st.write("\n\n")
        st.write("""
        # Hello 👋, Login Here    """)
        
        with st.form("Registeration"):
            def init_connection():
                return mysql.connector.connect(**st.secrets["mysql"])
            
            conn = init_connection()
            REmail = st.text_input('Email',placeholder='Enter Email')
            RPassword = st.text_input('Password',placeholder='Enter Password',type="password")
            st.write("\n\n")
            Login = st.form_submit_button('Login')
            
            if Login:
                cursor = conn.cursor()
                sql = f"""SELECT * from register
                where Email = '{REmail}' and Pass = '{RPassword}';"""
                cursor.execute(sql)
                cursor.fetchall()
                result = cursor.rowcount
                if result == 1:
                    st.success("Welcome! Loggined Successfully", icon = "✅")
                else:
                    st.error("OOPS!!! Invalid ID or Password", icon = "🚨")
        st.write("\n\n")

st.image('Images/AIlogo.png',width = 250)
st.write("""
# Analyse Your Next with **AI**mob
""")

st.image("Images/AI.jpg",caption='AImob - Sentiment Analyzer')
st.write(
    """
  *AImob* is web based tool which facilitates integrated AI tools for sentiment analysis & report generation.\n
  **AImob** is extremely useful web application integrated & combined report generation & sentiment analysis on e – commerce products & services as it allows us to gain an overview of the wider public opinion behind certain trends & tastes. AI Tools like public opinion analytics, statistical graph-based report generation & trend analysis make analytics process quicker and easier than ever before, thanks to real-time monitoring capabilities. 
    """
)        
st.write("\n")
st.write('''
# AImob Applications
''')

# Columns
Report, Trending, Aspect, Feasibility = st.columns(4,gap="medium")

with Report:
   st.header("Report GEN System")
   st.image("Images/1Report.jpg")
   st.write("The report generation module allows you to directly extract all the information you want from the open formats (CSV, .xsls etc) and either view it directly online or export it in analytical visuals.")
   Report_G = st.button('More on Report generation')

with Trending:
   st.header("Trending Analysis")
   st.image("Images/2Trend.jpg")
   st.write("Trend analysis is a technique used in technical analysis that attempts to predict future stock price movements based on recently observed trend data.")
   Trend_A = st.button('More on Trends Analysis')

with Aspect:
   st.header("Aspect-Based Analysis")
   st.image("Images/3Text.jpg")
   st.write("Aspect-based sentiment analysis (ABSA) is a text analysis technique that categorizes data by aspect and identifies the sentiment attributed to each one.")
   Aspect_A = st.button('More on Aspect Analysis')

with Feasibility:
   st.header("Feasibility Predicter")
   st.image("Images/4Feasibility.jpg")
   st.write("Product Feasibility Predictor is a market research methodology that aims to provide predictive analytics to guide the next steps for marketing, sales, and product development.")
   Feasibility_A = st.button('More on Feasibility Analysis')


#functions
if Report_G:
    st.success("Welcome to Report Generation Module of AImob")
    st.open("Report_generation.py")


st.write("\n")
st.write('''
# Data Analysis Visuals by AImob
''')


chart, text = st.columns([3,1],gap='medium')
chart1, text1 = st.columns([3,1],gap='medium')
chart2, text2 = st.columns([3,1],gap='medium')
chart3, text3 = st.columns([2,2],gap='medium')
data = np.random.randn(15, 4)

chart.subheader("Data Visulas for analysis of time periods (line graphs)")
chart.line_chart(data)
text.subheader('About')
text.write('It is used to show information that changes over time. Line charts are created by plotting a series of several points and connecting them with a straight line. Line charts are used to track changes over short and long periods.')
text.button('Explore...')

st.write("\n")
chart1.subheader("Data Visulas for Financial Instruments (Bar Charts)")
chart1.bar_chart(data)
text1.subheader('About')
text1.write('It visually depicts the open, high, low, and close prices of an asset or security over a specified period of time. The vertical line on a price bar represents the high and low prices for the period. The left and right horizontal lines on each price bar represent the open and closing prices.')
text1.button('Explore..')

st.write("\n")
chart2.subheader("Data Visulas for analytics in quantities (Area Charts)")
chart2.area_chart(data)
text2.subheader('About')
text2.write('It combines a line chart and a bar chart to show changes in quantities over time. Its similar to a line graph in that data points are plotted and connected by line segments. However, the area below the line is colored in or shaded.')
text2.button('Explore.')

st.write("\n")
chart3.subheader("Convert your data into API")
chart3.json({
    'Name': 'Vivek Kumar Singh',
    'Course': 'BCA (Computer Science)',
    'Favourite Subjects': [
        'Operating Systems',
        'Data Structures & Algorithms',
        'Python',
        'DBMS',
        'Java',
        'Data Science'
    ],
    'About' : 'I am a good backend developer 👩‍💻',
    'More' : 'stuffs can be added...'
})
text3.subheader('About')
text3.write('JSON is universally excellent because it provides a super friendly format for human-readers and super friendly for non-JavaScript machine-readers. It is both human and machine friendly, as compared to XML and other types of accomplishing the same thing.')
text3.button('Explore')









