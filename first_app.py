import streamlit as st
num = str.slider("Choose any number ", 1,100) 
st.write("square of ", num , "is" , num ** 2 )
