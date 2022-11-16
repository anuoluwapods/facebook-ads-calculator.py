import streamlit as st
import pandas as pd
import numpy as np

st.title('Conversion Rate ROI')

conv = st.number_input('Enter conversion rate')
cvpc = st.number_input('Enter the conversion per clicks')
curr2 = st.text_input('Enter currency symbol')

if st.button('💰'):
  convperc = (conv / 100)
  cvroi = (convperc * cvpc)
  st.write("Conversion Rate ROI = {}{}". format(curr2, cvroi))
