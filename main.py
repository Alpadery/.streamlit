import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Class Meeting', layout='wide')

with st.sidebar:
    selected=option_menu(
        menu_title='Class Meeting Abu Dzar',
        options=['Class Meeting 2024','Lomba Class Meeting','Leaderboard','Klasemen Ikhwan']
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
    st.header("What's new? *Keep scrolling* 🙌")
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
    st.title('Leaderboard Class Meeting 2024')
    st.write('---')
    image=Image.open('leaderboard.png')
    st.image(image,
             use_column_width=True)


if selected=='Klasemen Ikhwan':
#ESTAFET
    st.title('Klasemen Estafet')
    st.write('---')
    st.header('Estafet Fase A')
    with st.popover("Klasemen Estafet"):
        image=Image.open('estafet_a.png')
        st.image(image,
                 use_column_width=True)
        st.header('Estafet Fase B')
        image=Image.open('estafet_b.png')
        st.image(image,
                 use_column_width=True)
        st.header('Estafet Fase C')
        image=Image.open('estafet_c.png')
        st.image(image,
                 use_column_width=True)
    
#FUTSAL
    st.write('---')
    st.title('Klasemen Futsal')
    st.write('---')
    st.header('Futsal Fase A')
    image=Image.open('futsal_a.png')
    st.image(image,
             use_column_width=True)
    
    st.header('Futsal Fase B')
    image=Image.open('futsal_b.png')
    st.image(image,
             use_column_width=True)
    
    st.header('Futsal Fase C')
    image=Image.open('futsal_c.png')
    st.image(image,
             use_column_width=True)


#BASKET
    st.write('---')
    st.title('Klasemen Basket')
    st.write('---')
    st.header('Basket Fase A')
    image=Image.open('basket_a.png')
    st.image(image,
             use_column_width=True) 
    
    st.header('Basket Fase B')
    image=Image.open('basket_b.png')
    st.image(image,
             use_column_width=True) 

#BLIND BOTTLE
    st.write('---')
    st.title('Klasemen Blind Bottle')
    st.write('---')
    st.header('Blind Bottle Fase A')
    image=Image.open('blind_bottle_a.png')
    st.image(image,
             use_column_width=True)
    
    st.header('Blind Bottle Fase B')
    image=Image.open('blind_bottle_b.png')
    st.image(image,
             use_column_width=True)
    
    st.header('Blind Bottle Fase C')
    image=Image.open('blind_bottle_c.png')
    st.image(image,
             use_column_width=True)

#VOLLY SARUNG
    st.write('---')
    st.title('Klasemen Volly Sarung')
    st.write('---')
    st.header('Volly Sarung Fase A')
    image=Image.open('volly_sarung_a.png')
    st.image(image,
             use_column_width=True)
    
    st.header('Volly Sarung Fase B')
    image=Image.open('volly_sarung_b.png')
    st.image(image,
             use_column_width=True)
    
    st.header('Volly Sarung Fase C')
    image=Image.open('volly_sarung_c.png')
    st.image(image,
             use_column_width=True)

#BOLA BERACUN
    st.write('---')
    st.title('Klasemen Bola Beracun')
    st.write('---')
    st.header('Bola Beracun A')
    image=Image.open('futsal_a.png')
    st.image(image,
             use_column_width=True)
    
    st.header('Bola Beracun B')
    image=Image.open('futsal_a.png')
    st.image(image,
             use_column_width=True)
    
    st.header('Bola Beracun C')
    image=Image.open('futsal_a.png')
    st.image(image,
             use_column_width=True)

    st.write('---')
    st.title('Klasemen Chopstick Ball')
    st.write('---')
    st.header('Futsal Fase A')
    image=Image.open('futsal_a.png')
    st.image(image,
             use_column_width=True)
