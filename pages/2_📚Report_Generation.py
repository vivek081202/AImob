import streamlit as st
import pandas as pd
import os
from streamlit_option_menu import option_menu

st.set_page_config(
    layout="wide",
    page_title="Report Generation | AImob",
    page_icon="Images/AI.png"
    )

with st.sidebar:
    st.write('**AImob** Navigation')
    selected = option_menu(
        menu_title= "AImob",
        options=["Report Generation"],
        icons=["book"],
        default_index=0,
        orientation= "vertical",
        menu_icon="cast",
        styles={
        "icon": {"font-size": "17px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"3px", "--hover-color": "#262730"}
    }
    )
    if selected =="Report Generation":
        st.title(f"About AImob")
        st.write(
            """
  **Report Generation Module** of AImob allows you to generate reports or reporting dashboards that your team and clients can edit and cross-collaborate on.\n
  Module required structured data in columns and rows to generate text. To pull HubSpot and Google Analytics data into spreadsheets.
    """
        )
st.write("\n\n")
st.image("Images/report.png",width = 125)
st.title("""
AImob - Report Generation System
""")
st.write("\n\n")
uploaded_file = st.file_uploader("Choose a file",type = ['csv','excel','xlsx'])
st.write("\n\n\n\n")
if uploaded_file is not None:
    st.success('Your File Uploaded Successfully.', icon="✅")

Generate_Report = st.button("Generate Report")

if uploaded_file:
   split_tup = os.path.splitext(uploaded_file.name)
   file_extension = split_tup[1]
   extension = file_extension.replace('.','')

if Generate_Report and uploaded_file is not None:

    if extension == 'xlsx' or extension == 'excel':
        df = pd.read_excel(uploaded_file,
                        sheet_name = 'Data',
                        usecols = 'A:K',
                        header = 0)
        chart = pd.read_excel(uploaded_file,
                        sheet_name = 'Data',
                        usecols = 'J:K',
                        header = 0)
        st.write('\n\n\n')                    
        st.write("""
        # **Data Frames**
        """)                    
        st.dataframe(df)
        st.write('\n\n')
        st.write("""
        # **Chart Based Analysis**
        """) 

        st.write("\n\n\n")
        st.write("**Bar Chart**")
        st.bar_chart(chart)

        st.write('\n\n\n')
        st.write('**Line Chart**')
        st.line_chart(chart)
        st.write('\n\n\n')
        st.write('**Area Chart**')
        st.area_chart(chart)
    elif extension == 'csv':
        df = pd.read_csv(uploaded_file,header=0)
        st.write('\n\n\n')
        st.write("""
        # **Data Frames**
        """)
        st.dataframe(df)
        st.write('\n\n')
        st.write("""
        # **Chart Based Analysis**
        """) 

        st.write("\n\n\n")
        st.write("**Bar Chart**")
        st.bar_chart(df)

        st.write('\n\n\n')
        st.write('**Line Chart**')
        st.line_chart(df)
        
        st.write('\n\n\n')
        st.write('**Area Chart**')
        st.area_chart(df)

