import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu
from streamlit_image_coordinates import streamlit_image_coordinates

st.set_page_config(page_title='Class Meeting', layout='wide')

with st.sidebar:
    selected=option_menu(
        menu_title='Class Meeting Abu Dzar 2024',
        options=['Class Meeting 2024','Lomba Class Meeting','Leaderboard','Klasemen Ikhwan','Klasemen Akhwat'],
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
            st.header('A.  Tentang Class Meeting Abu Dzar', divider='grey')
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
            
            st.write('**Berikut hasil dokumentasi kegiatan Class Meeting 2023**')
            st.write('[Click Here >](https://www.youtube.com/live/ibEefMmPfrg?si=q_8Ii5MS1T8Kgdeq)')

        
        col1, col2 = st.columns((2.1,1))
        with col1:
            st.header('C.  Jadwal Kegiatan Class Meeting 2024', divider='grey')
            image=Image.open('jadwal.png')
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
   with st.container():
        st.title('Lomba Pada Kegiatan Class Meeting 2024')
        
        st.header('A. Estafet',divider='grey')
        col1, col2 = st.columns(2)

        with col2:
            st.write("""
            Lomba estafet adalah Apa pengertian lari estafet? Lari estafet juga sering disebut dengan lari sambung.
            Oleh karena itu, lari estafet adalah lari yang dilakukan berkelompok. Umumnya bisa berjumlah 2 sampai 4 orang di dalam kelompok.
            Setiap orang di dalam kelompok akan mendapat giliran berakhir.
            """)
            st.subheader('**Peraturan Permainan:**')
            st.write(
                """
                1. A
                2. B
                3. C
                """)

        
        st.header('B. Futsal',divider='grey')
        col1, col2 = st.columns((1.2,1))

        with col2:
            st.subheader('**Pengertian Olahraga Futsal**')
            st.write("""
            Futsal ialah sebuah permainan bola yang dimainkan oleh dua tim, yang masing-masing timnya memiliki jumlah anggota yakni lima orang.
            Tujuan dari permainan adalah untuk memasukkan bola ke gawang lawan sebanyak, dengan memanipulasi bola dengan kaki. 
            Dalam permainannya, futsal menggunakan media bola sebagai alat permainannya.
            Adapun pertandingan futsal bisa dilakukan di di luar ruangan (outdoor) ataupun di dalam ruangan (indoor).
                """)
        st.subheader('**Peraturan Permainan:**')
        st.markdown(
            """
            1. Bola yang digunakan dalam permainan futsal harus terbuat dari kulit atau bahan sejenisnya (tidak berbahaya).
            2. Jumlah pemain futsal dalam satu tim adalah 5 orang pemain di lapangan dan memiliki 2 pemain cadangan.
            3. Lama waktu bermain adalah 2 x 5 menit.
            4. Pemain diperbolehkan melakukan shooting langsung ke gawang saat kick-off berlangsung.
            5. Dalam olahraga futsal seorang penjaga gawang atau kiper tidak boleh terlalu lama melakukan penguasaan bola.
            6. Jika tendangan sudut tidak dilakukan dalam waktu 4 detik, restart menjadi izin gawang untuk tim lawan.
            7. Tendangan Bebas bisa dilakukan secara langsung atau tidak langsung.
            """)
        
        with col1:
            image=Image.open('futsal.png')
            st.image(image,
            use_column_width=True)

        st.subheader('C. Basket',divider='grey')
        col1, col2 = st.columns((1.2,1))
       
        with col2:
            st.subheader('**Pengertian Olahraga Basket**')
            st.write("""
                Bola basket merupakan salah satu contoh olahraga bola besar.
                Permainan ini berlangsung dengan cara mempertandingkan dua tim basket dan berebut bola untuk dimasukkan ke dalam ring lawan.
                Skor yang didapatkan sangat tergantung dari cara masuknya bola, skor berkisar satu sampai tiga poin.
                """)
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

        with col1:
            image=Image.open('basket.png')
            st.image(image,
            use_column_width=True)

        st.subheader('D. Blind Bottle',divider='grey')
        col1, col2 = st.columns((1.2,1))

        with col2:
            st.subheader('**Pengertian Lomba Blind Bottle**')
            st.write("""
            Lomba *blind bottle* atau lomba memasukkan pensil ke dalam botol dalam keadaan mata tertutup.
            Lomba ini merupakan permainan tim, satu tim terdiri dari 5 orang dengan 1 orang sebagai ketua tim yang bertugas memimpin dan mengarahkan agar pensil bisa masuk ke dalam botol.
            """)
        
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
        
        with col1:
            image=Image.open('blindbottle.png')
            st.image(image,
                use_column_width=True)
        
        st.header('E. Volly Sarung',divider='grey')
        col1, col2 = st.columns((1.2,1))
        
        with col2:
            st.subheader("**Pengertian Lomba Volly Sarung**")
            st.write("""
            Lomba Volly Sarung adalah permainan yang dimainkan oleh dua tim dengan masing-masing tim berjumlah 4 orang dengan menggunakan sarung dan balon air sebagai alat permainannya.
            """)

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

        st.write('[**Klik untuk melihat contoh permainan volly sarung**](https://www.instagram.com/reel/C71Oh-CNZFy/)')

        with col1:
            image=Image.open('voli.png')
            st.image(image,
                use_column_width=True)
            
        st.header('F. Bola Beracun',divider='grey')
        col1, col2 = st.columns((1.2,1))

        with col2:
            st.subheader('**Pengertian Lomba Bola Beracun**')
            st.write("""
            Permainan bola beracun ini dimainkan dalam bentuk kelompok dan mengharuskan setiap pemain berlari untuk menghindari bola yang dilempar oleh pemain lain.
            Jika pemain terkena atau tersentuh oleh bola, maka pemain dianggap "teracuni" dan harus keluar dari permainan.
            """)
        st.subheader('**Peraturan Permainan:**')
        st.write(
                """
                1. Terdapat 2 tim dalam permainan yaitu tim penyerang dan tim mangsa.
                2. Tim penyerang membentuk lingkaran sedangkan tim mangsa berada di tengah-tengah lingkaran.
                3. Tim penyerang melempar bola ke arah tim mangsa dan jika salah satu pemain dari tim mangsa terkena bola, maka harus keluar lingkaran.
                4. Tim penyerang memiliki waktu 10 menit untuk mengeluarkan semua tim mangsa dari dalam lingkaran.
                5. Kemudian kedua tim bertukar posisi
                6. Pemenang ditentukan jika tim berhasil mengeluarkan pemain tim mangsa terbanyak.
                """)

        with col1:
            image=Image.open('bolaberacun.png')
            st.image(image,
                use_column_width=True)

      
        st.header('G. Chopstick Ball',divider='grey')
        col1, col2 = st.columns((1.2,1))

        with col2:
            st.subheader('**Pengertian Lomba Chopstick Ball**')
            st.write('Lomba chopstick ball adalah permainan yang dimainkan ')
        st.subheader('**Peraturan Permainan:**')
        st.write(
                """
                1. A
                2. B
                3. C
                """)
            
        st.write('[**Klik untuk melihat contoh permainan chopstick ball**](https://www.youtube.com/shorts/1QJVuAhYOec?feature=share)')
    
#LEADERBOARD
if selected=='Leaderboard':
   
    st.title('Leaderboard Class Meeting 2024')
    st.write("---")

    #LEADERBOARD IKHWAN
    data = {
        'Kelas': [],
        'Gold Medals': [],
        'Silver Medals': []
    }

    leaderboard_df = pd.DataFrame(data)

    leaderboard_df.sort_values(by=['Gold Medals', 'Silver Medals'], ascending=False, inplace=True)

    def highlight_max_gold(s):
        is_max = s == s.max()
        return ['background-color: gold' if v else '' for v in is_max]

    def highlight_max_silver(s):
        is_max = s == s.max()
        return ['background-color: silver' if v else '' for v in is_max]

    # Display the leaderboard
    st.header("Perolehan Medali Ikhwan")
    if not leaderboard_df.empty:
        styled_table = leaderboard_df.style \
            .apply(highlight_max_gold, subset=['Gold Medals']) \
            .apply(highlight_max_silver, subset=['Silver Medals'])
        
        st.table(styled_table)
    else:
        st.write(f"🏆 The winner will be announced soon 🏆, Stay Tuned!")

    # LEADERBOARD AKHWAT
    data = {
        'Kelas': [],
        'Gold Medals': [],
        'Silver Medals': []
    }

    # Dataframe
    leaderboard_df = pd.DataFrame(data)

    leaderboard_df.sort_values(by=['Gold Medals', 'Silver Medals'], ascending=False, inplace=True)

    def highlight_max_gold(s):
        is_max = s == s.max()
        return ['background-color: gold' if v else '' for v in is_max]

    def highlight_max_silver(s):
        is_max = s == s.max()
        return ['background-color: silver' if v else '' for v in is_max]

    # Display the leaderboard
    st.header("Perolehan Medali Akhwat")
    if not leaderboard_df.empty:
        styled_table = leaderboard_df.style \
            .apply(highlight_max_gold, subset=['Gold Medals']) \
            .apply(highlight_max_silver, subset=['Silver Medals'])
        
        st.table(styled_table)
    else:
        st.write(f"🏆 The winner will be announced soon 🏆, Stay Tuned!")
    st.write("#")

    st.header('Juara Fase Class Meeting 2024', divider='grey')

    image=Image.open('juarafase_i.png')
    st.image(image, use_column_width=True)

    st.write('#')

    st.header('Finalis Class Meeting 2024', divider='grey')

    image=Image.open('finalis_i.png')
    st.image(image, use_column_width=True)
    
    
if selected=='Klasemen Ikhwan':
   
    st.title('Klasemen Ikhwan Class Meeting Abu Dzar 2024')
    st.write("---")

    selected_lomba = st.selectbox(
    "**Pilih Jenis Lomba**",
    ("Estafet","Futsal","Basket","Bola Beracun","Volly Sarung","Blind Bottle","Chopstick Ball"),
)

#LOMBA ESTAFET
    if selected_lomba == "Estafet":
        image=Image.open('ikhwan/estafet_a.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/3df0b4a1fe6a62518a64045cbe6e400560f236aba9774a5086084243.png)')
        st.write('#')
        image=Image.open('ikhwan/estafet_b.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/750e4c6e5ba0f825090a4cfc3f3b4b5ebec02aac318c802119a4b3d5.png)')
        st.write('#')
        image=Image.open('ikhwan/estafet_c.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/fa290bfa124e491b55e87cb39b91874888d4f139bfa0642c7168f8cf.png)')

#LOMBA FUTSAL
    if selected_lomba == "Futsal":
        image=Image.open('ikhwan/futsal_a.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/5192ea6f01aab750854566851556e61dca13e65870b219d690c00f3f.png)')
        st.write('#')
        image=Image.open('ikhwan/futsal_b.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/61902a2eef52ec2a77411f4f891b7f17fd237c0d2744eab5afd290b1.png)')
        st.write('#')
        image=Image.open('ikhwan/futsal_c.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/649558a18837335a51e3895f357bc6f5f0470aa395a8ea0410fd56fd.png)')

#LOMBA BASKET  
    if selected_lomba == "Basket":
        image=Image.open('ikhwan/basket_b.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/2dc0e7eb09a9e411ea2a907e0afbbf007c7ce41a5050ffa369abc968.png)')
        st.write('#')
        image=Image.open('ikhwan/basket_c.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/4687f9c909f15add1f1fe53b311307ceb1b608b69b4ad8443dd99b21.png)')

#LOMBA BOLA BERACUN
    if selected_lomba == "Bola Beracun":
        image=Image.open('ikhwan/bola_a.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/7d5c3a42a764bd2d9b3f074b97523281393119f2880b7f0eb86ea4ff.png)')
        st.write('#')
        image=Image.open('ikhwan/bola_b.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/46c15a396effd459e2d71975541fe45c256015ad0ef6587c75b1887c.png)')
        st.write('#')
        image=Image.open('ikhwan/bola_c.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/336c269bd9f71dece24a4b3c7924416d80a7faf1700d4e9c14bc88e2.png)')
    
#LOMBA VOLLY SARUNG  
    if selected_lomba == "Volly Sarung":
        image=Image.open('ikhwan/volly_a.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/16532e7d195d54937a49617e2c87908ecfad58ba41f4b50c5d0046a4.png)')
        st.write('#')
        image=Image.open('ikhwan/volly_b.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/2d388a001972c17ba7dca906f8f926d8a9b2ccf81ca2acde3d7d78e9.png)')
        st.write('#')
        image=Image.open('ikhwan/volly_c.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/7c0844c0531f645da57c1af6c127cb30d67b724b4e82873682b6c6cc.png)')

#LOMBA BLIND BOTTLE
    if selected_lomba == "Blind Bottle":
        image=Image.open('ikhwan/blind_a.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/c02081d7e7dea0fd299a8003bd5323ee62e30dd4a5f8e94b9d3d6ae0.png)')
        st.write('#')
        image=Image.open('ikhwan/blind_b.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/d498d94818ad9ee4f796ebe48e745b2bc69f4feaef2c04de474c6416.png)')
        st.write('#')
        image=Image.open('ikhwan/blind_c.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/5aa89703c314324afcc03f4a4ca7860b37454b017a1a9f4adf7857b3.png)')

#LOMBA CHOPSTICK BALL
    if selected_lomba == "Chopstick Ball":
        image=Image.open('ikhwan/chop_a.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/67cd8b1e2398b770ecb863e8c4917a319cdd0b383b7445b363f99a36.png)')

if selected=='Klasemen Akhwat':
   
    st.title('Klasemen Akhwat Class Meeting Abu Dzar 2024')
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
        st.write('#')
        image=Image.open('akhwat/estafet_ba.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/750e4c6e5ba0f825090a4cfc3f3b4b5ebec02aac318c802119a4b3d5.png)')
        st.write('#')
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
        st.write('#')
        image=Image.open('ikhwan/futsal_b.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/61902a2eef52ec2a77411f4f891b7f17fd237c0d2744eab5afd290b1.png)')
        st.write('#')
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
        st.write('#')
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
        st.write('#')
        image=Image.open('akhwat/bola_ba.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/46c15a396effd459e2d71975541fe45c256015ad0ef6587c75b1887c.png)')
        st.write('#')
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
        st.write('#')
        image=Image.open('akhwat/volly_ba.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/2d388a001972c17ba7dca906f8f926d8a9b2ccf81ca2acde3d7d78e9.png)')
        st.write('#')
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
        st.write('#')
        image=Image.open('akhwat/blind_ba.png')
        st.image(image,
                    use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/d498d94818ad9ee4f796ebe48e745b2bc69f4feaef2c04de474c6416.png)')
        st.write('#')
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
