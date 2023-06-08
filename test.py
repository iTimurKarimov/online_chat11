import streamlit as st
import datetime
import time

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

# создание файла для хранения сообщений
messages_container = st.empty()  # создание "пустого" места для отображения сообщений

def display_messages():

    with open("messages.txt", "r") as f:
        messages = f.readlines()
        messages_container.empty()
        message = ' \n\n'.join(messages)

        messages_container.write(f"<div class='message'><b>:</b> {message}</div>", unsafe_allow_html=True)

display_messages()

# создание формы для отправки сообщений
message = st.text_input("Введите сообщение", max_chars=500, key="message_input")
if st.button("Отправить"):
    if message:
        with open("messages.txt", "a+") as f:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"User: {message} ({now})\n")
        st.text_input("", value="", key="clear_input", disabled=True)
    else:
        st.write("Введите сообщение")

# автоматическое обновление сообщений
while True:

    display_messages()  # отображение сообщений

    time.sleep(1)