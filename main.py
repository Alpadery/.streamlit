import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Class Meeting', layout='wide')

with st.sidebar:
    selected=option_menu(
        menu_title='Class Meeting Abu Dzar',
        options=['Class Meeting 2024','Lomba Class Meeting','Leaderboard']
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
    st.write('[Click Here >](https://www.youtube.com/live/ibEefMmPfrg?si=q_8Ii5MS1T8Kgdeq)')

    st.header('Jadwal Kegiatan Class Meeting 2024')
    image=Image.open('jadwal.png')
    st.image(image,
             use_column_width=True)


if selected=='Lomba Class Meeting':
    st.title('Lomba Pada Kegiatan Class Meeting 2024')
    st.header("What's new? *Keep scrolling*")
    st.write('---')
    st.subheader('A. Estafet 🧩')
    st.write('Lomba estafet adalah')
    st.subheader('**Cara Bermain:**')
    st.write(
        """
        1. A
        2. B
        3. C
        """)

    st.write('---')
    st.subheader('B. Futsal ⚽')
    st.write('Lomba futsal adalah')
    st.subheader('**Cara Bermain:**')
    st.write(
        """
        1. A
        2. B
        3. C
        """)

    st.write('---')
    st.subheader('C. Basket 🏀')
    st.write('Lomba basket adalah')
    st.subheader('**Cara Bermain:**')
    st.write(
        """
        1. A
        2. B
        3. C
        """)
    
    st.write('---')
    st.subheader('D. Blind Bottle 😎')
    st.write('Lomba blind bottle adalah')
    st.subheader('**Cara Bermain:**')
    st.write(
        """
        1. A
        2. B
        3. C
        """)
    
    st.write('---')
    st.subheader('E. Volly Sarung 🏐')
    st.write('Lomba blind bottle adalah')
    st.subheader('**Cara Bermain:**')
    st.write(
        """
        1. A
        2. B
        3. C
        """)

    st.write('---')
    st.subheader('F. Bola Beracun 🏉')
    st.write('Lomba bola beracun adalah')
    st.subheader('**Cara Bermain:**')
    st.write(
        """
        1. A
        2. B
        3. C
        """)

    st.write('---')
    st.subheader('G. Chopstick Ball 🥢')
    st.write('Lomba chopstick ball adalah')
    st.subheader('**Cara Bermain:**')
    st.write(
        """
        1. A
        2. B
        3. C
        """)
   
if selected=='Leaderboard':
    st.title('Klasemen Sementara Class Meeting 2024')
