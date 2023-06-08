import streamlit as st
import datetime
import time
import os

# создание div блока для сообщений
message_style = """
    <style>
        .message {
            padding: 10px;
            margin: 5px;
            background-color: black;
            border-radius: 10px;
        }
    </style>
"""

st.markdown(message_style, unsafe_allow_html=True)


messages_container = st.empty() 

def display_messages():

    if not os.path.exists("messages.txt"):
        with open("messages.txt", "w") as f:
            f.write("")

    with open("messages.txt", "r", encoding='utf-8') as f:
        messages = f.readlines()
        messages_container.empty()
        message = '\n'.join(messages)

        messages_container.write(f"<div class='message'><b>:</b> {message}</div>", unsafe_allow_html=True)

display_messages()


message = st.text_input("Введите сообщение", max_chars=500, key="message_input")
if st.button("Отправить"):
    if message:
        with open("messages.txt", "a+") as f:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"User: {message} ({now})\n")
        st.session_state.clear_input = True
    else:
        st.write("Введите сообщение")

if st.session_state.get("clear_input"):
    message = ""
    st.session_state.clear_input = False

while True:

    display_messages()

    time.sleep(1)
