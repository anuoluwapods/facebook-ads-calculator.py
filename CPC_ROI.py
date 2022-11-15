import streamlit as st
import pandas as pd
import numpy as np

st.title('ROI For Cost Per Click')

noc = st.number_input('Enter value of no of clicks')
cpcv = st.number_input('Enter value of cost per click')
curr2 = st.text_input('Enter currency symbol')

if st.button('💰'):
  roicpc = (noc / cpcv)
  st.write("Cost Per Click ROI = {}{}". format(curr2, roicpc))
