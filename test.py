import streamlit as st
import datetime
import time
import os

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

if not os.path.exists("users.txt"):
    with open("users.txt", "w") as f:
        f.write("")

with st.sidebar:
    st.write("Введите имя пользователя:")
    username = st.text_input("", max_chars=12)

    st.write("Введите пароль:")
    password = st.text_input("", type="password", max_chars=50)

    if st.button("Зарегистрироваться"):
        if username and password:
            with open("users.txt", "r") as f:
                users = f.readlines()

            if any(username in user for user in users):
                st.write("Этот пользователь уже зарегистрирован")
            else:
                with open("users.txt", "a") as f:
                    f.write(f"{username}:{password}\n")
                st.write("Вы успешно зарегистрировались!")
        else:
            st.write("Введите имя пользователя и пароль")

    if st.button("Войти"):
        if username and password:
            with open("users.txt", "r") as f:
                users = f.readlines()

            if any(f"{username}:{password}" in user for user in users):
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

                message = st.text_input("Введите сообщение", max_chars=500, key=username)
                if st.button("Отправить"):
                    if message:
                        with open("messages.txt", "a+") as f:
                            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            f.write(f"{username}: {message} | ```{now}```\n")
                    else:
                        st.write("Введите сообщение")

                display_messages()
            else:
                st.write("Неверное имя пользователя или пароль")
        else:
            st.write("Введите имя пользователя и пароль")


    if username and password:
        messages_container = st.empty()

        while True:
            def display_messages():

                if not os.path.exists("messages.txt"):
                    with open("messages.txt", "w") as f:
                        f.write("")

                with open("messages.txt", "r", encoding='utf-8') as f:
                    messages = f.readlines()
                    messages_container.empty()
                    message = '\n'.join(messages)

                    messages_container.write(f"<div class='message'><b>:</b> {message}</div>", unsafe_allow_html=True)

            message = st.text_input("Введите сообщение", max_chars=500, key=username)
            if st.button("Отправить", key=username):
                if message:
                    with open("messages.txt", "a+") as f:
                        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        f.write(f"{username}: {message} ({now})\n")
                else:
                    st.write("Введите сообщение")

            display_messages()

            time.sleep(1)
