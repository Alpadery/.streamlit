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
        options=['Juara Umum Ikhwan','Juara Umum Akhwat'],
        icons=['rocket-takeoff','rocket-takeoff-fill'], 
        menu_icon='cast',
        default_index=0,
    )

sidebar_logo=('Logo Sekolah Islam Abu Dzar-01.png')
main_body_logo=('Icon Logo Yayasan-01 (1).png')
image_path = "LOGO CM.png"  # Replace with your image path or URL
st.sidebar.image(image_path, use_column_width=True)

st.logo(sidebar_logo,
        icon_image='Icon Logo Yayasan-01 (1).png',
        size='large')

if selected == 'Class Meeting 2024':
    st.title('Pusat Informasi Class Meeting Abu Dzar 2024')

    # A. Class Meeting Abu Dzar
    st.header('A. Class Meeting Abu Dzar')
    st.write(
        """
        Class Meeting adalah kegiatan yang diadakan setelah Sumatif Akhir Semester (SAS) untuk memberi kesempatan bagi peserta didik bersenang-senang dan melepas ketegangan pasca-ujian. Kegiatan ini bertujuan mempererat hubungan antar peserta didik dan memupuk semangat baru menghadapi tantangan akademik di semester berikutnya.
        """
    )
    st.write('**Berikut video dokumentasi kegiatan Class Meeting 2023**')
    st.write('[Click Here >](https://www.youtube.com/live/ibEefMmPfrg?si=q_8Ii5MS1T8Kgdeq)')

    # B. Jadwal Kegiatan Class Meeting 2024
    st.header('B. Jadwal Kegiatan Class Meeting 2024')
    image = Image.open('Jadwal CM 24.png')
    st.image(image, use_column_width=True)

    # C. Lomba Class Meeting 2024
    st.header('C. Lomba Class Meeting 2024')
    st.write('Pada kegiatan Class Meeting 2024 terdapat 8 jenis lomba yang akan diikuti oleh siswa berdasarkan kelas dan fasenya masing-masing. Berikut ini adalah daftar lomba dan pesertanya.')
    image = Image.open('lomba CM 24.png')
    st.image(image, use_column_width=True)

    # D. Juara Umum Class Meeting 2024
    st.header('D. Juara Umum Class Meeting 2024')
    st.write('Dalam rangka memeriahkan Class Meeting 2024, akan diadakan perlombaan untuk memperebutkan gelar Juara Umum Kelas Ikhwan dan Juara Umum Kelas Akhwat.')
    st.subheader('Medali Juara Umum Class Meeting 2024')
    image = Image.open('juaraumum.png')
    st.image(image, use_column_width=True)

    # E. Teacher Corner
    st.header('E. Teacher Corner')
    st.write('✨ Kuliner Seru hanya di Class Meeting 2024! ✨')
    st.write('Nikmati hidangan lezat di Teacher Corner: Sosis Bakar, Makaroni Telur, Es Cokelat, Es Krim, dan Lemon Tea.')
    image = Image.open('teachercorner.png')
    st.image(image, use_column_width=True)

    # F. Lokasi Lomba
    st.header('F. Lokasi Lomba')

    # Lapangan Atas
    st.subheader('Lapangan Atas')
    st.write(
        """
        Lapangan atas ini direncanakan untuk digunakan dalam tiga jenis lomba: Basket, Blind Bottle, dan Chopstick Ball.
        """
    )
    image = Image.open('lapangan_atas.png')
    st.image(image, use_column_width=True)

    # Lapangan Bawah
    st.subheader('Lapangan Bawah')
    st.write(
        """
        Lapangan bawah ini digunakan untuk lomba Futsal kelas ikhwan dan lomba Bowling serta Dodgeball untuk kelas akhwat.
        """
    )
    image = Image.open('lapangan_bawah.png')
    st.image(image, use_column_width=True)

    # Lapangan Depan Perpustakaan
    st.subheader('Lapangan Depan Perpustakaan')
    st.write(
        """
        Lapangan ini digunakan untuk lomba Bomb Balloon yang memanfaatkan media air sehingga memerlukan lapangan dari *paving block*.
        """
    )
    image = Image.open('depan_perpus.png')
    st.image(image, use_column_width=True)

    # Basement
    st.subheader('Basement')
    st.write(
        """
        Lokasi basement digunakan untuk lomba Dodgeball kelas ikhwan.
        """
    )
    image = Image.open('basement.png')
    st.image(image, use_column_width=True)


