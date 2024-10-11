import streamlit as st
import pandas as st
import plotly.express as px
from PIL import Image
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
        Class Meeting merupakan kegiatan yang berlangsung setelah kegiatan Sumatif Akhir Semester dilaksanakan. Kegiatan ini merupakan sebuah *refreshment* untuk peserta didik setelah mengikuti SAS.""")
    
    st.write('---')
    st.header('Tujuan dan Manfaat kegiatan Class Meeting diantara lain:')
    st.write(
        """
        1. Ajang hiburan dan relaksasi pasca ujian.
        2. Mengembangkan bakat dan minat.
        3. Mempererat hubungan antar siswa.
        4. Mencari bibit prestasi ekstrakulikuler.
        5. Melatih mental dan daya saing.
        6. Memberikan kesempatan berekspresi.
        """)
    
    st.write('Berikut hasil dokumentasi kegiatan Class Meeting 2023')
    st.write('[Watch Here >](https://www.youtube.com/live/ibEefMmPfrg?si=q_8Ii5MS1T8Kgdeq)')

    image = Image.open("images.jpg")

if selected=='Leaderboard':
    st.title('Klasemen Sementara Class Meeting 2024')
if selected=='Lomba Class Meeting':
    st.title(f'you have selected {selected}')
