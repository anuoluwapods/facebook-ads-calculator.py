import streamlit as st
import numpy as np
import pandas as pd

st.title('Calculating the cost per action of an ad')

cost = st.text_input('Enter the cost per click')
clicks = st.text_input('Enter the average clicks per sale')

if st.button('💰'):
  st.write(costs * clicks) 
