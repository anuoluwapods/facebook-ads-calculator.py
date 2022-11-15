import streamlit as st
import pandas as pd
import numpy as np

st.title('Calculating the cost per action of an ad')

cost = st.number_input('Enter the cost per click')
click = st.number_input('Enter the average clicks per sale')

if st.button('💰'):
  cpa = click * cost
  st.write("Cost Per Action Is: " cpa)
  
 
  
 
