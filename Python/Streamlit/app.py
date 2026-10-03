import streamlit as st
import pandas as pd

st.write("Hello Avinash")

st.title("This is Streamlit Title")
st.write("This is my first Streamlit Web App")
st.header("This is streamlit header")
st.subheader("This is subheader")
st.text("This is plain text")

# Button
if st.button("click me"):
    st.write("Button clicked")

# checkbox
agree = st.checkbox("I agree")
if agree:
    st.write("You agreed")

# Slider
level = st.slider("Select a level: ", 1, 10, 5)
st.write(f"Selected level: {level}")

# file upload
uploaded_file = st.file_uploader("Upload a file", type=["csv","txt"])
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)                     # import pandas for this line

