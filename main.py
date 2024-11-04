import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu
from streamlit_image_coordinates import streamlit_image_coordinates
from openpyxl import load_workbook

st.set_page_config(page_title='Class Meeting', layout='wide')

with st.sidebar:
    selected=option_menu(
        menu_title='Class Meeting Abu Dzar 2024',
        options=['Class Meeting 2024','Lomba Class Meeting','Leaderboard','Bagan Kelas Ikhwan','Bagan Kelas Akhwat'],
        icons=['info-square','journal-bookmark-fill','graph-up','rocket-takeoff','rocket-takeoff-fill'], 
        menu_icon='cast',
        default_index=0,
    )

sidebar_logo=('Logo Sekolah Islam Abu Dzar-01.png')
main_body_logo=('Icon Logo Yayasan-01 (1).png')

st.logo(sidebar_logo,
        icon_image='Icon Logo Yayasan-01 (1).png',
        size='large')

if selected=='Class Meeting 2024':
    with st.container():
        st.title('Pusat Informasi Class Meeting Abu Dzar 2024')
        
        col1, col2 = st.columns((2,1))
        with col1:
            st.header('A.  Class Meeting Abu Dzar', divider='grey')
            st.write(
                """
                Class Meeting merupakan kegiatan yang berlangsung setelah kegiatan Sumatif Akhir Semester dilaksanakan. Kegiatan ini merupakan sebuah *refreshment* untuk peserta didik setelah mengikuti SAS.""")
        
        col1, col2 = st.columns((2.5,1))
        with col1:
            st.header('B.  Tujuan dan Manfaat Class Meeting', divider='grey')
            st.write(
                """
                1. Ajang hiburan dan relaksasi pasca ujian.
                2. Mengembangkan bakat dan minat.
                3. Mempererat hubungan antar siswa.
                4. Mencari bibit prestasi ekstrakulikuler.
                5. Melatih mental dan daya saing.
                6. Memberikan kesempatan berekspresi.
                """)
            
            st.write('**Berikut video dokumentasi kegiatan Class Meeting 2023**')
            st.write('[Click Here >](https://www.youtube.com/live/ibEefMmPfrg?si=q_8Ii5MS1T8Kgdeq)')

        
        col1, col2 = st.columns((2.1,1))
        with col1:
            st.header('C.  Jadwal Kegiatan Class Meeting 2024', divider='grey')
            image=Image.open('JadwalCM.png')
            st.image(image,
                    use_column_width=True)
        
        
        st.header('D. Lokasi Lomba', divider='grey')
        col1, col2 = st.columns((1,1))
        with col1:
            st.subheader('**Lapangan Atas**')
            st.write(
                """
                Lapangan atas ini nantinya akan digunakan untuk 3 jenis lomba dengan jadwal yang berbeda.
                Jadwal pertama digunakan untuk lomba basket, kemudian setelahnya digunakan untuk lomba Blind Bottle dan Chopstick Ball dalam waktu bersamaan.
                """)    

        with col2:
            image=Image.open('lapangan_atas.png')
            st.image(image, use_column_width=True)

        st.write('---')
        col1, col2 = st.columns((1,1))
        with col1:
            st.subheader('**Lapangan Bawah**')
            st.write(
            """
            Lapangan bawah ini digunakan untuk 2 jenis lomba yaitu lomba futsal untuk kelas Ikhwan dan lomba (?) untuk kelas Akhwat.
            Lomba futsal dilaksanakan pada Selasa, 11 Desember 2024 dan Lomba (?) dilaksanakan pada Rabu, 13 Desember 2024.
            """)
        with col2:
            image=Image.open('lapangan_bawah.png')
            st.image(image, use_column_width=True)

        st.write('---')
        col1, col2 = st.columns((1,1))
        with col1:
            st.subheader('**Lapangan Depan Perpustakaan**')
            st.write(
            """
            Lapangan ini adalah tempat untuk lomba Volly Sarung. Lomba ini menggunakan media air sehingga pelaksanaannya perlu berada di daerah yang tidak licin,
            atau lapangan yang terbuat dari *paving block*.
            """)
        with col2:
            image=Image.open('depan_perpus.png')
            st.image(image, use_column_width=True)

