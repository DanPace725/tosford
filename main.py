import streamlit as st
import requests, os, json, openai
import custom_functions as cf


openai.api_key = os.getenv("OPENAI_API_KEY")

# Header -----
st.title("TOS for D")
st.header("Terms of Service for Dummies")
st.subheader("Everyone knows no one know what the Terms of Service actually say. I read one once and now we're here.")
st.write("This helpful tool will break down the terms of service using AI to give it to you straight")


# Sidebar -----
with st.sidebar:
    c = st.container()
    c.write("Click the type of summarization you want:")
    with open('prompts.json') as f:
        prompts = json.load(f)
    selected_prompt = c.selectbox("Select a Prompt", list(prompts.keys()))
   
# Send the initial prompt to the API
initial_prompt = prompts[selected_prompt]
st.write(initial_prompt)
user_input1 = st.text_area("Enter your text here:")

enter = st.button("Enter")
    
if enter:
    with st.spinner("Thinking..."):
        response2 = cf.get_response(initial_prompt + " " + user_input1)
    
        st.write(response2)
    st.success("Alright, I'm done, now leave me alone.")