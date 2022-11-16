import streamlit as st
import pandas as pd
import numpy as np

st.title('Profit Value')

clv = st.number_input('Enter customer life time value')
cpa = st.number_input('Enter the cost per action value')
sales = st.number_input('Enter no of sales')
curren = st.text_input('Enter currency symbol')

if st.button('💰'):
  sale = (cpa * sales)
  profit = (clv - sale)
  st.write("Conversion Rate ROI = {}{}". format(curren, profit))
