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

# создание боковой панели для выбора имени пользователя
with st.sidebar:
    st.write("Выберите имя пользователя:")
    username = st.text_input("", max_chars=50)

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

# создание текстового поля для ввода сообщения (видимое только после ввода имени пользователя)
if username:
    message = st.text_input("Введите сообщение", max_chars=500, key="message_input")
    if st.button("Отправить"):
        if message:
            with open("messages.txt", "a+") as f:
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{username}: {message} ({now})\n")
        else:
            st.write("Введите сообщение")
else:
    st.write("Введите имя пользователя в боковой панели")

while True:

    display_messages()

    time.sleep(1)