#TTG LOMBA CM
if selected=='Lomba Class Meeting':

    st.title("Lomba Pada Class Meeting Abu Dzar 2024")
    st.write("---")

    selected_lomba = st.selectbox(
    "**Pilih Jenis Lomba**",
    ("Estafet (Fase ABC)","Bomb Balloon (Fase ABC)","Blind Bottle (Fase ABC)","Chopstick Ball (Fase A)","Bowling (Akhwat Fase ABC)","Dodgeball (Fase ABC)","Futsal (Ikhwan Fase ABC)","Basket (Fase BC)"),
    )

    # FUNCTION MENAMPILKAN DISPLAY PENJELASAN LOMBA
    def display_lomba_info(header, image_file, description, rules):
        st.header(header)
        if image_file.endswith('.mp4'):
            video_file = open(image_file, 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)
        else:
            image = Image.open(image_file)
            st.image(image, use_column_width=True)
        st.subheader('**Pengertian Permainan**')
        st.write(description)
        st.subheader('**Peraturan Permainan:**')
        st.markdown(rules)

    # DATA LOMBA
    lomba_data = {
        "Estafet (Fase ABC)": {
            "header": "Estafet",
            "image": 'Estafet.mp4',
            "description": """**Lomba estafet** adalah kompetisi tim di mana peserta menyelesaikan serangkaian rintangan/pos secara bergantian, dengan tim yang tercepat menyelesaikan semua pos sebagai pemenang.""",
            "rules": """
                1. Setiap kelas maksimal mengirimkan satu tim yang terdiri dari 6 siswa untuk fase A dan 7 siswa untuk fase B-C.
                2. Perlombaan terdiri dari lima pos.
                3. Setiap pos terdiri dari :
                    - Pos 1 (Lompat Belalang)
                    Peserta berada di dalam hulahop, kemudian hulahop yang akan digunakan untuk langkah sealnjutnya diambil dengan posisi badan tetap di dalam hulahopnya.
                    - Pos 2 (Balok Berjalan)
                    Peserta menggunakan balok sebagai pijakan untuk berjalan.
                    - Pos 3 (Balap Karung)
                    Peserta meloncat dengan menggunakan karung.
                    - Pos 4 (Halang Rintang)
                    Peserta merayap untuk ikhwan dan jongkok untuk akhwat melawati rintangan tali.
                    - Pos 5
                        - Balon Punggung (Fase A): Berjalan dengan balon berada di kedua punggung peserta menuju garis finish
                        - Sundul Balon (Fase B-C): Peserta berjumlah 3 orang bergantian menyundul balon tanpa jatuh menuju garis finish`
                4. Kelompok yang melewati garis finish pertama dinyatakan sebagai pemenang.
                5. Pemenang dari setiap level akan dipertandingkan di final per fase. Misal pemenang kelas 1 akan dipertandingkan di final melawan pemenang kelas 2.
                6. Setiap fase akan diambil satu pemenang dari ikhwan dan satu pemenang dari akhwat.
            """
        },
        "Futsal (Ikhwan Fase ABC)": {
            "header": "Futsal",
            "image": 'futsal.png',
            "description": """**Futsal** adalah olahraga tim yang merupakan variasi dari sepak bola, dimainkan di lapangan kecil dan biasanya di dalam ruangan. Setiap tim terdiri dari lima pemain, termasuk penjaga gawang. Futsal fokus pada keterampilan teknis, kontrol bola, dan kecepatan.""",
            "rules": """
                1. Jumlah pemain 5 vs 5
                2. Lama waktu pertandingan 8 menit tanpa pindah lapangan
                3. Ketika kick off jika peluit sudah ditiup lalu pemain sudah melewati garis tengah maka permainan sudah dianggap aktif
                4. Setiap Bola clearance dari kiper tidak diperbolehkan melempar lebih dari tengah lapangan.
                5. Pada saat Kick in bola wajib di atas garis sedangkan kaki boleh di luar atau di dalam lapangan
            """
        },
        "Basket (Fase BC)":{
            "header":"Basket",
            "image":'basket.png',
            "description":"""**Basket** adalah olahraga tim yang melibatkan dua tim dengan lima pemain di lapangan masing-masing.
                Tujuan utama dalam permainan basket adalah memasukkan bola ke dalam ring lawan sebanyak-banyaknya.
                Bola dapat dilempar, digiring, atau dioperkan untuk mencapai tujuan tersebut.""",
            "rules":"""
                1. **Lapangan:** Pertandingan basket dimainkan di lapangan berbentuk persegi panjang dengan papan ring di kedua ujungnya.
                2. **Bola:** Bola basket terbuat dari bahan karet atau kulit sintetis dan memiliki ukuran dan berat standar.
                3. **Waktu Pertandingan:** Satu pertandingan biasanya terdiri dari 4 kuarter dengan durasi waktu tertentu (biasanya 10 menit per kuarter).
                4. **Cara Mencetak Poin:** Poin diperoleh ketika bola berhasil dimasukkan ke dalam ring. Nilai poin berbeda tergantung dari jarak lemparan.
                5. **Pelanggaran:** Beberapa pelanggaran umum dalam basket antara lain:
                    - *Foul:* Kontak fisik yang berlebihan terhadap pemain lawan.
                    - *Traveling:* Mengambil langkah lebih dari dua langkah saat menggiring bola.
                    - *Double dribble:* Menggiring bola dua kali berturut-turut.
                    - *Backcourt violation:* Membawa bola melewati garis tengah lapangan ke arah belakang tanpa mengoper bola.
            """
        },
        "Dodgeball (Fase ABC)":{
            "header":"Dodgeball",
            "image":"dodgeballHD.mp4",
            "description":"""**Dodgeball** permainan tim yang melibatkan dua kelompok yang saling berusaha untuk melempar bola dan menghindari bola yang dilempar oleh lawan.
                    Tujuan utama dari permainan ini adalah untuk "mengeluarkan" pemain lawan dengan cara mengenai mereka menggunakan bola sehingga mereka keluar dari lapangan.""",
            "rules":"""
                1. **Jumlah Pemain dan Waktu:** Setiap tim terdiri dari 6 orang dan permainan berlangsung selama 6 menit.
                2. **Formasi:** Kedua tim akan dibagi menjadi 2 bagian saling berhadapan.
                3. **Cara Bermain:**
                    - Bola pertama diletakkan di tengah lapangan, dengan total ada 4 bola.
                    - Pemain yang memegang bola dapat melempar bola ke pemain lawan, dan bola yang jatuh diambil oleh pemain terdekat.
                    - Pemain tidak boleh menahan bola lebih dari 3 detik. Jika melebihi pemain dianggap "out".
                    - Pemain tanpa bola harus menghindar dari lemparan bola lawan.
                    - Pemain yang terkena bola atau keluar lapangan dianggap "out".
                    - Bola yang ditangkap tidak boleh dua kali sentuhan atau ditepis. Lemparan yang melewati garis dianggap tidak sah dan bola diberikan ke lawan.
                4. **Pemenang:**
                    - Jika skor imbang, tim yang tersisa memilih 1 pemain untuk melempar atau menangkap bola. Jika bola tidak tertangkap atau kena tubuh, pemain tersebut kalah.
                    - Jika pemain habis sebelum waktu, tim dengan pemain tersisa menang.
                    - Pemenang adalah tim dengan pemain terbanyak atau skor tertinggi.      
            """
        },
        "Bomb Balloon (Fase ABC)":{
            "header":"Bomb Balloon",
            "image":"bombballon.mp4",
            "description":"""**Lomba Bomb Balloon** ialah sebuah olahraga tim dimana 4 pemain memegang ujung sisi-sisi kain untuk melemparkan balon berisi air ke tim lawan.
                    Terdapat dua metode untuk menentukan pemenang: system waktu dan sistem skor.""",
            "rules":"""
                1. **Tim dan Lapangan:** Setiap tim terdiri dari 4 pemain, bertanding di lapangan persegi panjang (4 x 5 meter) dengan alat permainan berupa kain 4 sisi (1,5 x 1,5 meter) dan balon air.
                2. **Durasi dan Waktu:** Waktu permainan adalah 3 menit, dengan masing-masing tim mendapat 5 balon air per ronde.
                3. **Penentuan Giliran:** Coin flip menentukan tim yang melemparkan balon air pertama kali.
                4. **Poin:**
                    - 1 poin diberikan jika balon pecah di area lapangan lawan (Balloon in).
                    - 1 poin diberikan ke tim lawan jika balon pecah di luar lapangan (Balloon out).
                    - Balon pecah di kain lawan tidak dihitung sebagai poin.
                5. **Pemenang:** Tim yang paling banyak menjatuhkan balon air ke area lawan dalam waktu 3 menit menang. Jika 3 menit belum selesai, tim yang pertama kali memasukkan 5 balon air ke tim lawan dinyatakan menang.
            """
        },
        "Blind Bottle (Fase ABC)":{
            "header":"Blind Bottle",
            "image":'blindbottleHD.mp4',
            "description":"""**Lomba *Blind Bottle*** adalah permainan yang menguji kerja sama tim, komunikasi, dan kepercayaan antar anggota tim.
                    setiap anggota tim diikat dengan tali yang terhubung satu sama lain. Hal ini membuat gerakan setiap anggota tim menjadi saling mempengaruhi dan membutuhkan koordinasi yang lebih tinggi.
                    Satu orang anggota tim ditunjuk sebagai kapten yang akan memberikan instruksi kepada anggota lainnya.
            """,
            "rules":"""
                1. **Pembentukan Tim:** Peserta dibagi menjadi beberapa kelompok, masing-masing terdiri dari 6 orang.
                2. **Penunjukan Kapten:** Setiap kelompok memilih satu orang sebagai kapten.
                3. **Persiapan:** Siapkan botol, paku, dan tali yang cukup panjang untuk mengikat semua anggota tim dalam satu kelompok.
                4. **Pengikatan Tali:** Semua anggota tim diikat dengan tali, membentuk satu kesatuan kecuali kapten.
                5. **Posisi Pemain:** Semua anggota tim kecuali kapten menutup mata/membelakangi botol.
                6. **Instruksi Kapten:** Kapten memberikan instruksi yang sangat detail kepada anggota timnya, seperti arah, jarak, dan teknik yang harus digunakan.
                7. **Waktu:** Waktu pertandingan ± 5 menit per babak, pemenang lanjut ke babak final.
                8. **Pemenang:** Kelompok yang berhasil memasukkan paku ke dalam botol dalam waktu tercepat dinyatakan sebagai pemenang.
            """
        },
        "Chopstick Ball (Fase A)":{
            "header":"Chopstick Ball",
            "image":'chopstickHD.mp4',
            "description":"""**Lomba *chopstick ball*** adalah Permainan yang menguji ketangkasan dan kecepatan peserta dalam mengeluarkan bola dari suatu wadah atau area menggunakan sumpit.
                    Setiap tim terdiri dari 5 orang yang dibekali 2 sumpit. Dalam waktu 5 menit, tim harus bekerja sama untuk mengeluarkan sebanyak mungkin bola.
            """,
            "rules":"""
                1. **Jumlah Peserta dan Waktu:** Lomba dilakukan secara berkelompok, terdiri dari 5 anggota yang bermain chopstick ball. Waktu permainan adalah 5 menit.
                2. **Peralatan:** Setiap peserta diberikan 2 sumpit dan tersedia wadah berlubang yang berisi bola.
                3. **Cara Bermain:** Setiap anggota tim bersama-sama mengeluarkan bola dari wadah menggunakan sumpit.
                4. **Skor:** Skor dihitung dari bola yang keluar, masing-masing 1 poin. Jika skor seri, tim yang tercepat mengeluarkan bola terakhir yang menang.
                5. **Pelanggaran:** Pelanggaran seperti memasukkan tangan atau menggoyang keranjang mengurangi skor 1 poin.
            """
        },
        "Bowling (Akhwat Fase ABC)":{
            "header":"Bowling",
            "image":"bowlingHD.mp4",
            "description":"""**Lomba Bowling** adalah sebuah permainan yang mengadaptasi permainan bowling namun menggunakan botol plastik sebagai pengganti pin bowling. Dalam lomba ini, botol plastik akan diisi pasir atau benda berat lainnya ditempatkan dalam formasi tertentu (seperti segitiga) di ujung jalur permainan, sementara peserta melempar bola untuk mencoba menjatuhkan botol-botol tersebut.
            """,
            "rules":"""
                1. Satu lintasan digunakan oleh 1 kelompok yang beranggotakan 3-5 pemain.
                    - **Babak kualifikasi:** 1 tim terdiri dari 3 orang.
                    - **Babak final:** 1 tim terdiri dari 5 orang.
                2. Pastikan semua pin (botol) bowling berdiri sempurna sebelum melempar bola.
                3. Pemain melempar bola dari jarak atau batas yang sudah ditentukan.
                4. Setiap pemain memiliki 2 kesempatan untuk menjatuhkan semua pin bowling.
                5. Pemain yang menjatuhkan 10 pin pada lemparan pertama (strike) mendapat 20 poin.
                6. Pemain yang menjatuhkan 10 pin dalam 2 lemparan (spare) mendapat 15 poin.
                7. Jika tidak menjatuhkan semua pin setelah 2 lemparan, poin dihitung dari jumlah pin yang jatuh (1 pin = 1 poin).
            """
        }
    }

    # DISPLAY SELECTED LOMBA
    if selected_lomba in lomba_data:
        lomba = lomba_data[selected_lomba]
        display_lomba_info(lomba['header'], lomba['image'], lomba['description'], lomba['rules'])


