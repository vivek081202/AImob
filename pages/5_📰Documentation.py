import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    layout="wide",
    page_title="Documentation | AImob",
    page_icon="Images/AI.png"
    )

with st.sidebar:
    selected = option_menu(
        menu_title= "AImob",
        options=["Documentation"],
        icons=["file"],
        default_index=0,
        orientation= "vertical",
        menu_icon="cast",
        styles={
        "icon": {"font-size": "17px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"3px", "--hover-color": "#262730"}
    }
    )
    if selected =="Documentation":
        st.title(f"About AImob")
        st.write(
            """
  *AImob* is web based tool which facilitates integrated AI tools for sentiment analysis & report generation.\n
  **AImob** is extremely useful web application integrated & combined report generation & sentiment analysis on e – commerce products & services as it allows us to gain an overview of the wider public opinion behind certain trends & tastes. AI Tools like public opinion analytics, statistical graph-based report generation & trend analysis make analytics process quicker and easier than ever before, thanks to real-time monitoring capabilities. 
    """
        )
            
    st.write("\n\n")

st.image('Images/folder.png',width = 125)
st.title("""
AImob Documentation
""")

st.header("""
    About - AImob Modules & User Guide
""")

st.subheader("""
    1. Report Generation Module 📚
""")
st.write("""
The report generation module allows you to directly extract all the information you want from the open formats (CSV, .xsls etc) and either view it directly online or export it in analytical visuals.
""")
st.write("""
This module supports **.csv, .xlsx & .excel** files which converts it into data visualisation models using advanced display elments.
\n
Report Generation modules process only numeric values like integer, real & float data, Unless data **(i.e Strings, characters will not be processed)** & may throw an exception of **utf - 8 conversion** and else.
\n
**Efficient & Enhanced code to catogerise file formats is below:**
""")
file_code = '''
import streamlit as st
from streamlit_option_menu import option_menu
import os

if uploaded_file:
   split_tup = os.path.splitext(uploaded_file.name)
   file_extension = split_tup[1]
   extension = file_extension.replace('.','')

if Generate_Report and uploaded_file is not None:
    if extension == 'xlsx' or extension == 'excel':
        # Code Writen for if file extensions are xlsx or excel
    elif extension == 'csv':    
        # Code Writen for if file extension is csv
'''
st.code(file_code,language='python')
st.write('\n')
st.write("""
**Tutorial to generate reports:**
""")
st.video("Videos/Report.webm")

st.write("\n\n\n")
st.subheader("""
    2. Product Feasibility Analyser 📉
""")

st.write('\n')
st.write("""
**Tutorial to Product reviews & feasibility**
""")
st.video("Videos/FRD.webm")

st.write("\n\n\n")
st.subheader("""
    3. Aspect Based Analyzer (AImob analysis tool)) 📉
""")

st.write('\n')
st.write("""
**Tutorial to Aspect Based Analysis**
""")
st.video("Videos/ABA.webm")

st.write("\n\n\n")
st.subheader("""
    4. Keyword Extractor (AImob analysis tool)) 📉
""")

st.write('\n')
st.write("""
**Tutorial to Keyword Extraction**
""")
st.video("Videos/KE.webm")

st.write("\n\n\n")
st.subheader("""
    5. Youtube Comments Extractor (AImob analysis tool)) 📉
""")

st.write('\n')
st.write("""
**Tutorial to Youtube Comments Extraction**
""")
st.video("Videos/YCE.webm")