#TTG LOMBA CM
if selected=='Lomba Class Meeting':

    st.title("Lomba Pada Class Meeting Abu Dzar 2024")
    st.write("---")

    selected_lomba = st.selectbox(
    "**Pilih Jenis Lomba**",
    ("Estafet","Futsal","Basket","Bola Beracun","Volly Sarung","Blind Bottle","Chopstick Ball"),
)

    #LOMBA ESTAFET
    if selected_lomba == "Estafet":
        st.header('1. Estafet')
        image=Image.open('estafet.png')
        st.image(image, use_column_width=True)
        st.subheader('**Pengertian Permainan Estafet**')
        st.write("""
                Lomba estafet adalah Apa pengertian lari estafet? Lari estafet juga sering disebut dengan lari sambung.
                Oleh karena itu, lari estafet adalah lari yang dilakukan berkelompok. Umumnya bisa berjumlah 2 sampai 4 orang di dalam kelompok.
                Setiap orang di dalam kelompok akan mendapat giliran berakhir.
                """)
        st.subheader('**Peraturan Permainan:**')
        st.markdown(
                """
                1. A
                2. B
                3. C
                """)

    if selected_lomba == "Futsal":
        st.header('2. Futsal')
        image=Image.open('futsal.png')
        st.image(image, use_column_width=True)
        st.subheader('**Pengertian Olahraga Futsal**')
        st.write("""
                **Futsal** adalah olahraga tim yang merupakan variasi dari sepak bola, dimainkan di lapangan kecil dan biasanya di dalam ruangan.
                Setiap tim terdiri dari lima pemain, termasuk penjaga gawang. Futsal fokus pada keterampilan teknis, kontrol bola, dan kecepatan.
                """)
        st.subheader('**Peraturan Permainan:**')
        st.markdown(
                """
                1. **Pemain:** Setiap tim terdiri dari 5 pemain di lapangan, termasuk kiper.
                2. **Waktu:** Pertandingan biasanya berlangsung 2 babak, masing-masing 5 menit.
                3. **Lapangan:** Lebih kecil dari lapangan sepak bola, dengan permukaan keras.
                4. **Bola:** Lebih kecil dan lebih berat dari bola sepak.
                5. **Pelanggaran:** Mirip dengan sepak bola, seperti handball, melanggar, dan sebagainya.
                6. **Tendangan Bebas:** Dilakukan jika terjadi pelanggaran di luar kotak penalti.
                7. **Tendangan Penalti:** Dilakukan jika terjadi pelanggaran di dalam kotak penalti.
                8. **Pergantian Pemain:** Dapat dilakukan kapan saja.
                """)

    if selected_lomba == "Basket":
        st.header('3. Basket')
        image=Image.open('basket.png')
        st.image(image, use_column_width=True)
        st.subheader('**Pengertian Olahraga Basket**')
        st.write("""
                **Basket** adalah olahraga tim yang melibatkan dua tim dengan lima pemain di lapangan masing-masing.
                Tujuan utama dalam permainan basket adalah memasukkan bola ke dalam ring lawan sebanyak-banyaknya.
                Bola dapat dilempar, digiring, atau dioperkan untuk mencapai tujuan tersebut.
                """)
        st.subheader('**Peraturan Permainan:**')
        st.markdown(
                """
                1. **Lapangan:** Pertandingan basket dimainkan di lapangan berbentuk persegi panjang dengan papan ring di kedua ujungnya.
                2. **Bola:** Bola basket terbuat dari bahan karet atau kulit sintetis dan memiliki ukuran dan berat standar.
                3. **Waktu Pertandingan:** Satu pertandingan biasanya terdiri dari 4 kuarter dengan durasi waktu tertentu (biasanya 10 menit per kuarter).
                4. **Cara Mencetak Poin:** Poin diperoleh ketika bola berhasil dimasukkan ke dalam ring. Nilai poin berbeda tergantung dari jarak lemparan.
                5. **Pelanggaran:** Beberapa pelanggaran umum dalam basket antara lain:
                    - *Foul:* Kontak fisik yang berlebihan terhadap pemain lawan.
                    - *Traveling:* Mengambil langkah lebih dari dua langkah saat menggiring bola.
                    - *Double dribble:* Menggiring bola dua kali berturut-turut.
                    - *Backcourt violation:* Membawa bola melewati garis tengah lapangan ke arah belakang tanpa mengoper bola.
                """)
        
    if selected_lomba == "Bola Beracun":
        st.header('4. Bola Beracun')
        image=Image.open('bolaberacun.png')
        st.image(image, use_column_width=True)
        st.subheader('**Pengertian Olahraga Basket**')
        st.write("""
                **Bola beracun** merupakan permainan yang melibatkan dua tim, yaitu tim pelempar dan tim mangsa.
                Tim mangsa berada di dalam lingkaran, sementara tim pelempar berada di luar lingkaran. Tujuan tim pelempar adalah melempar bola ke anggota tim mangsa untuk mengeluarkan mereka dari permainan.
                Sebaliknya, tim mangsa berusaha menghindari lemparan bola dan menjaga agar semua anggota tim tetap berada di dalam lingkaran.
                """)
        st.subheader('**Peraturan Permainan:**')
        st.markdown(
                """
                1. **Jumlah Pemain dan Waktu:** Setiap tim terdiri dari 7 orang dan permainan berlangsung selama 10 menit.
                2. **Formasi:** Tim mangsa membentuk lingkaran yang rapat, sedangkan tim pelempar berada di luar lingkaran.
                3. **Cara Bermain:**
                    - Tim pelempar secara bergantian melempar bola ke arah anggota tim mangsa.
                    - Anggota tim mangsa harus berusaha menghindari lemparan bola.
                    - Jika seorang anggota tim mangsa terkena lemparan bola, ia harus keluar dari permainan.
                    - Permainan akan berhenti jika waktu 10 menit habis atau semua anggota satu tim telah keluar dari permainan.
                4. **Pemenang:**
                    - Jika waktu habis: Tim dengan jumlah anggota terbanyak yang masih berada di dalam lingkaran dinyatakan sebagai pemenang.
                    - Jika semua anggota satu tim keluar: Tim yang berhasil melumpuhkan semua lawan terlebih dahulu dinyatakan sebagai pemenang.
                """)
        
    if selected_lomba == "Volly Sarung":
        st.header('5. Volly Sarung')
        image=Image.open('voli.png')
        st.image(image, use_column_width=True)
        st.subheader('**Pengertian Permainan Volly Sarung**')
        st.write("""
                **Lomba Volly Sarung** adalah yang mirip dengan voli biasa, namun menggunakan sarung sebagai alat untuk melempar balon air yang berisi air.
                Setiap tim terdiri dari 4 orang yang bertugas memegang sudut sarung dan secara bersama-sama melempar balon air ke area lawan.
                """)
        st.subheader('**Peraturan Permainan:**')
        st.markdown(
                """
                1. **Peralatan:** Sarung, balon air, net dan lapangan yang sudah diberikan garis batas.
                2. **Jumlah pemain:** Setiap tim terdiri dari 4 orang.
                3. **Waktu:** Waktu permainan berlangsung selama 10 menit.
                4. **Cara bermain:** Melempar balon air menggunakan sarung.
                5. **Poin:** Dapatkan poin jika balon air jatuh di lapangan lawan.
                6. **Pemenang:** Tim dengan poin terbanyak di akhir permainan dinyatakan sebagai pemenang.
                """)
        
        st.write('[**Contoh Video Permainan Volly Sarung**](https://www.instagram.com/reel/C71Oh-CNZFy/)')

    if selected_lomba == "Blind Bottle":
        st.header('6. Blind Bottle')
        image=Image.open('blindbottle.png')
        st.image(image, use_column_width=True)
        st.subheader('**Pengertian Permainan Blind Bottle**')
        st.write("""
                **Lomba *Blind Bottle*** adalah permainan yang menguji kerja sama tim, komunikasi, dan kepercayaan antar anggota tim.
                setiap anggota tim diikat dengan tali yang terhubung satu sama lain. Hal ini membuat gerakan setiap anggota tim menjadi saling mempengaruhi dan membutuhkan koordinasi yang lebih tinggi.
                Satu orang anggota tim ditunjuk sebagai kapten yang akan memberikan instruksi kepada anggota lainnya.
                """)
        st.subheader('**Peraturan Permainan:**')
        st.markdown(
                """
                1. **Pembentukan Tim:** Peserta dibagi menjadi beberapa kelompok, masing-masing terdiri dari 6 orang.
                2. **Penunjukan Kapten:** Setiap kelompok memilih satu orang sebagai kapten.
                3. **Persiapan:** Siapkan botol, pensil, dan tali yang cukup panjang untuk mengikat semua anggota tim dalam satu kelompok.
                4. **Pengikatan Tali:** Semua anggota tim diikat dengan tali, membentuk satu kesatuan kecuali kapten.
                5. **Posisi Pemain:** Semua anggota tim kecuali kapten menutup mata.
                6. **Instruksi Kapten:** Kapten memberikan instruksi yang sangat detail kepada anggota timnya, seperti arah, jarak, dan teknik yang harus digunakan.
                7. **Waktu:** Berikan waktu 10 menit untuk setiap kelompok menyelesaikan tantangan.
                8. **Pemenang:** Kelompok yang berhasil memasukkan pensil ke dalam botol dalam waktu tercepat dinyatakan sebagai pemenang.
                """)
        
    if selected_lomba == "Chopstick Ball":
        st.header('7. Chopstick Ball')
        image=Image.open('chopstickball.png')
        st.image(image, use_column_width=True)
        st.subheader('**Pengertian Permainan Chopstick Ball**')
        st.write("""
                **Lomba *chopstick ball*** adalah Permainan yang menguji ketangkasan dan kecepatan peserta dalam mengeluarkan bola dari suatu wadah atau area menggunakan sumpit.
                Setiap tim terdiri dari 5 orang, dan setiap peserta dibekali 2 sumpit. Dalam waktu 10 menit, tim harus bekerja sama untuk mengeluarkan sebanyak mungkin bola.
                """)
        st.subheader('**Peraturan Permainan:**')
        st.markdown(
                """
                1. **Jumlah Peserta dan Waktu:** Setiap tim terdiri dari 5 orang dan permainan berlangsung selama 10 menit.
                2. **Peralatan:** Setiap peserta diberikan 2 sumpit dan tersedia wadah berlubang yang berisi bola.
                3. **Cara Bermain:** Setiap anggota tim bersama-sama mengeluarkan bola dari wadah menggunakan sumpit.
                4. **Pemenang:** Tim dengan jumlah bola terbanyak yang berhasil dikeluarkan dalam waktu 10 menit dinyatakan sebagai pemenang.
                """)
    

