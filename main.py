import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected=option_menu(
        menu_title='Class Meeting Abu Dzar',
        options=['Class Meeting 2024','Leaderboard','Lomba Class Meeting']
    )

if selected=='Class Meeting 2024':
    st.title('Pusat Informasi Class Meeting Abu Dzar 2024')
    st.header('Tentang Class Meeting Abu Dzar')
    st.write(
        """
        Class Meeting merupakan kegiatan yang berlangsung setelah kegiatan Sumatif Akhir Semester dilaksanakan. Kegiatan ini merupakan sebuah refreshment untuk peserta didik setelah mengikuti SAS.""")
    
    st.write('---')
    st.header('Tujuan kegiatan Class Meeting diantara lain:')
    st.write(
        """
        - A
        - B
        - C
        """)

    st.write('---')
    st.header('Manfaat kegiatan Class Meeting diantara lain:')
    st.write("""
        - A
        - B
        - C
          """)
    
    st.write('---')
    st.header('Keseruan Kegiatan Class Meeting 2023')
    st.image('doggo.jpg')

if selected=='Leaderboard':
    st.title('Klasemen Sementara Class Meeting 2024')
if selected=='Lomba Class Meeting':
    st.title(f'you have selected {selected}')
