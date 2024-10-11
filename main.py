import streamlit as st
from streamlit_option_menu import option_menu


with st.sidebar:
    selected=option_menu(
        menu_title='Class Meeting Abu Dzar',
        options=['home','Leaderboard','Lomba Class Meeting']
    )

if selected=='home':
    st.title('Pusat Informasi Class Meeting Abu Dzar 2024')
    st.header('Tentang Class Meeting Abu Dzar')
    st.write(
        """
        Class Meeting merupakan kegiatan yang berlangsung setelah kegiatan Sumatif Akhir Semester dilaksanakan. Kegiatan ini merupakan sebuah refreshment untuk peserta didik setelah mengikuti SAS.
        Tujuan kegiatan Class Meeting diantara lain:
        - A
        - B
        - C

        Manfaat kegiatan Class Meeting diantara lain:
        - A
        - B
        - C
        """
    )
if selected=='Leaderboard':
    st.title('Klasemen Sementara Class Meeting 2024')
if selected=='Lomba Class Meeting':
    st.title(f'you have selected {selected}')
