import streamlit as st

file_path = "C:/Users/nscha/anaconda3/envs/toswebapp/Main/tosford/pages/text.md"


with open("C:/Users/nscha/anaconda3/envs/toswebapp/Main/text.md") as f:
    markdown_text = f.read()

st.markdown(markdown_text)

