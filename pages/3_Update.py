import streamlit as st
import sqlite3
from sqlite3 import Error
from PIL import Image

conn = None
try:
    conn = sqlite3.connect('Copa.db')
except Error as e:
    print(e)

cur = conn.cursor()

st.set_page_config(page_title='Update - Artist DB App', layout = 'wide')

with st.container():
    left_column, right_column = st.columns([4, 1])
    with right_column:
        logo = Image.open('cuLogo.png')
        st.image(logo)
    with left_column:
        st.title("What record would you like to update?")

# def input_func(desc):
#     if "my_input" not in st.session_state:
#         st.session_state["my_input"] = ""
#
#     my_input = st.text_input("Input " + desc, st.session_state["my_input"])
#     submit = st.button("Submit")
#     if submit:
#         print("Submited")
#         st.session_state["my_input"] = my_input
#         print("INPUT")
#         print(my_input)
#         query_func(my_input)
#
# def query_func(my_input):
#     try:
#         cur = conn.cursor()
#         query = "SELECT * FROM Student WHERE studentID = " + my_input + ";"
#         cur.execute(query)
#         conn.commit()
#
#         results = cur.fetchall()
#         for row in results:
#             st.write(row)
#
#
#         st.session_state["my_input"] = ""
#     except Error as e:
#         print(e)




with st.container():
    stud_but = st.button("Student Info")
    if stud_but:
        if "my_input" not in st.session_state:
            st.session_state["my_input"] = ""

            my_input = st.text_input("Input a student ID number")
            submit = st.button("Submit")

            update5_but = st.button("Update Name", key = 5)
            update6_but = st.button("Update Email", key = 6)
            update1_but = st.button("Update Year", key = 1)
            update2_but = st.button("Update Major", key = 2)
            update3_but = st.button("Update Resume", key = 3)
            update4_but = st.button("Update Reel", key = 4)


            #if submit == True:






# with st.container():
#     student_but1 = st.button("Student Info")
#
#     if "my_input" not in st.session_state:
#         st.session_state["my_input"] = ""
#
#     my_input = st.text_input("Input a student ID number", st.session_state["my_input"])
#     submit = st.button("Submit")
#
#     if submit:
#         st.session_state["my_input"] = my_input
#
#         try:
#             cur = conn.cursor()
#             query = "SELECT * FROM Student WHERE studentID = " + my_input + ";"
#             cur.execute(query)
#             conn.commit()
#
#             results = cur.fetchall()
#             for row in results:
#                 st.write(row)
#
#
#             st.session_state["my_input"] = ""
#
#         except Error as e:
#             print(e)


            #st.caption("Not a valid student ID, try again please")
    department_but = st.button("Department Info")

    if department_but:
        if "my_input" not in st.session_state:
            st.session_state["my_input"] = ""

            my_input = st.text_input("Input a department")
            submit = st.button("Submit")

            st.write("These buttons are supposed to pop up after inputting the department")
            st.write("On event command not really working")

            update4_but = st.button("Update Chair", key = 8)
            update5_but = st.button("Update Advisor", key = 9)


conn.close()
