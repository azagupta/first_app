import streamlit as st
num = st.slider("Choose any number ", 1,100) 
st.write("square of ", num , "is" , num ** 2 )
