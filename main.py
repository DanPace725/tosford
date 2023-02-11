import streamlit as st
import requests, os, json, openai
import custom_functions as cf


openai.api_key = os.getenv("OPENAI_API_KEY")

# Header -----
st.title("A chatbot of sorts")


# Sidebar -----
with st.sidebar:
    c = st.container()
    c.write("Pick the tone:")
    with open('prompts.json') as f:
        prompts = json.load(f)
    selected_prompt = c.selectbox("Select a Prompt", list(prompts.keys()))
   
# Send the initial prompt to the API
initial_prompt = prompts[selected_prompt]

user_input1 = st.text_input("Enter your text here:")

enter = st.button("Enter")
    
if enter:
    text = cf.get_response(initial_prompt + " " + user_input1)
    st.write(text)
    
    