#LEADERBOARD
if selected=='Juara Umum Ikhwan':
   
    st.title('Juara Umum Ikhwan Class Meeting 2024')
    st.write('---')
    st.subheader('👑 4 Muslim is our Class Meeting 2024 Champion! 👑')
    image=Image.open('4muslim.png')
    st.image(image, use_column_width=True)

    st.write('')
    st.subheader('Statistics', divider='grey')

#LEADERBOARD IKHWAN
    data = {
    'Kelas': ['Muslim','Sufyan Ats Tsaury','Makkah','Firdaus','Al Quds'],
    'Winner': [4,3,2,1,1],
    'Runner Up': [1,0,1,2,1],
    
    }
    leaderboard_df = pd.DataFrame(data)

    leaderboard_df.sort_values(by=['Winner', 'Runner Up'], ascending=False, inplace=True)

    # WARNA TRANSPARAN
    def color_medals(df):
        styles = pd.DataFrame('', index=df.index, columns=df.columns,)
        styles['Winner'] = 'background-color: rgba(255, 215, 0, 0.5)'
        styles['Runner Up'] = 'background-color: rgba(192, 192, 192, 0.5)'
        
        return styles

    # IF ELSE DATA KOSONG
    st.subheader('🎖️ Hasil Perlombaan Ikhwan') 
    if not leaderboard_df.empty:
        # DATA STYLE
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # MAX MIN COLOR
        styled_df = styled_df.highlight_max(color='darkorange', axis=0, subset=['Winner'], props='font-weight: bold; background-color: rgba(255, 140, 0, 0.7);')
        styled_df = styled_df.highlight_max(color='gray', axis=0, subset=['Runner Up'], props='font-weight: bold; background-color: rgba(169, 169, 169, 0.7);')

        st.dataframe(styled_df)
    else:
        st.write(f"The winner will be announced soon, stay tuned!")

    st.write('')

