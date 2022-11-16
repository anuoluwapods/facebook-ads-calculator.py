import streamlit as st
import pandas as pd
import numpy as np

st.title('Ad Frequency Value')
st.write('A good ad frequency is around 1 to 2')

impr = st.number_input('Enter the impression value')
reac = st.number_input('Enter the reach value')
curr4 = st.text_input('Enter currency symbol')

if st.button('💰'):
  adfreq = (imp / reac)
  st.write("Conversion Rate ROI = {}{}". format(curr4, adfreq))
