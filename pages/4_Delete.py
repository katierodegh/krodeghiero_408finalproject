import streamlit as st
import sqlite3
from sqlite3 import Error
from PIL import Image

conn = None
try:
    conn = sqlite3.connect('Copa.db')
except Error as e:
    print(e)

st.set_page_config(page_title='Delete - Artist DB App', layout = 'wide')

with st.container():
    left_column, right_column = st.columns([4, 1])
    with right_column:
        logo = Image.open('cuLogo.png')
        st.image(logo)
    with left_column:
        st.title("Which student would you like to delete?")

with st.container():
    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""

    my_input = st.text_input("Input a student ID number", st.session_state["my_input"])
    submit = st.button("Submit")
    if submit:
        st.session_state["my_input"] = my_input

        try:
            cur = conn.cursor()
            query = "DELETE FROM Student WHERE studentID = " + my_input + ";"
            cur.execute(query)
            conn.commit()
            st.session_state["my_input"] = ""
        except Error as e:
            print(e)
            #st.caption("Not a valid student ID, try again please")

conn.close()
