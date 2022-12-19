import streamlit as st
from PIL import Image
import sqlite3
from sqlite3 import Error
from PIL import Image


conn = None
try:
    conn = sqlite3.connect('Copa.db')
except Error as e:
    print(e)

st.set_page_config(page_title='Search - Artist DB App', layout = 'wide')
with st.container():
    left_column, right_column = st.columns([4, 1])
    with right_column:
        logo = Image.open('cuLogo.png')
        st.image(logo)
    with left_column:
        st.title("What would you like to search for?")



with st.container():
    cur = conn.cursor()
    #conn.commit()

    st.header("Quick Seach")
    left_column, left, middle, right = st.columns(4)
    sql = ''
    with left_column:
        search1_but = st.button('Display all Dance Majors', key = 10)
        if search1_but:
            sql = '''SELECT * FROM Student WHERE departmentID = 1'''

            #display query
    with left:
        search2_but = st.button('Display all Theater Majors', key = 11)
        if search2_but:
            sql = '''SELECT * FROM Student WHERE departmentID = 2'''

    with middle:
        search3_but = st.button('Display all Music Majors', key = 12)
        if search3_but:
            sql = '''SELECT * FROM Student WHERE departmentID = 3'''

    with right:
        search4_but = st.button('Display all Film Majors', key = 13)
        if search4_but:
            sql = '''SELECT * FROM Student WHERE departmentID = 4'''


    cur.execute(sql)
    results = cur.fetchall()
    for row in results:
        st.write(row)

    st.write("Other quick search options:")
    st.write("- by department and year")
    st.write("- by major (Dance/Theater: BA vs BFA Film/Music: lots of majors in the departments)")
    st.write("- by major and yes")
    st.write("- students who have been in certain works")
    st.write("- students who have completed certain rolls")


with st.container():
    st.header("Create your own seach")
    st.write("This might be ambitious and still trying to work out the logistics here")
