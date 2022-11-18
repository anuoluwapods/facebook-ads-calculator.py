import streamlit as st
import pandas as pd
import numpy as np

st.title('Click through rate')
st.write('Also known as the average click per sales')

unique= st.number_input('Enter number of unique clicks')
ads = st.number_input('Enter the number of ad impressions')

if st.button('💰'):
  ctr = (unique / ads)
  st.write("Click through rate = {}". format(ctr))
