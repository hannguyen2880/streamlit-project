import streamlit as st
from hugchat import hugchat
from hugchat.login import Login

# Generating LLM response


def generate_response(prompt_input, email, password):
    sign = Login(email, password)
    cookies = sign.login()
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)


# MAIN PROGRAM
# ChatBot Title
st.title('Simple ChatBot')
with st.sidebar:
    st.title('Login HugChat')
    email = st.text_input('Enter email:')
    password = st.text_input('Enter password:', type='password')
    if email and password:
        st.success('Proceed to entering your prompt message!')
    else:
        st.warning('Please enter your account!')

# Store LLM generated responses and display first message
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "How may I help you?"}]

for message in st.session_state.messages:
    with st.chat_message("assistant"):
        st.write(message["content"])

# User-provided prompt
if prompt := st.chat_input(disabled=not (email and password)):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate other responses
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt, email, password)
            st.write(response)
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
