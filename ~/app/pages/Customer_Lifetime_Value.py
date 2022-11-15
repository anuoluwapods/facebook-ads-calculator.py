import streamlit as st
import pandas as pd
import numpy as np

st.title('Customer Lifetime Value')

aov = st.number_input('Enter the Avg Order Value')
noo = st.number_input('Enter the no of orders per year')
cust = st.number_input('Enter the no of years as a customer')
curr1 = st.text_input('Enter currency symbol')

if st.button('💰'):
  clv = (aov * noo * cust)
  st.write("Customer Lifetime Value = {}{}".format(curr1, clv))
