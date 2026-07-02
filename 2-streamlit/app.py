from turtle import pd

import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, welcome to the Streamlit app!")
st.title("My First Streamlit App" )
st.write("This is a simple app to demonstrate Streamlit capabilities.")
st.write("You can use Streamlit to create interactive web applications with Python.")
st.header("Features")
st.subheader("1. Easy to Use")
st.text("Streamlit provides a simple and intuitive API for building web apps.")
st.write("You can create interactive widgets, display data, and visualize results with just a few lines of code.")


# Button example
if st.button("Click Me"):
    st.write("Button clicked! You can add your own functionality here.")

# checkbox example
if st.checkbox("Show more information"):
    st.write("Here is some additional information that can be displayed when the checkbox is checked.")
    st.write("You can use checkboxes to toggle the visibility of content in your app.")      

# slider example
age = st.slider("Select your age", 0, 100, 25)
st.write(f"You selected: {age} years old.") 
with st.expander("More details"):
    st.write("You can use expanders to hide or show additional content in your app.")
    st.write("This is useful for keeping your app clean and organized.")


upload_file = st.file_uploader("Upload a file", type=["csv", "txt"])
if upload_file is not None:
    df=pd.read_csv(upload_file)
    st.write(df.head())
    st.write("File uploaded successfully!")
    # You can add code here to process the uploaded file as needed.     
    # For example, you can read the contents of the file and display it in the app.    