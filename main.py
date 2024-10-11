import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Class Meeting', layout='wide')

with st.sidebar:
    selected=option_menu(
        menu_title='Class Meeting Abu Dzar',
        options=['Class Meeting 2024','Lomba Class Meeting','Leaderboard','Klasemen Ikhwan','Klasemen Akhwat']
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


#TTG LOMBA CM
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
    
#LEADERBOARD
if selected=='Leaderboard':
    st.title('Leaderboard Class Meeting 2024')
    st.write('---')
    st.subheader('Finalis Class Meeting Abu Dzar 2024/2025')
    with st.popover("Finalis Ikhwan"):
        image=Image.open('finalis_i.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Finalis Akhwat"):
        image=Image.open('finalis_a.png')
        st.image(image,
                  use_column_width=True)
    st.write('---')
    st.subheader('Juara Fase Class Meeting Abu Dzar 2024/2025')
    with st.popover("Juara Fase Ikhwan"):
        image=Image.open('juarafase_i.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Juara Fase Akhwat"):
        image=Image.open('juarafase_a.png')
        st.image(image,
                  use_column_width=True)
    st.write('---')
    st.subheader('Perolehan Medali Class Meeting Abu Dzar 2024/2025')
    with st.popover("Perolehan Medali Ikhwan"):
        image=Image.open('medali_i.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Perolehan Medali Akhwat"):
        image=Image.open('medali_a.png')
        st.image(image,
                  use_column_width=True)


#KLASEMEN IKHWAN
if selected=='Klasemen Ikhwan':
#ESTAFET
    st.write('---')
    st.title('1. Klasemen Estafet')
    st.subheader('Klasemen Lomba Estafet Class Meeting Abu Dzar 2024/2025')
    with st.popover("Klasemen Estafet Fase A"):
        st.header('Estafet Fase A')
        image=Image.open('estafet_a.png')
        st.image(image,
                 use_column_width=True)
    with st.popover("Klasemen Estafet Fase B"):
        st.header('Estafet Fase B')
        image=Image.open('estafet_b.png')
        st.image(image,
                 use_column_width=True)
    with st.popover("Klasemen Estafet Fase C"):
        st.header('Estafet Fase C')
        image=Image.open('estafet_c.png')
        st.image(image,
                 use_column_width=True)
    
#FUTSAL
    st.write('---')
    st.title('2. Klasemen Futsal')
    st.subheader('Klasemen Lomba Futsal Class Meeting Abu Dzar 2024/2025')
    with st.popover("Klasemen Futsal Fase A"):
        st.header('Futsal Fase A')
        image=Image.open('futsal_a.png')
        st.image(image,
                 use_column_width=True)
    with st.popover("Klasemen Futsal Fase B"):
        st.header('Futsal Fase B')
        image=Image.open('futsal_b.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Futsal Fase C"):
        st.header('Futsal Fase C')
        image=Image.open('futsal_c.png')
        st.image(image,
                 use_column_width=True)


#BASKET
    st.write('---')
    st.title('3. Klasemen Basket')
    st.subheader('Klasemen Lomba Basket Class Meeting Abu Dzar 2024/2025')
    with st.popover("Klasemen Basket Fase B"):
        st.header('Basket Fase B')
        image=Image.open('basket_b.png')
        st.image(image,
                  use_column_width=True) 
    with st.popover("Klasemen Basket Fase C"):
        st.header('Basket Fase C')
        image=Image.open('basket_c.png')
        st.image(image,
                  use_column_width=True) 

#BLIND BOTTLE
    st.write('---')
    st.title('4. Klasemen Blind Bottle')
    st.subheader('Klasemen Lomba Blind Bottle Class Meeting Abu Dzar 2024/2025')
    with st.popover("Klasemen Blind Bottle Fase A"):
        st.header('Blind Bottle Fase A')
        image=Image.open('blind_a.png')
        st.image(image,
                 use_column_width=True)
    with st.popover("Klasemen Blind Bottle Fase B"):
        st.header('Blind Bottle Fase B')
        image=Image.open('blind_b.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Blind Bottle Fase C"):
        st.header('Blind Bottle Fase C')
        image=Image.open('blind_c.png')
        st.image(image,
                  use_column_width=True)

#VOLLY SARUNG
    st.write('---')
    st.title('Klasemen Volly Sarung')
    st.subheader('Klasemen Lomba Volly Sarung Class Meeting Abu Dzar 2024/2025')
    with st.popover("Klasemen Volly Sarung Fase A"):
        st.header('Volly Sarung Fase A')
        image=Image.open('volly_a.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Volly Sarung Fase B"):
        st.header('Volly Sarung Fase B')
        image=Image.open('volly_b.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Volly Sarung Fase C"):
        st.header('Volly Sarung Fase C')
        image=Image.open('volly_c.png')
        st.image(image,
                  use_column_width=True)

#BOLA BERACUN
    st.write('---')
    st.title('Klasemen Bola Beracun')
    st.subheader('Klasemen Lomba Bola Beracun Class Meeting Abu Dzar 2024/2025')
    with st.popover("Klasemen Bola Beracun Fase A"):
        st.header('Bola Beracun Fase A')
        image=Image.open('bola_a.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Bola Beracun Fase B"):
        st.header('Bola Beracun Fase B')
        image=Image.open('bola_b.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Bola Beracun Fase C"):
        st.header('Bola Beracun Fase C')
        image=Image.open('bola_c.png')
        st.image(image,
                  use_column_width=True)
    
#Chopstick Ball
    st.write('---')
    st.title('Klasemen Chopstick Ball')
    st.subheader('Klasemen Lomba Chopstick Ball Class Meeting Abu Dzar 2024/2025')
    with st.popover("Klasemen Chopstick Ball Fase A"):
        st.header('Bola Chopstick Ball A')
        image=Image.open('chop_a.png')
        st.image(image,
                  use_column_width=True)


#KLASEMEN AKHWAT
if selected=='Klasemen Akhwat':
#ESTAFET
    st.write('---')
    st.title('1. Klasemen Estafet')
    st.subheader('Klasemen Lomba Estafet Class Meeting Abu Dzar 2024/2025')
    with st.popover("Klasemen Estafet Fase A"):
        st.header('Estafet Fase A')
        image=Image.open('estafet_a.png')
        st.image(image,
                 use_column_width=True)
    with st.popover("Klasemen Estafet Fase B"):
        st.header('Estafet Fase B')
        image=Image.open('estafet_b.png')
        st.image(image,
                 use_column_width=True)
    with st.popover("Klasemen Estafet Fase C"):
        st.header('Estafet Fase C')
        image=Image.open('estafet_c.png')
        st.image(image,
                 use_column_width=True)
    
#FUTSAL
    st.write('---')
    st.title('2. Klasemen Futsal')
    st.subheader('Klasemen Lomba Futsal Class Meeting Abu Dzar 2024/2025')
    with st.popover("Klasemen Futsal Fase A"):
        st.header('Futsal Fase A')
        image=Image.open('futsal_a.png')
        st.image(image,
                 use_column_width=True)
    with st.popover("Klasemen Futsal Fase B"):
        st.header('Futsal Fase B')
        image=Image.open('futsal_b.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Futsal Fase C"):
        st.header('Futsal Fase C')
        image=Image.open('futsal_c.png')
        st.image(image,
                 use_column_width=True)


#BASKET
    st.write('---')
    st.title('3. Klasemen Basket')
    st.subheader('Klasemen Lomba Basket Class Meeting Abu Dzar 2024/2025')
    with st.popover("Klasemen Basket Fase B"):
        st.header('Basket Fase B')
        image=Image.open('basket_b.png')
        st.image(image,
                  use_column_width=True) 
    with st.popover("Klasemen Basket Fase C"):
        st.header('Basket Fase C')
        image=Image.open('basket_c.png')
        st.image(image,
                  use_column_width=True) 

#BLIND BOTTLE
    st.write('---')
    st.title('4. Klasemen Blind Bottle')
    st.subheader('Klasemen Lomba Blind Bottle Class Meeting Abu Dzar 2024/2025')
    with st.popover("Klasemen Blind Bottle Fase A"):
        st.header('Blind Bottle Fase A')
        image=Image.open('blind_a.png')
        st.image(image,
                 use_column_width=True)
    with st.popover("Klasemen Blind Bottle Fase B"):
        st.header('Blind Bottle Fase B')
        image=Image.open('blind_b.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Blind Bottle Fase C"):
        st.header('Blind Bottle Fase C')
        image=Image.open('blind_c.png')
        st.image(image,
                  use_column_width=True)

#VOLLY SARUNG
    st.write('---')
    st.title('Klasemen Volly Sarung')
    st.subheader('Klasemen Lomba Volly Sarung Class Meeting Abu Dzar 2024/2025')
    with st.popover("Klasemen Volly Sarung Fase A"):
        st.header('Volly Sarung Fase A')
        image=Image.open('volly_a.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Volly Sarung Fase B"):
        st.header('Volly Sarung Fase B')
        image=Image.open('volly_b.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Volly Sarung Fase C"):
        st.header('Volly Sarung Fase C')
        image=Image.open('volly_c.png')
        st.image(image,
                  use_column_width=True)

#BOLA BERACUN
    st.write('---')
    st.title('Klasemen Bola Beracun')
    st.subheader('Klasemen Lomba Bola Beracun Class Meeting Abu Dzar 2024/2025')
    with st.popover("Klasemen Bola Beracun Fase A"):
        st.header('Bola Beracun Fase A')
        image=Image.open('bola_a.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Bola Beracun Fase B"):
        st.header('Bola Beracun Fase B')
        image=Image.open('bola_b.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Bola Beracun Fase C"):
        st.header('Bola Beracun Fase C')
        image=Image.open('bola_c.png')
        st.image(image,
                  use_column_width=True)
    
#Chopstick Ball
    st.write('---')
    st.title('Klasemen Chopstick Ball')
    st.subheader('Klasemen Lomba Chopstick Ball Class Meeting Abu Dzar 2024/2025')
    with st.popover("Klasemen Chopstick Ball Fase A"):
        st.header('Bola Chopstick Ball A')
        image=Image.open('chop_a.png')
        st.image(image,
                  use_column_width=True)
