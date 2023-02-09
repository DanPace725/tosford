import streamlit as st
import requests, os, json, openai
import functions 


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
   

    
casual = functions.get_prompt("Casual")
st.write(casual)    

# Send the initial prompt to the API
initial_prompt = prompts[selected_prompt]
st.write(initial_prompt)
begin = st.button("Begin")

if begin:
    response = functions.get_response(initial_prompt)
    st.write("Geeting:", response)

if response !=  None:
    user_input1 = st.text_area("Enter your text here:")

if user_input1:
    response2 = functions.get_response(initial_prompt + " " + user_input1)