#LEADERBOARD
if selected=='Leaderboard':
   
    st.title('Leaderboard Class Meeting 2024')
    st.write("---")


#LEADERBOARD IKHWAN
    data = {
    'Kelas': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
    'Gold Medals': [1,2,3,4],
    'Silver Medals': [4,3,2,1]
    }
    leaderboard_df = pd.DataFrame(data)

    leaderboard_df.sort_values(by=['Gold Medals', 'Silver Medals'], ascending=False, inplace=True)

    # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
    def color_medals(df):
        styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
        styles['Gold Medals'] = 'background-color: rgba(255, 215, 0, 0.5)'  # Gold with 50% transparency
        styles['Silver Medals'] = 'background-color: rgba(192, 192, 192, 0.5)'  # Silver with 50% transparency
        return styles

    # Check if the DataFrame is not empty
    st.header('🎖️ Perolehan Medali Ikhwan')
    if not leaderboard_df.empty:
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Highlight the maximum values in the 'Gold Medal' and 'Silver Medal' columns
        styled_df = styled_df.highlight_max(color='darkorange', axis=0, subset=['Gold Medals'], props='font-weight: bold; background-color: rgba(255, 140, 0, 0.7);')
        styled_df = styled_df.highlight_max(color='gray', axis=0, subset=['Silver Medals'], props='font-weight: bold; background-color: rgba(169, 169, 169, 0.7);')

        # Display the styled DataFrame in Streamlit
        st.dataframe(styled_df)
    else:
        st.write(f"The winner will be announced soon, stay tuned!")

    st.write('')


