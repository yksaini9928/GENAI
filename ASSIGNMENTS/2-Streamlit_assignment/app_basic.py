import streamlit as st

st.title("Welcome to streamlit")

st.text("Enter your name")
name = st.text_input("Name", "")



if st.button("Greet Me"):
   if name.strip():
     st.write(f"Hello, {name}!")
   else:
     st.write("Please enter your name.")