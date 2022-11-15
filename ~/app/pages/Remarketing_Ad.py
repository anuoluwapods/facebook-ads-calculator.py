import streamlit as st
import pandas as pd
import numpy as np

st.title('Remarketing Ad')

cpa = st.number_input('Enter the CPA Value')
rad = st.number_input('Enter Cost of remarketing ad')
curr1 = st.text_input('Enter currency symbol')

if st.button('💰'):
  rmad = cpa - rad
  st.write("Cost of Remarketing Ad = {}{}".format(curr1, rmd))
