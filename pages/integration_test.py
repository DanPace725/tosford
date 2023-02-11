import streamlit as st
import requests, os, json, openai
import custom_functions as cf


openai.api_key = os.getenv("OPENAI_API_KEY")

# Header -----
st.title("A chatbot of sorts")

chat_history = []

# Sidebar -----
with st.sidebar:
    c = st.container()
    c.write("Pick the tone:")
    with open('prompts.json') as f:
        prompts = json.load(f)
    selected_prompt = c.selectbox("Select a Prompt", list(prompts.keys()))
   
# Send the initial prompt to the API
initial_prompt = prompts[selected_prompt]
st.write(initial_prompt)

user_input1 = st.text_input("Enter your text here:")

enter = st.button("Enter")
    
if enter:
    with st.spinner("Thinking..."):
        response = cf.get_response(initial_prompt + " " + user_input1)
    
        st.write(response)
    chat_history.append(f"User: {user_input1}")
    chat_history.append(f"Bot: {response}")
    st.success("Done")
    
# Show the chat history
st.write("Chat History:")
for i, history in enumerate(chat_history):
    st.write("#" + str(i+1), history)
