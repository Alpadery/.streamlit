import streamlit as st
from streamlit_option_menu import option_menu


with st.sidebar:
    selected=option_menu(
        menu_title='main menu',
        options=['home','projects','contact']
    )

if selected=='home':
    st.title('Selamat Datang')
    st.header('class meeting')
    st.write('cara bermain')
if selected=='projects':
    st.title(f'you have selected {selected}')
if selected=='contact':
    st.title(f'you have selected {selected}')