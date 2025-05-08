import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

st.set_page_config(
    page_title="SafeSpace Risk Dashboard",
    layout="wide",
)

st.title("🏠 Welcome to SafeSpace")

st.markdown("""
Welcome to the SafeSpace Financial Risk Dashboard!  
Use the sidebar to explore:
- 📊 Investment Simulator
            A quick and easy way to make a stock portfolio and assertain the risk associated with the stocks chosen in the portfolio.
- 🤲 Loan Risk Assessment
            A loan calculator to determine your loan risk.
""")

# import streamlit as st

# # App Config
# st.set_page_config(page_title="SafeSpace Risk Dashboard", layout="wide")

# # Define the pages
# main_page = st.Page("investment_simulator.py", title="Investment Simulator", icon="📊")
# page_2 = st.Page("loan_assessment.py", title="Loan Risk Assessment", icon="🤲")

# # Set up navigation
# pg = st.navigation([main_page, page_2, page_3])

# # Run the selected page
# pg.run()