# LEADERBOARD AKHWAT
    data = {
    'Kelas': [],
    'Gold Medals': [],
    'Silver Medals': []
    }

    # Dataframe
    leaderboard_df = pd.DataFrame(data)

    leaderboard_df.sort_values(by=['Gold Medals', 'Silver Medals'], ascending=False, inplace=True)

    # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
    def color_medals(df):
        styles = pd.DataFrame('', index=df.index, columns=df.columns)  # Create an empty DataFrame for styles
        styles['Gold Medals'] = 'background-color: rgba(255, 215, 0, 0.5)'  # Gold with 50% transparency
        styles['Silver Medals'] = 'background-color: rgba(192, 192, 192, 0.5)'  # Silver with 50% transparency
        return styles

    # Check if the DataFrame is not empty
    st.header('🎖️ Perolehan Medali Akhwat')
    if not leaderboard_df.empty:
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Highlight the maximum values in the 'Gold Medal' and 'Silver Medal' columns
        styled_df = styled_df.highlight_max(color='darkorange', axis=0, subset=['Gold Medals'], props='font-weight: bold; background-color: rgba(255, 140, 0, 0.7);')
        styled_df = styled_df.highlight_max(color='gray', axis=0, subset=['Silver Medals'], props='font-weight: bold; background-color: rgba(169, 169, 169, 0.7);')

        # Display the styled DataFrame in Streamlit
        st.dataframe(styled_df)
    else:
        st.write(f"The winner will be announced soon, stay tuned!")


# JUARA FASE IKHWAN
    st.write('---')
    st.header('🏆 Juara Fase Ikhwan Class Meeting 2024')

    juara = {
            'juara fase': [],
            }

    juarafase_df = pd.DataFrame(juara)
    juarafase_df.sort_values(by=['juara fase'],ascending=False, inplace=True)
    if not juarafase_df.empty:
            image=Image.open('juarafase_i.png')
            st.image(image, use_column_width=True)
    else:
            st.write('*"Competition is not about winning or losing, but about learning and growth"*  **-Brian Herbert**')
            
    st.write("")


# JUARA FASE AKHWAT
    st.header('🏆 Juara Fase Akhwat Class Meeting 2024')

    juara = {
            'juara fase': [],
            }

    juarafase_df = pd.DataFrame(juara)
    juarafase_df.sort_values(by=['juara fase'],ascending=False, inplace=True)
    if not juarafase_df.empty:
            image=Image.open('juarafase_i.png')
            st.image(image, use_column_width=True)
    else:
            st.write('*"The lessons of competition are lessons for life"*  **-Robert Kennedy**')

    st.write('---')
    st.header(' Finalis Ikhwan Class Meeting 2024')

    image=Image.open('finalis_i.png')
    st.image(image, use_column_width=True)
        
    st.write("")
        
    st.header('Finalis Akhwat Class Meeting 2024')

    image=Image.open('finalis_i.png')
    st.image(image, use_column_width=True)
    
if selected=='Bagan Kelas Ikhwan':
   
    st.title('Bagan Ikhwan Class Meeting Abu Dzar 2024')
    st.write("---")

    selected_lomba = st.selectbox(
    "**Pilih Jenis Lomba**",
    ("Estafet","Futsal","Basket","Bola Beracun","Volly Sarung","Blind Bottle","Chopstick Ball"),
)

#LOMBA ESTAFET
    if selected_lomba == "Estafet":

