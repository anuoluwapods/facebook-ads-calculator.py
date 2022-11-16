import streamlit as st
import pandas as pd
import numpy as np

st.title('Cost Per Click ROI')

clicks = st.number_input('Enter no of clicks')
cpcv = st.number_input('Enter the cost per click value')
curr2 = st.text_input('Enter currency symbol')

if st.button('💰'):
  cpcroi = (clicks / cpcv)
  st.write("Cost Per Action = {}{}". format(curr2, cpcroi))
