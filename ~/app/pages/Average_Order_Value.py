import streamlit as st
import pandas as pd
import numpy as np

st.title('Average Order Value')
st.write('Used for calculating customer lifetime value')

rev = st.number_input('Enter the total revenue value')
orders = st.number_input('Enter the total number of orders')

if st.button('💰'):
  aov = (rev / orders)
  st.write("Averge order value = {}". format(aov))
