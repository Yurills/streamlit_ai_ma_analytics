import streamlit as st
from dotenv import load_dotenv

load_dotenv()


st.set_page_config(
    page_title="AI-Powered Company Financial Dashboard", 
    layout="wide")



st.title("📊 Data Dashboard")

st.markdown(
    """
    ## Welcome to the AI-Powered Company Financial Dashboard!
    **👈 Select workflows from the sidebar** to see some examples
    ### What our AI can currently do:
    - **AI Analysis**: Get insights and PDFs report from comparing two companies
    - **AI Chart Visualization**: Visualize both companies' performance
"""
)
