import streamlit as st
import openai
import json, time

# Get Response Function -----

def get_response(prompt):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
      
    )
    if response:
        return {
    "text": response["choices"][0]["text"],
    "total_tokens": response["usage"]["total_tokens"]
    }

  
    else:
        return "There was a problem"

# Get Prompt Function -----
def get_prompt(prompt_id):
    with open('prompts.json') as f:
        prompts = json.load(f)
    return prompts.get(prompt_id)

