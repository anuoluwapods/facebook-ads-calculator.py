import streamlit as st
import pandas as pd
import numpy as np

st.title('Calculating the cost per action of an ad')

cost = st.text_input('Enter the cost per click')
click = st.text_input('Enter the average clicks per sale')

if st.button('💰'):
  cpa = click * cost
  st.write(cpa)
  
 
  
 
