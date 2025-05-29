import streamlit as st
import os
from groq import Groq

st.title("ChatBot Using Groq & Streamlit")

if 'model' not in st.session_state:
    st.session_state['model'] = Groq(api_key='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')

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

st.sidebar.title("Model Parameters")
selected_model = st.selectbox("Select Model", options=[
    'gemma2-9b-it',
    'llama-3.3-70b-versatile',
    'whisper-large-v3-turbo'
])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
max_tokens = st.sidebar.slider("Max Tokens", min_value=1, max_value=1024, value=512)

for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt := st.chat_input("Enter your query"):
    st.session_state['messages'].append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.markdown(prompt)

    with st.chat_message('assistant'):
        client = st.session_state['model']
        stream = client.chat.completions.create(
            model=selected_model,
            messages=[{'role': m['role'], 'content': m['content']} for m in st.session_state['messages']],
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True
        )
        response = st.write_stream(
    (chunk.choices[0].delta.content for chunk in stream if chunk.choices[0].delta.content)
)


    st.session_state['messages'].append({'role': 'assistant', 'content': response})