# JUARA FASE IKHWAN
    st.subheader('🏆 Juara Fase Ikhwan Class Meeting 2024')

    juara = {
            'juara fase': ['juarafase_i.png'],
            }

    juarafase_df = pd.DataFrame(juara)
    juarafase_df.sort_values(by=['juara fase'],ascending=False, inplace=True)
    if not juarafase_df.empty:
            image=Image.open('juarafase_i.png')
            st.image(image, use_column_width=True)
    else:
            st.write('*"Competition is not about winning or losing, but about learning and growth"*  **-Brian Herbert**')
            st.write('***will be announced soon**')
            
    st.write("")
    
if selected=='Juara Umum Akhwat':

    st.title('Juara Umum Akhwat Class Meeting 2024')
    #st.write('---')
    #st.subheader('👑 Madinah is our Class Meeting 2024 Champion! 👑')
    #image=Image.open()
    #st.image(image, use_column_width=True)
    #st.write('Selamat kepada kelas 2 Madinah yang berhasil meraih **Juara Umum Ikhwan Class Meeting 2024!**')

    #st.write('')
    #st.subheader('Statistics', divider='grey') 
     
# LEADERBOARD AKHWAT
    data = {
    'Kelas': [],
    'Winner': [],
    'Runner Up': [],
    'Pts':[]
    }
    leaderboard_df = pd.DataFrame(data)

    leaderboard_df.sort_values(by=['Winner', 'Runner Up'], ascending=False, inplace=True)

    # WARNA TRANSPARAN
    def color_medals(df):
        styles = pd.DataFrame('', index=df.index, columns=df.columns)  # Create an empty DataFrame for styles
        styles['Winner'] = 'background-color: rgba(255, 215, 0, 0.5)'  # Gold with 50% transparency
        styles['Runner Up'] = 'background-color: rgba(192, 192, 192, 0.5)'  # Silver with 50% transparency
        styles['Pts'] = 'background-color: rgba(255, 255, 255, 0.5)'  # Silver with 50% transparency
        return styles

    # ELSE IF DATA KOSONG
    st.subheader('🎖️ Hasil Perlombaan Akhwat')
    if not leaderboard_df.empty:
        # DATA STYLE
        styled_df = leaderboard_df.style.apply(color_medals, axis=None)

        # MAX MIN COLOR
        styled_df = styled_df.highlight_max(color='darkorange', axis=0, subset=['Winner'], props='font-weight: bold; background-color: rgba(255, 140, 0, 0.7);')
        styled_df = styled_df.highlight_max(color='gray', axis=0, subset=['Runner Up'], props='font-weight: bold; background-color: rgba(169, 169, 169, 0.7);')

        st.dataframe(styled_df)
    else:
        st.write(f"The winner will be announced soon, stay tuned!")

