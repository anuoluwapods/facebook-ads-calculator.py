import streamlit as st
import maths

st.title('Calculating the cost per action of an ad')

cost = st.text_input('Enter the cost per click')
clicks = st.text_input('Enter the average clicks per sale')

if st.button('💰'):
  def cpa (cost, clicks):
    st.write(return cost * clicks)
 
