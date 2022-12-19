import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Artist DB App',
    layout = 'wide',
)

st.title('Welcome')
#st.sidebar.success("Select a page above.")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        Copa = Image.open('COPAlogo.png')
        st.image(Copa)
    with right_column:
        Dodge = Image.open('DodgeLogo2.png')
        st.image(Dodge)

with st.container():
    st.header('')
    st.header('')
    st.header('<-- Please choose an action from the menu on the left')