# JUARA FASE AKHWAT
    st.subheader('🏆 Juara Fase Akhwat Class Meeting 2024')

    juara = {
            'juara fase': [],
            }

    juarafase_df = pd.DataFrame(juara)
    juarafase_df.sort_values(by=['juara fase'],ascending=False, inplace=True)
    if not juarafase_df.empty:
            image=Image.open('juarafase_a.png')
            st.image(image, use_column_width=True)
    else:
            st.write('*"The lessons of competition are lessons for life"*  **-Robert Kennedy**')
            st.write('***will be announced soon**')

if selected=='Pertandingan Ikhwan':
    st.title('Informasi Pertandingan Ikhwan Class Meeting Abu Dzar 2024')
    st.write("---")

    # FILE PATH
    file_path = "Jadwal Ikhwan CM 24 (4).xlsx"  # Change this to your actual file path

    workbook = load_workbook(filename=file_path, data_only=True)

    # MAPPING SHEET
    item_to_sheets = {
        'Estafet': {
            'sheets': ['(Ikhwan) Estafet A','(Ikhwan) Estafet B','(Ikhwan) Estafet C'],
            'link': 'https://docs.google.com/spreadsheets/d/14jFBB5hRJjN9F649mA-EMlpgRJJyY8bFndcDJ5h3Aq4/edit?gid=480333465#gid=480333465'
        },
        'Futsal': {
            'sheets': ['(Ikhwan) Futsal A','(Ikhwan) Futsal B','(Ikhwan) Futsal C'],
            'link': 'https://docs.google.com/spreadsheets/d/14CGLvYdIMOIQy6SY4fMyUjppz7O8HHIin2X_CvHpV4I/edit?gid=462673749#gid=462673749'
        },
        'Basket': {
            'sheets': ['(Ikhwan) Basket B','(Ikhwan) Basket C'],
            'link': 'https://docs.google.com/spreadsheets/d/1L2s6VAZHFIvmWncYNPL-JYopPTiCZBmd3q__LkivXik/edit?gid=1079463361#gid=1079463361'
        },
        'Bomb Balloon': {
            'sheets': ['(Ikhwan) Bomb Ballon A','(Ikhwan) Bomb Ballon B','(Ikhwan) Bomb Ballon C'],
            'link': 'https://docs.google.com/spreadsheets/d/1D75FPSGwDcW60wl9P4xo6iAPDqZiHjJxG01L3LqXYCI/edit?gid=179922245#gid=179922245'
        },
        'Dodgeball': {
            'sheets': ['(Ikhwan) Dodgeball A','(Ikhwan) Dodgeball B','(Ikhwan) Dodgeball C'],
            'link': 'https://docs.google.com/spreadsheets/d/1OVx6YIqnKMKN0JNZrDcnZKF9DQoJN1rxplyZUNQ-pEM/edit?gid=22040083#gid=22040083'
        },
        'Blind Bottle': {
            'sheets': ['(Ikhwan) Blind Bottle A','(Ikhwan) Blind Bottle B','(Ikhwan) Blind Bottle C'],
            'link': 'https://docs.google.com/spreadsheets/d/1EzQDdcBBEJ3NE38g1PlGU_Xy1PDchzLB3ZDeItnGFxM/edit?gid=2055359865#gid=2055359865'
        },
        'Chopstick Ball': {
            'sheets': ['(Ikhwan) Chopstick Ball A'],
            'link': 'https://docs.google.com/spreadsheets/d/1sKSKhvUaPEJXJlcJPkWS5YoNChtz_ebnUALWrJp9JA8/edit?gid=53591745#gid=53591745'
        }
    }

    # SELECT BOX
    selected_item = st.selectbox("Pilih Jenis lomba", list(item_to_sheets.keys()))

    # FUNCTION TO READ THE SHEETS
    def read_sheet(sheet_name):
        sheet = workbook[sheet_name]
        data = [[cell if cell is not None else "" for cell in row] for row in sheet.iter_rows(values_only=True)]
        return pd.DataFrame(data).dropna(how='all')
    
    # DISPLAY THE DATA
    if selected_item:
        related_info = item_to_sheets[selected_item]
        related_sheets = related_info['sheets']
        st.header(f"*Upcoming Match!*")
        st.write("""Temukan informasi lengkap mengenai pertandingan berikutnya beserta jadwal waktunya dengan melihat bagan pertandingan di bawah ini.""")
        
        # LINK
        st.markdown(f"[Lihat Bagan Pertandingan {selected_item}]({related_info['link']})")
        
        st.write("---")
        st.header(f"Klasemen Lomba {selected_item}")
        for sheet in related_sheets:
            df = read_sheet(sheet)
            if not df.empty:  # Only display if DataFrame is not empty
                html = df.to_html(index=False, header=False)
                st.write(f"### {sheet}")  # Display sheet name
                st.markdown(html, unsafe_allow_html=True)

