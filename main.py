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
    st.write('---')
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
    
    st.write('**Berikut hasil dokumentasi kegiatan Class Meeting 2023**')
    st.write('[Click Here >](https://www.youtube.com/live/ibEefMmPfrg?si=q_8Ii5MS1T8Kgdeq)')

    st.write('---')
    st.header('Jadwal Kegiatan Class Meeting 2024')
    image=Image.open('jadwal.png')
    st.image(image,
             use_column_width=True)


#TTG LOMBA CM
if selected=='Lomba Class Meeting':
    st.title('Lomba Pada Kegiatan Class Meeting 2024')
    st.write('---')
    st.header("*What's new? Keep scrolling!* 🙌")
    st.subheader('A. Estafet')
    st.write("""
    Lomba estafet adalah Apa pengertian lari estafet? Lari estafet juga sering disebut dengan lari sambung.
    Pasalnya, lari estafet dilakukan dengan*Peraturan sambung menyambung.
    Oleh karena itu, lari estafet adalah lari yang dilakukan s*Peraturan berkelompok. Umumnya bisa berjumlah 2 sampai 4 orang di dalam kelompok.
    Setiap orang di dalam kelompok akan mendapat giliran berakhir.
    """)
    st.subheader('**Peraturan Permainan:**')
    st.write(
        """
        1. A
        2. B
        3. C
        """)

    st.write('---')
    st.subheader('**B. Futsal**')
    st.write("""
    Futsal ialah sebuah permainan bola yang dimainkan oleh dua tim, yang masing-masing timnya memiliki jumlah anggota yakni lima orang.
    Tujuan dari permainan adalah untuk memasukkan bola ke gawang lawan sebanyak, dengan memanipulasi bola dengan kaki. 
    Dalam permainannya, futsal menggunakan media bola sebagai alat permainannya.
    Adapun pertandingan futsal bisa dilakukan di di luar ruangan (outdoor) ataupun di dalam ruangan (indoor).
    """)
    image=Image.open('futsal.png')
    st.image(image,
        use_column_width=True)
    st.subheader('**Peraturan Permainan:**')
    st.subheader('**Peraturan Permainan:**')
    st.write(
        """
        1. Bola yang digunakan dalam permainan futsal harus terbuat dari kulit atau bahan sejenisnya (tidak berbahaya).
        2. Jumlah pemain futsal dalam satu tim adalah 5 orang pemain di lapangan dan memiliki 2 pemain cadangan.
        3. Lama waktu bermain adalah 2 x 5 menit.
        4. Pemain diperbolehkan melakukan shooting langsung ke gawang saat kick-off berlangsung.
        5. Dalam olahraga futsal seorang penjaga gawang atau kiper tidak boleh terlalu lama melakukan penguasaan bola.
        6. Jika tendangan sudut tidak dilakukan dalam waktu 4 detik, restart menjadi izin gawang untuk tim lawan.
        7. Tendangan Bebas bisa dilakukan secara langsung atau tidak langsung.
        """)

    st.write('---')
    st.subheader('C. Basket')
    st.write("""
    Bola basket merupakan salah satu contoh olahraga bola besar.
    Permainan ini berlangsung dengan cara mempertandingkan dua tim basket dan berebut bola untuk dimasukkan ke dalam ring lawan.
    Skor yang didapatkan sangat tergantung dari cara masuknya bola, skor berkisar satu sampai tiga poin.
    """)
    image=Image.open('basket.png')
    st.image(image,
        use_column_width=True)
    st.subheader('**Peraturan Permainan:**')
    st.write(
        """
        1. Setiap tim dalam permainan bola basket terdiri dari lima orang pemain ditambah beberapa pemain cadangan.
        2. Bola dapat dilempar ke kedua arah dengan satu atau kedua tangan, tetapi tidak boleh ditinju. Bola harus dipegang di dalam atau di antara telapak tangan.
        3. Permainan dimulai dengan *jump ball* di tengah lapangan. Tim yang mencetak poin terbanyak pada akhir pertandingan dinyatakan sebagai pemenang.
        4. Membawa bola dengan berlari atau berjalan akan dianggap sebagai bentuk pelanggaran. Bola hanya boleh dibawa dengan cara di-dribble.
        5. *Double dribble* tidak diperkenankan. Maksudnya, jika seorang pemain melakukan dribble kemudian berhenti dan memegang bola dengan kedua tangannya, maka pemain tidak diperbolehkan untuk melakukan dribble lagi.
        6. Lama waktu bermain adalah 2 x 5 menit.
        """)
    
    st.write('---')
    st.subheader('D. Blind Bottle')
    st.write("""
    Lomba *blind bottle* atau lomba memasukkan pensil ke dalam botol dalam keadaan mata tertutup.
    Lomba ini merupakan permainan tim, satu tim terdiri dari 5 orang dengan 1 orang sebagai ketua tim yang bertugas memimpin dan mengarahkan agar pensil bisa masuk ke dalam botol.
    """)
    image=Image.open('blindbottle.png')
    st.image(image,
        use_column_width=True)
    st.subheader('**Peraturan Permainan:**')
    st.write(
        """
        1. Lama waktu bermain adalah 10 menit.
        2. Pemain terdiri dari 6 orang dengan 1 orang sebagai kapten.
        3. 5 pemain akan diikat tali pada pinggangnya, kemudian masing-masing tali pada pemain dihubungkan dengan mengikat pensil di tengahnya.
        4. Selama permainan, pemain akan ditutup matanya dan berpindah tempat sesuai perintah kapten tim tersebut.
        5. Kapten mengarahkan timnya agar dapat memasukkan pensil ke dalam botol.
        6. Tim yang berhasil memasukkan pensil tercepat adalah pemenangya.
        """)
    
    
    
    st.write('---')
    st.subheader('E. Voli Sarung')
    st.write("""
    Lomba Voli Sarung adalah permainan yang dimainkan oleh dua tim dengan masing-masing tim berjumlah 4 orang dengan menggunakan sarung dan balon air sebagai alat permainannya.
    """)
    image=Image.open('voli.png')
    st.image(image,
        use_column_width=True)
    st.subheader('**Peraturan Permainan:**')
    st.write(
        """
        1. Lama waktu bermain adalah 10 menit.
        2. Permainan terdiri dari 2 tim dengan setiap tim terdiri dari 4 orang.
        3. Setiap tim diberikan 1 sarung dan ke-4 pemain memegang tiap sudut sarung yang diberikan.
        4. Balon yang berisi air diletakkan disarung dan dilempar ke arah lawan.
        5. Lawan harus berusaha untuk menangkap balon dengan sarung dan dilemparkan kembali ke arah lawan, begitu seterusnya.
        6. Tim mendapatkan poin jika lawan tidak bisa menangkap balon.
        """)

    st.write('---')
    st.subheader('F. Bola Beracun')
    st.write('Lomba bola beracun adalah')
    st.subheader('**Peraturan Permainan:**')
    st.write(
        """
        1. A
        2. B
        3. C
        """)

    st.write('---')
    st.subheader('G. Chopstick Ball')
    st.write('Lomba chopstick ball adalah')
    st.subheader('**Peraturan Permainan:**')
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
    st.subheader('Finalis Class Meeting Abu Dzar 2024')
    with st.popover("Finalis Ikhwan"):
        image=Image.open('finalis_i.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Finalis Akhwat"):
        image=Image.open('finalis_a.png')
        st.image(image,
                  use_column_width=True)
    st.write('---')
    st.subheader('Juara Fase Class Meeting Abu Dzar 2024')
    with st.popover("Juara Fase Ikhwan"):
        image=Image.open('juarafase_i.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Juara Fase Akhwat"):
        image=Image.open('juarafase_a.png')
        st.image(image,
                  use_column_width=True)
    st.write('---')
    st.subheader('Perolehan Medali Class Meeting Abu Dzar 2024')
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
    st.title('Klasemen Ikhwan Class Meeting Abu Dzar 2024')
    st.write('---')
    st.header('1. Klasemen Estafet')
    st.subheader('Klasemen Lomba Estafet Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Estafet Fase A"):
        st.subheader('Estafet Fase A')
        image=Image.open('ikhwan/estafet_a.png')
        st.image(image,
                 use_column_width=True)
    with st.popover("Klasemen Estafet Fase B"):
        st.subheader('Estafet Fase B')
        image=Image.open('ikhwan/estafet_b.png')
        st.image(image,
                 use_column_width=True)
    with st.popover("Klasemen Estafet Fase C"):
        st.subheader('Estafet Fase C')
        image=Image.open('ikhwan/estafet_c.png')
        st.image(image,
                 use_column_width=True)
    
#FUTSAL
    st.write('---')
    st.header('2. Klasemen Futsal')
    st.subheader('Klasemen Lomba Futsal Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Futsal Fase A"):
        st.subheader('Futsal Fase A')
        image=Image.open('ikhwan/futsal_a.png')
        st.image(image,
                 use_column_width=True)
    with st.popover("Klasemen Futsal Fase B"):
        st.subheader('Futsal Fase B')
        image=Image.open('ikhwan/futsal_b.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Futsal Fase C"):
        st.subheader('Futsal Fase C')
        image=Image.open('ikhwan/futsal_c.png')
        st.image(image,
                 use_column_width=True)


#BASKET
    st.write('---')
    st.header('3. Klasemen Basket')
    st.subheader('Klasemen Lomba Basket Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Basket Fase B"):
        st.subheader('Basket Fase B')
        image=Image.open('ikhwan/basket_b.png')
        st.image(image,
                  use_column_width=True) 
    with st.popover("Klasemen Basket Fase C"):
        st.subheader('Basket Fase C')
        image=Image.open('ikhwan/basket_c.png')
        st.image(image,
                  use_column_width=True) 

#BLIND BOTTLE
    st.write('---')
    st.header('4. Klasemen Blind Bottle')
    st.subheader('Klasemen Lomba Blind Bottle Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Blind Bottle Fase A"):
        st.subheader('Blind Bottle Fase A')
        image=Image.open('ikhwan/blind_a.png')
        st.image(image,
                 use_column_width=True)
    with st.popover("Klasemen Blind Bottle Fase B"):
        st.subheader('Blind Bottle Fase B')
        image=Image.open('ikhwan/blind_b.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Blind Bottle Fase C"):
        st.subheader('Blind Bottle Fase C')
        image=Image.open('ikhwan/blind_c.png')
        st.image(image,
                  use_column_width=True)

#VOLLY SARUNG
    st.write('---')
    st.header('5. Klasemen Voli Sarung')
    st.subheader('Klasemen Lomba Voli Sarung Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Voli Sarung Fase A"):
        st.subheader('Voli Sarung Fase A')
        image=Image.open('ikhwan/volly_a.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Voli Sarung Fase B"):
        st.subheader('Voli Sarung Fase B')
        image=Image.open('ikhwan/volly_b.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Voli Sarung Fase C"):
        st.subheader('Voli Sarung Fase C')
        image=Image.open('ikhwan/volly_c.png')
        st.image(image,
                  use_column_width=True)

#BOLA BERACUN
    st.write('---')
    st.header('6. Klasemen Bola Beracun')
    st.subheader('Klasemen Lomba Bola Beracun Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Bola Beracun Fase A"):
        st.subheader('Bola Beracun Fase A')
        image=Image.open('ikhwan/bola_a.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Bola Beracun Fase B"):
        st.subheader('Bola Beracun Fase B')
        image=Image.open('ikhwan/bola_b.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Bola Beracun Fase C"):
        st.subheader('Bola Beracun Fase C')
        image=Image.open('ikhwan/bola_c.png')
        st.image(image,
                  use_column_width=True)
    
#Chopstick Ball
    st.write('---')
    st.header('7. Klasemen Chopstick Ball')
    st.subheader('Klasemen Lomba Chopstick Ball Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Chopstick Ball Fase A"):
        st.subheader('Bola Chopstick Ball A')
        image=Image.open('ikhwan/chop_a.png')
        st.image(image,
                  use_column_width=True)


#KLASEMEN AKHWAT
if selected=='Klasemen Akhwat':
#ESTAFET
    st.title('Klasemen Akhwat Class Meeting Abu Dzar 2024')
    st.write('---')
    st.header('1. Klasemen Estafet')
    st.subheader('Klasemen Lomba Estafet Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Estafet Fase A"):
        st.subheader('Estafet Fase A')
        image=Image.open('ikhwan/estafet_a.png')
        st.image(image,
                 use_column_width=True)
    with st.popover("Klasemen Estafet Fase B"):
        st.subheader('Estafet Fase B')
        image=Image.open('ikhwan/estafet_b.png')
        st.image(image,
                 use_column_width=True)
    with st.popover("Klasemen Estafet Fase C"):
        st.subheader('Estafet Fase C')
        image=Image.open('ikhwan/estafet_c.png')
        st.image(image,
                 use_column_width=True)
    
#FUTSAL
    st.write('---')
    st.header('2. Klasemen Futsal')
    st.subheader('Klasemen Lomba Futsal Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Futsal Fase A"):
        st.subheader('Futsal Fase A')
        image=Image.open('ikhwan/futsal_a.png')
        st.image(image,
                 use_column_width=True)
    with st.popover("Klasemen Futsal Fase B"):
        st.subheader('Futsal Fase B')
        image=Image.open('ikhwan/futsal_b.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Futsal Fase C"):
        st.subheader('Futsal Fase C')
        image=Image.open('ikhwan/futsal_c.png')
        st.image(image,
                 use_column_width=True)


#BASKET
    st.write('---')
    st.header('3. Klasemen Basket')
    st.subheader('Klasemen Lomba Basket Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Basket Fase B"):
        st.subheader('Basket Fase B')
        image=Image.open('ikhwan/basket_b.png')
        st.image(image,
                  use_column_width=True) 
    with st.popover("Klasemen Basket Fase C"):
        st.subheader('Basket Fase C')
        image=Image.open('ikhwan/basket_c.png')
        st.image(image,
                  use_column_width=True) 

#BLIND BOTTLE
    st.write('---')
    st.header('4. Klasemen Blind Bottle')
    st.subheader('Klasemen Lomba Blind Bottle Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Blind Bottle Fase A"):
        st.subheader('Blind Bottle Fase A')
        image=Image.open('ikhwan/blind_a.png')
        st.image(image,
                 use_column_width=True)
    with st.popover("Klasemen Blind Bottle Fase B"):
        st.subheader('Blind Bottle Fase B')
        image=Image.open('ikhwan/blind_b.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Blind Bottle Fase C"):
        st.subheader('Blind Bottle Fase C')
        image=Image.open('ikhwan/blind_c.png')
        st.image(image,
                  use_column_width=True)

#VOLLY SARUNG
    st.write('---')
    st.header('5. Klasemen Voli Sarung')
    st.subheader('Klasemen Lomba Voli Sarung Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Voli Sarung Fase A"):
        st.subheader('Voli Sarung Fase A')
        image=Image.open('ikhwan/volly_a.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Voli Sarung Fase B"):
        st.subheader('Voli Sarung Fase B')
        image=Image.open('ikhwan/volly_b.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Voli Sarung Fase C"):
        st.subheader('Voli Sarung Fase C')
        image=Image.open('ikhwan/volly_c.png')
        st.image(image,
                  use_column_width=True)

#BOLA BERACUN
    st.write('---')
    st.header('6. Klasemen Bola Beracun')
    st.subheader('Klasemen Lomba Bola Beracun Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Bola Beracun Fase A"):
        st.subheader('Bola Beracun Fase A')
        image=Image.open('ikhwan/bola_a.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Bola Beracun Fase B"):
        st.subheader('Bola Beracun Fase B')
        image=Image.open('ikhwan/bola_b.png')
        st.image(image,
                  use_column_width=True)
    with st.popover("Klasemen Bola Beracun Fase C"):
        st.subheader('Bola Beracun Fase C')
        image=Image.open('ikhwan/bola_c.png')
        st.image(image,
                  use_column_width=True)
    
#Chopstick Ball
    st.write('---')
    st.header('7. Klasemen Chopstick Ball')
    st.subheader('Klasemen Lomba Chopstick Ball Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Chopstick Ball Fase A"):
        st.subheader('Bola Chopstick Ball A')
        image=Image.open('ikhwan/chop_a.png')
        st.image(image,
                  use_column_width=True)
