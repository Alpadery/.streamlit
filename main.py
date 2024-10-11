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
if selected=='Leaderboard':
    st.title('Klasemen Sementara Class Meeting 2024')
if selected=='Lomba Class Meeting':
    st.title(f'you have selected {selected}')