if selected=='Pertandingan Akhwat':
   
    st.title('Informasi Pertandingan Akhwat Class Meeting Abu Dzar 2024')
    st.write("---")

    # FILE PATH
    file_path = "Jadwal Akhwat CM 24 (3).xlsx"  # Change this to your actual file path

    workbook = load_workbook(filename=file_path, data_only=True)

    # MAPPING SHEETS
    item_to_sheets = {
        'Estafet': {
            'sheets': ['(Akhwat) Estafet A','(Akhwat) Estafet B','(Akhwat) Estafet C'],
            'link': 'https://docs.google.com/spreadsheets/d/1lZvbmRRhlxIi6jDoIb1qbShXdm0aElr3FkdOWrIUIzA/edit?gid=254729298#gid=254729298'
        },
        'Bowling': {
            'sheets': ['(Akhwat) Bowling A','(Akhwat) Bowling B','(Akhwat) Bowling C'],
            'link': 'https://docs.google.com/spreadsheets/d/158wkZUdfQc4qdDEmCN24i72mSZCaRHmu__OuL_SoEqM/edit?gid=1986181007#gid=1986181007'
        },
        'Basket': {
            'sheets': ['(Akhwat) Basket B','(Akhwat) Basket C'],
            'link': 'https://docs.google.com/spreadsheets/d/11LAslC-7dGnC5i-rvN6-gbqZJ9dtaOWkMtg1wC4ezqs/edit?gid=488637149#gid=488637149'
        },
        'Bomb Balloon': {
            'sheets': ['(Akhwat) Bomb Ballon A','(Akhwat) Bomb Ballon B','(Akhwat) Bomb Ballon C'],
            'link': 'https://docs.google.com/spreadsheets/d/1rFo1NZCYrW_7z1_MwHIblQ-CmEeOhk2sys-7yVF_RbY/edit?gid=913776429#gid=913776429'
        },
        'Dodgeball': {
            'sheets': ['(Akhwat) Dodgeball A','(Akhwat) Dodgeball B','(Akhwat) Dodgeball C'],
            'link': 'https://docs.google.com/spreadsheets/d/1QEDnT_GEDYMznW0HL84jzyha70B_y51TCqk6qdsOuVw/edit?gid=1154821625#gid=1154821625'
        },
        'Blind Bottle': {
            'sheets': ['(Akhwat) Blind Bottle A','(Akhwat) Blind Bottle B','(Akhwat) Blind Bottle C'],
            'link': 'https://docs.google.com/spreadsheets/d/1CfsasYGmZlWOEST0_X7SiJnBVaePZhqqxrrJZTZ5ZqY/edit?gid=637622410#gid=637622410'
        },
        'Chopstick Ball': {
            'sheets': ['(Akhwat) Chopstick Ball A'],
            'link': 'https://docs.google.com/spreadsheets/d/1WdHYsVbMtU50bHWzQ3XFKeSnQzYRYI0C7kO_Dnd6qf4/edit?gid=1179081002#gid=1179081002'
        }
    }

    # SELECT BOX
    selected_item = st.selectbox("Pilih Jenis lomba", list(item_to_sheets.keys()))

    # FUNCTION TO READ THE SHEETS
    def read_sheet(sheet_name):
        sheet = workbook[sheet_name]
        data = [[cell if cell is not None else "" for cell in row] for row in sheet.iter_rows(values_only=True)]
        return pd.DataFrame(data).dropna(how='all')  # Drop empty rows
    
    # Display related sheets for selected item
    if selected_item:
        related_info = item_to_sheets[selected_item]
        related_sheets = related_info['sheets']
        st.header(f"*Upcoming Match!*")
        st.write("""Temukan informasi lengkap mengenai pertandingan berikutnya beserta jadwal waktunya dengan melihat bagan pertandingan di bawah ini.""")
        
        # LINK
        st.markdown(f"[Lihat Bagan Pertandingan {selected_item}]({related_info['link']})")
        
        st.write("---")
        st.header(f"Klasemen Lomba {selected_item}")
        for sheet in related_sheets:
            df = read_sheet(sheet)
            if not df.empty:  # Only display if DataFrame is not empty
                html = df.to_html(index=False, header=False)
                st.write(f"### {sheet}")  # Display sheet name
                st.markdown(html, unsafe_allow_html=True)
