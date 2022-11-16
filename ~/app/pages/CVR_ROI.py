import streamlit as st
import pandas as pd
import numpy as np

st.title('Conversion Rate ROI')

cvrv = st.number_input('Enter the conversion rate value')
crvc = st.number_input('Enter the cconversion per clicks')
curr3 = st.text_input('Enter currency symbol')

if st.button('💰'):
  cvrvp = (cvrv / 100)
  cpvroi = (crvc * cvrvp)
  st.write("Conversion Rate ROI = {}{}". format(curr3, cpvroi))
