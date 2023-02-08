import streamlit as st
import requests
import os
import json
import openai
import time

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
    begin = c.button("Begin")

    

    

# Send the initial prompt to the API
initial_prompt = prompts[selected_prompt]
st.write(initial_prompt)

# Get Response Function -----
@st.cache
def get_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    if response:
        return response["choices"][0]["text"]
    else:
        return None

# Write the response

if begin:
    response = get_response(initial_prompt)
    st.write("Geeting:", response)


# Get original text input
original_text = st.text_area("Enter your text here:")


# Make API request and display response
# run some long-running and blocking code

if original_text:
    st.spinner("Working...")
    response = get_response(initial_prompt & original_text)
             
    if response:
        st.write("Generated text:")
        st.write(response)
    else:
        st.write("An error occurred.")
    st.success("All done, now leave me alone")



