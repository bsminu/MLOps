import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd


st.title('Airbnb Project Demo')

st.write("Let us have a glimpse of our first dataset, which is listings")
data1 = pd.read_csv("../data/listings.csv",low_memory=False)
st.write(data1.head(5))
st.write()
st.write()
st.write("Let us have a look at our second dataset, which is listings_summary")
data2 = pd.read_csv("../data/listings_summary.csv",low_memory=False)
st.write(data2.head(5))