#ESTAFET FASE A
#KUALIFIKASI ESTAFET FASE A
        data = {
            'Kelas 1': ['ABU BAKR','UTSMAN','UMAR','ALI BIN ABI THALIB'],
            'Pemenang Kelas 1': ['-','-','-','-'],
            'Kelas 2': ['MAKKAH','ISTANBUL','MADINAH','AL QUDS'],
            'Pemenang Kelas 2': ['-','-','-','-'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Kelas 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Kelas 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Pemenang Kelas 1'] = 'background-color: rgba()'  # Green with 50% transparency
                styles['Pemenang Kelas 2'] = 'background-color: rgba()'  # Green with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Estafet Fase A')
        st.dataframe(styled_df)

#SEMIFINAL ESTAFET FASE A
        data = {
            'Kelas 1': ['Pemenang Level 1'],
            'Vs': ['vs'],
            'Kelas 2': ['Pemenang Level 2'],
            'Pemenang Fase A': ['-'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Kelas 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Kelas 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Pemenang Fase A'] = 'background-color: rgba()'  # Green with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Estafet Fase A')
        st.dataframe(styled_df)

        st.write('---')
#ESTAFET FASE B
#KUALIFIKASI ESTAFET FASE B
        data = {
            'Kelas 3': ['BADR','UHUD','KHAIBAR','TABUK'],
            'Pemenang Kelas 3': ['-','-','-','-'],
            'Kelas 4': ['BUKHORI','MUSLIM','ABU DAWUD','AL BAIHAQI'],
            'Pemenang Kelas 4': ['-','-','-','-'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Kelas 3'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Kelas 4'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Pemenang Kelas 3'] = 'background-color: rgba()'  # Green with 50% transparency
                styles['Pemenang Kelas 4'] = 'background-color: rgba()'  # Green with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Estafet Fase B')
        st.dataframe(styled_df)

#SEMIFINAL ESTAFET FASE B
        data = {
            'Kelas 3': ['Pemenang Level 3'],
            'Vs': ['vs'],
            'Kelas 4': ['Pemenang Level 4'],
            'Pemenang Fase B': ['-'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Kelas 3'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Kelas 4'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Pemenang Fase B'] = 'background-color: rgba()'  # Green with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Estafet Fase B')
        st.dataframe(styled_df)

        st.write('---')
#ESTAFET FASE C
#KUALIFIKASI ESTAFET FASE C
        data = {
            'Kelas 5': ['FIRDAUS',"NA'IM",'DARUSSALAM'],
            'Pemenang Kelas 5': ['-','-','-'],
            'Kelas 6': ['AHMAD BIN HAMBAL','ABU HANIFAH','SUFYAN ATS TSAURY'],
            'Pemenang Kelas 6': ['-','-','-'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Kelas 5'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Kelas 6'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Pemenang Kelas 5'] = 'background-color: rgba()'  # Green with 50% transparency
                styles['Pemenang Kelas 6'] = 'background-color: rgba()'  # Green with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Estafet Fase C')
        st.dataframe(styled_df)

#SEMIFINAL ESTAFET FASE C
        data = {
            'Kelas 5': ['Pemenang Level 5'],
            'Vs': ['vs'],
            'Kelas 6': ['Pemenang Level 6'],
            'Pemenang Fase C': ['-'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Kelas 5'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Kelas 6'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Pemenang Fase C'] = 'background-color: rgba()'  # Green with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Estafet Fase C')
        st.dataframe(styled_df)

        # Link for more information
        st.markdown(f"[Klik untuk melihat bagan lomba Estafet]")


#LOMBA FUTSAL
    if selected_lomba == "Futsal":

#FUTSAL FASE A
#KUALIFIKASI FUTSAL FASE A
        data = {
            'Peserta 1': ['ABU BAKR','UMAR','MAKKAH','MADINAH'],
            '.': [0,0,0,0],
            'SKOR': ['vs','vs','vs','vs'],
            ',': [0,0,0,0],
            'Peserta 2': ['UTSMAN','ALI BIN ABI THALIB','ISTANBUL','AL QUDS'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Futsal Fase A')
        st.dataframe(styled_df)

#SEMIFINAL FUTSAL FASE A
        data = {
            'Peserta 1': ['Level 1','Level 1'],
            '.': [0,0],
            'SKOR': ['vs','vs'],
            ',': [0,0],
            'Peserta 2': ['Level 2','Level 2'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles

        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Futsal Fase A')
        st.dataframe(styled_df)

        st.write('---')
#FUTSAL FASE B
#KUALIFIKASI FUTSAL FASE B
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            '.': [1,3,5,1],
            'SKOR': ['vs','vs','vs','vs'],
            ',': [2,4,6,2],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Green with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Green with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Futsal Fase B')
        st.dataframe(styled_df)

#SEMIFINAL FUTSAL FASE B
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            '.': [1,3],
            'SKOR': ['vs','vs'],
            ',': [2,4],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles

        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Futsal Fase B')
        st.dataframe(styled_df)

        st.write('---')
#FUTSAL FASE C
#KUALIFIKASI FUTSAL FASE C
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            '.': [1,3,5,1],
            'SKOR': ['vs','vs','vs','vs'],
            ',': [2,4,6,2],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Green with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Green with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Futsal Fase C')
        st.dataframe(styled_df)

#SEMIFINAL FUTSAL FASE C
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            '.': [1,3],
            'SKOR': ['vs','vs'],
            ',': [2,4],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles

        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Futsal Fase C')
        st.dataframe(styled_df)

        # Link for more information
        st.markdown(f"[Klik untuk melihat bagan lomba Futsal]")


#LOMBA BASKET
    if selected_lomba == "Basket":

#BASKET FASE B
#KUALIFIKASI BASKET FASE B
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            '.': [1,3,5,1],
            'SKOR': ['vs','vs','vs','vs'],
            ',': [2,4,6,2],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Basket Fase B')
        st.dataframe(styled_df)

#SEMIFINAL BASKET FASE B
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            '.': [1,3],
            'SKOR': ['vs','vs'],
            ',': [2,4],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles

        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Basket Fase B')
        st.dataframe(styled_df)

        st.write('---')
#BASKET FASE C
#KUALIFIKASI BASKET FASE C
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            '.': [1,3,5,1],
            'SKOR': ['vs','vs','vs','vs'],
            ',': [2,4,6,2],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Green with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Green with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Basket Fase C')
        st.dataframe(styled_df)

#SEMIFINAL BASKET FASE C
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            '.': [1,3],
            'SKOR': ['vs','vs'],
            ',': [2,4],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles

        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Basket Fase C')
        st.dataframe(styled_df)

        st.markdown(f"[Klik untuk melihat bagan lomba Basket]")


#LOMBA BOLA BERACUN
    if selected_lomba == "Bola Beracun":

#BOLA BERACUN FASE A
#KUALIFIKASI BOLA BERACUN FASE A
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            '.': [1,3,5,1],
            'SKOR': ['vs','vs','vs','vs'],
            ',': [2,4,6,2],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Bola Beracun Fase A')
        st.dataframe(styled_df)

#SEMIFINAL BOLA BERACUN FASE A
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            '.': [1,3],
            'SKOR': ['vs','vs'],
            ',': [2,4],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles

        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Bola Beracun Fase A')
        st.dataframe(styled_df)

        st.write('---')
#BOLA BERACUN FASE B
#KUALIFIKASI BOLA BERACUN FASE B
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            '.': [1,3,5,1],
            'SKOR': ['vs','vs','vs','vs'],
            ',': [2,4,6,2],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Green with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Green with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Bola Beracun Fase B')
        st.dataframe(styled_df)

#SEMIFINAL BOLA BERACUN FASE B
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            '.': [1,3],
            'SKOR': ['vs','vs'],
            ',': [2,4],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles

        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Bola Beracun Fase B')
        st.dataframe(styled_df)

        st.write('---')
#BOLA BERACUN FASE C
#KUALIFIKASI BOLA BERACUN FASE C
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            '.': [1,3,5,1],
            'SKOR': ['vs','vs','vs','vs'],
            ',': [2,4,6,2],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Green with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Green with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Bola Beracun Fase C')
        st.dataframe(styled_df)

#SEMIFINAL BOLA BERACUN FASE C
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            '.': [1,3],
            'SKOR': ['vs','vs'],
            ',': [2,4],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles

        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Bola Beracun Fase C')
        st.dataframe(styled_df)

        # Link for more information
        st.markdown(f"[Klik untuk melihat bagan lomba Bola Beracun]")


#LOMBA VOLLY SARUNG
    if selected_lomba == "Volly Sarung":

#VOLLY SARUNG FASE A
#KUALIFIKASI VOLLY SARUNG FASE A
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            '.': [1,3,5,1],
            'SKOR': ['vs','vs','vs','vs'],
            ',': [2,4,6,2],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Volly Sarung Fase A')
        st.dataframe(styled_df)

#SEMIFINAL VOLLY SARUNG FASE A
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            '.': [1,3],
            'SKOR': ['vs','vs'],
            ',': [2,4],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles

        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Volly Sarung Fase A')
        st.dataframe(styled_df)

        st.write('---')
#VOLLY SARUNG FASE B
#KUALIFIKASI VOLLY SARUNG FASE B
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            '.': [1,3,5,1],
            'SKOR': ['vs','vs','vs','vs'],
            ',': [2,4,6,2],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Green with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Green with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Volly Sarung Fase B')
        st.dataframe(styled_df)

#SEMIFINAL VOLLY SARUNG FASE B
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            '.': [1,3],
            'SKOR': ['vs','vs'],
            ',': [2,4],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles

        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Volly Sarung Fase B')
        st.dataframe(styled_df)

        st.write('---')
#VOLLY SARUNG FASE C
#KUALIFIKASI VOLLY SARUNG FASE C
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            '.': [1,3,5,1],
            'SKOR': ['vs','vs','vs','vs'],
            ',': [2,4,6,2],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Green with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Green with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Volly Sarung Fase C')
        st.dataframe(styled_df)

#SEMIFINAL VOLLY SARUNG FASE C
        data = {
            'Peserta 1': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            '.': [1,3],
            'SKOR': ['vs','vs'],
            ',': [2,4],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Gold with 50% transparency
                styles['.'] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                styles[','] = 'background-color: rgba(192, 192, 192, 0.2)'  # Silver with 50% transparency
                return styles

        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Volly Sarung Fase C')
        st.dataframe(styled_df)

        # Link for more information
        st.markdown(f"[Klik untuk melihat bagan lomba Volly Sarung]")    


#LOMBA BLIND BOTTLE
    if selected_lomba == "Blind Bottle":

#BLIND BOTTLE FASE A
#KUALIFIKASI BLIND BOTTLE FASE A
        data = {
            'Peserta 1': ['ABU BAKR','UTSMAN','UMAR','ALI BIN ABI THALIB'],
            'Pemenang Peserta 1': ['-','-','-','-'],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            'Pemenang Peserta 2': ['-','-','-','-'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Pemenang Peserta 1'] = 'background-color: rgba()'  # Green with 50% transparency
                styles['Pemenang Peserta 2'] = 'background-color: rgba()'  # Green with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Blind Bottle Fase A')
        st.dataframe(styled_df)

#SEMIFINAL BLIND BOTTLE FASE A
        data = {
            'Peserta 1': ['Pemenang Level 1'],
            'Vs': ['vs'],
            'Peserta 2': ['Pemenang Level 2'],
            'Pemenang Fase A': ['-'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Pemenang Fase A'] = 'background-color: rgba()'  # Green with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Blind Bottle Fase A')
        st.dataframe(styled_df)

        st.write('---')
#BLIND BOTTLE FASE B
#KUALIFIKASI BLIND BOTTLE FASE B
        data = {
            'Peserta 3': ['ABU BAKR','UTSMAN','UMAR','ALI BIN ABI THALIB'],
            'Pemenang Peserta 3': ['-','-','-','-'],
            'Peserta 4': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            'Pemenang Peserta 4': ['-','-','-','-'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 3'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Peserta 4'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Pemenang Peserta 3'] = 'background-color: rgba()'  # Green with 50% transparency
                styles['Pemenang Peserta 4'] = 'background-color: rgba()'  # Green with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Blind Bottle Fase B')
        st.dataframe(styled_df)

#SEMIFINAL BLIND BOTTLE FASE B
        data = {
            'Peserta 3': ['Pemenang Level 3'],
            'Vs': ['vs'],
            'Peserta 4': ['Pemenang Level 4'],
            'Pemenang Fase B': ['-'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 3'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Peserta 4'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Pemenang Fase B'] = 'background-color: rgba()'  # Green with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Blind Bottle Fase B')
        st.dataframe(styled_df)

        st.write('---')
#BLIND BOTTLE FASE C
#KUALIFIKASI BLIND BOTTLE FASE C
        data = {
            'Peserta 5': ['ABU BAKR','UTSMAN','UMAR','ALI BIN ABI THALIB'],
            'Pemenang Peserta 5': ['-','-','-','-'],
            'Peserta 6': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            'Pemenang Peserta 6': ['-','-','-','-'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 5'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Peserta 6'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Pemenang Peserta 5'] = 'background-color: rgba()'  # Green with 50% transparency
                styles['Pemenang Peserta 6'] = 'background-color: rgba()'  # Green with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Blind Bottle Fase C')
        st.dataframe(styled_df)

#SEMIFINAL BLIND BOTTLE FASE C
        data = {
            'Peserta 5': ['Pemenang Level 5'],
            'Vs': ['vs'],
            'Peserta 6': ['Pemenang Level 6'],
            'Pemenang Fase C': ['-'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 5'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Peserta 6'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Pemenang Fase C'] = 'background-color: rgba()'  # Green with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Blind Bottle Fase C')
        st.dataframe(styled_df)

        # Link for more information
        st.markdown(f"[Klik untuk melihat bagan lomba Blind Bottle]")


#LOMBA CHOPSTICK BALL
    if selected_lomba == "Chopstick Ball":

#CHOPSTICK BALL FASE A
#KUALIFIKASI CHOPSTICK BALL FASE A
        data = {
            'Peserta 1': ['ABU BAKR','UTSMAN','UMAR','ALI BIN ABI THALIB'],
            'Pemenang Peserta 1': ['-','-','-','-'],
            'Peserta 2': ['AHMAD BIN HAMBAL','SUFYAN ATS TSAURY','DARUSSALAM','AL BAIHAQI'],
            'Pemenang Peserta 2': ['-','-','-','-'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Pemenang Peserta 1'] = 'background-color: rgba()'  # Green with 50% transparency
                styles['Pemenang Peserta 2'] = 'background-color: rgba()'  # Green with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Kualifikasi Chopstick Ball Fase A')
        st.dataframe(styled_df)

#SEMIFINAL CHOPSTICK BALL FASE A
        data = {
            'Peserta 1': ['Pemenang Level 1'],
            'Vs': ['vs'],
            'Peserta 2': ['Pemenang Level 2'],
            'Pemenang Fase A': ['-'],
            }
        leaderboard_df = pd.DataFrame(data)

        # Function to color entire 'Gold Medal' and 'Silver Medal' columns with transparency
        def color_medals(df):
                styles = pd.DataFrame('', index=df.index, columns=df.columns,)  # Create an empty DataFrame for styles
                styles['Peserta 1'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Peserta 2'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Red with 50% transparency
                styles['Pemenang Fase A'] = 'background-color: rgba()'  # Green with 50% transparency
                return styles
        # Apply the styling to the DataFrame
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # Display the styled DataFrame in Streamlit
        st.subheader('Semifinal Chopstick Ball Fase A')
        st.dataframe(styled_df)

        # Link for more information
        st.markdown(f"[Klik untuk melihat bagan lomba Chopstick Ball]")    



if selected=='Bagan Kelas Akhwat':
   
    st.title('Bagan Akhwat Class Meeting Abu Dzar 2024')
    st.write('---')

    selected_lomba = st.selectbox(
    "**Pilih Jenis Lomba**",
    ("Estafet","Futsal","Basket","Bola Beracun","Volly Sarung","Blind Bottle","Chopstick Ball"),
)

#LOMBA ESTAFET
    if selected_lomba == "Estafet":
        image=Image.open('akhwat/estafet_aa.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/3df0b4a1fe6a62518a64045cbe6e400560f236aba9774a5086084243.png)')
        st.write('')
        st.write('')
        image=Image.open('akhwat/estafet_ba.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/750e4c6e5ba0f825090a4cfc3f3b4b5ebec02aac318c802119a4b3d5.png)')
        st.write('')
        st.write('')
        image=Image.open('akhwat/estafet_ca.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/fa290bfa124e491b55e87cb39b91874888d4f139bfa0642c7168f8cf.png)')

#LOMBA FUTSAL
# PENDING!!!
    if selected_lomba == "Futsal":
        image=Image.open('ikhwan/futsal_a.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/5192ea6f01aab750854566851556e61dca13e65870b219d690c00f3f.png)')
        st.write('')
        st.write('')
        image=Image.open('ikhwan/futsal_b.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/61902a2eef52ec2a77411f4f891b7f17fd237c0d2744eab5afd290b1.png)')
        st.write('')
        st.write('')
        image=Image.open('ikhwan/futsal_c.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/649558a18837335a51e3895f357bc6f5f0470aa395a8ea0410fd56fd.png)')

#LOMBA BASKET  
    if selected_lomba == "Basket":
        image=Image.open('akhwat/basket_ba.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/2dc0e7eb09a9e411ea2a907e0afbbf007c7ce41a5050ffa369abc968.png)')
        st.write('')
        st.write('')
        image=Image.open('akhwat/basket_ca.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/4687f9c909f15add1f1fe53b311307ceb1b608b69b4ad8443dd99b21.png)')

#LOMBA BOLA BERACUN
    if selected_lomba == "Bola Beracun":
        image=Image.open('akhwat/bola_aa.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/7d5c3a42a764bd2d9b3f074b97523281393119f2880b7f0eb86ea4ff.png)')
        st.write('')
        st.write('')
        image=Image.open('akhwat/bola_ba.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/46c15a396effd459e2d71975541fe45c256015ad0ef6587c75b1887c.png)')
        st.write('')
        st.write('')
        image=Image.open('akhwat/bola_ca.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/336c269bd9f71dece24a4b3c7924416d80a7faf1700d4e9c14bc88e2.png)')
    
#LOMBA VOLLY SARUNG  
    if selected_lomba == "Volly Sarung":
        image=Image.open('akhwat/volly_aa.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/16532e7d195d54937a49617e2c87908ecfad58ba41f4b50c5d0046a4.png)')
        st.write('')
        st.write('')
        image=Image.open('akhwat/volly_ba.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/2d388a001972c17ba7dca906f8f926d8a9b2ccf81ca2acde3d7d78e9.png)')
        st.write('')
        st.write('')
        image=Image.open('akhwat/volly_ca.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/7c0844c0531f645da57c1af6c127cb30d67b724b4e82873682b6c6cc.png)')

#LOMBA BLIND BOTTLE
    if selected_lomba == "Blind Bottle":
        image=Image.open('akhwat/blind_aa.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/c02081d7e7dea0fd299a8003bd5323ee62e30dd4a5f8e94b9d3d6ae0.png)')
        st.write('')
        st.write('')
        image=Image.open('akhwat/blind_ba.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/d498d94818ad9ee4f796ebe48e745b2bc69f4feaef2c04de474c6416.png)')
        st.write('')
        st.write('')
        image=Image.open('akhwat/blind_ca.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/5aa89703c314324afcc03f4a4ca7860b37454b017a1a9f4adf7857b3.png)')

#LOMBA CHOPSTICK BALL
    if selected_lomba == "Chopstick Ball":
        image=Image.open('akhwat/chop_aa.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/67cd8b1e2398b770ecb863e8c4917a319cdd0b383b7445b363f99a36.png)')
