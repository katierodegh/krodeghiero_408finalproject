import streamlit as st
import sqlite3
from sqlite3 import Error
import random
from PIL import Image

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_student(conn, studentID, studentName, studentPhone, studentEmail, studentYear, studentMajor, departmentID, url, resume):
    """
    Create a new student into the student table
    :param conn:
    :param student:
    :return: student id
    """
    # sql = ''' INSERT INTO student(studentID, studentName,
    #     studentPhone, studentEmail, studentYear, studentMajor,
    #     departmentID, url, resume) VALUES(?,?,?,?,?,?,?,?,?)'''

    cur = conn.cursor()
    cur.execute(''' INSERT INTO student(studentID, studentName,
        studentPhone, studentEmail, studentYear, studentMajor,
        departmentID, url, resume) VALUES(?,?,?,?,?,?,?,?,?)''', (studentID, studentName, studentPhone, studentEmail, studentYear, studentMajor, departmentID, url, resume))
    conn.commit()
    return cur.lastrowid

def create_work(conn, workID, departmentID, type, year, director):
    """
    Create a new work
    :param conn:
    :param work:
    :return:
    """

    sql = (''' INSERT INTO work(workID, departmentID, type, year, director)
              VALUES(?,?,?,?,?) ''', (workID, departmentID, type, year, director))
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

    return cur.lastrowid

st.set_page_config(page_title='Add - Artist DB App', layout = 'wide')
with st.container():
    left_column, right_column = st.columns([4, 1])
    with right_column:
        logo = Image.open('cuLogo.png')
        st.image(logo)
    with left_column:
        st.title("What would you like to add?")


def stud_form():
    randVal = random.randint(0, 100000)

    st.write("Please enter a new student's information")
    with st.form(key='Information form'):
        hold = st.text_input('Student ID*', value=randVal)
        #studentID = st.text_input('Student ID*')
        studentName = st.text_input('Name*')
        studentPhone = st.text_input('Phone Number')
        studentEmail = st.text_input('Email Address*')
        hold1 = st.text_input('Academic Year', value="0")
        #studentYear = st.text_input('Academic Year')
        studentMajor = st.text_input('Major*')
        #departmentID = st.text_input('Department*')
        hold2 = st.text_input('Department*', value="0")
        url = st.text_input('Website')
        resume = st.text_input('Resume')

        submission = st.form_submit_button(label = 'Submit')
        studentID = int(hold)
        studentYear = int(hold1)
        departmentID = int(hold2)

        #params = (studentID, studentName, studentPhone, studentEmail, studentYear, studentMajor, departmentID, url, resume)

    if submission == True:
        st.success('We Submitted')
        createStudent(create_connection(r'Copa.db'), studentID, studentName, studentPhone, studentEmail, studentYear, studentMajor, departmentID, url, resume)
        #     studentID = int(hold)
        #     studentYear = int(hold1)
        #     departmentID = int(hold2)
        #
        #     params = (studentID, studentName, studentPhone, studentEmail, studentYear, studentMajor, departmentID, url, resume)
        #     st.success('We Submitted')

        #return params



def work_form():
    st.write("Please enter a new work's information")
    with st.form(key='Information form'):
        hold = st.text_input('workID*', value="0")
        hold1 = st.text_input('departmentID*', value="0")
        type = st.text_input('Type of Work (Works, Masters, AP, IP, Thesis, Our Town, Meta)')
        hold2 = st.text_input('Year', value="0")
        director = st.text_input('Director*')

        submission = st.form_submit_button(label = 'Submit')
        #create_work(create_connection(r'Copa.db'), workID, departmentID, type, year, director)


        workID = int(hold)
        departmentID = int(hold1)
        year = int(hold2)


        if submission == True:
            st.success('We Submitted')
            create_work(create_connection(r'Copa.db'), workID, departmentID, type, year, director)


with st.container():

    #conn = create_connection(r'Copa.db')

    student_but = st.button('Student')
    if student_but:
        #create_student(conn, stud_form())
        stud_form()
        st.write("Once a student is subitted, user will them be prompted to add the student's classes")

    studClass_but = st.button('Student Class')

    work_but = st.button('Work')
    if work_but:
        work_form()

    studWork_but = st.button('Student Work')

#conn.close()
