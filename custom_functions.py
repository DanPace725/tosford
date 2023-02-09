import streamlit as st
import openai
import json, time

# Get Response Function -----
@st.cache
def get_response(prompt):

    response = openai.Completion.create(
        model="text-curie-001",
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

# Get Prompt Function -----
def get_prompt(prompt_id):
    with open('prompts.json') as f:
        prompts = json.load(f)
    return prompts.get(prompt_id)

def show_spinner(text):
    with st.spinner(text):
        time.sleep(5)