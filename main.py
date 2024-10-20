
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from streamlit_image_coordinates import streamlit_image_coordinates

st.set_page_config(page_title='Class Meeting', layout='wide')

with st.sidebar:
    selected=option_menu(
        menu_title='Class Meeting Abu Dzar 2024',
        options=['Class Meeting 2024','Lomba Class Meeting','Leaderboard','Klasemen Ikhwan (1)','Klasemen Ikhwan','Klasemen Akhwat'],
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
    st.title('Pusat Informasi Class Meeting Abu Dzar 2024')
    st.write('---')
    col1, col2 = st.columns((2,1))
    with col1:
        st.header('Tentang Class Meeting Abu Dzar')
        st.write(
            """
            Class Meeting merupakan kegiatan yang berlangsung setelah kegiatan Sumatif Akhir Semester dilaksanakan. Kegiatan ini merupakan sebuah *refreshment* untuk peserta didik setelah mengikuti SAS.""")
        
    st.write('---')
    col1, col2 = st.columns((2.5,1))
    with col1:
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
    col1, col2 = st.columns((2.1,1))
    with col1:
        st.header('Jadwal Kegiatan Class Meeting 2024')
        image=Image.open('jadwal.png')
        st.image(image,
                use_column_width=True)

#TTG LOMBA CM
if selected=='Lomba Class Meeting':
   with st.container():
        st.title('Lomba Pada Kegiatan Class Meeting 2024')
        st.write('---')
        col1, col2 = st.columns(2)

        with col1:
            st.header("*What's new? Keep scrolling!* 🙌")
            st.subheader('A. Estafet')
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

        st.write('---')
        col1, col2 = st.columns((1.2,1))

        with col1:
            st.subheader('B. Futsal')
            st.write("""
            Futsal ialah sebuah permainan bola yang dimainkan oleh dua tim, yang masing-masing timnya memiliki jumlah anggota yakni lima orang.
            Tujuan dari permainan adalah untuk memasukkan bola ke gawang lawan sebanyak, dengan memanipulasi bola dengan kaki. 
            Dalam permainannya, futsal menggunakan media bola sebagai alat permainannya.
            Adapun pertandingan futsal bisa dilakukan di di luar ruangan (outdoor) ataupun di dalam ruangan (indoor).
                """)
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
        
        with col2:
            image=Image.open('futsal.png')
            st.image(image,
            use_column_width=True)

        st.write('---')
        col1, col2 = st.columns((1.2,1))
       
        with col1:
            st.subheader('C. Basket')
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

        with col2:
            image=Image.open('basket.png')
            st.image(image,
            use_column_width=True)

        st.write('---')
        col1, col2 = st.columns((1.2,1))

        with col1:
            st.subheader('D. Blind Bottle')
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
        
        with col2:
            image=Image.open('blindbottle.png')
            st.image(image,
                use_column_width=True)
        
        st.write('---')
        col1, col2 = st.columns((1.2,1))
        
        with col1:
            st.subheader('E. Volly Sarung')
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

        with col2:
            image=Image.open('voli.png')
            st.image(image,
                use_column_width=True)
            

        st.write('---')
        col1, col2 = st.columns((1.2,1))

        with col1:
            st.subheader('F. Bola Beracun')
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

        with col2:
            image=Image.open('bolaberacun.png')
            st.image(image,
                use_column_width=True)

        st.write('---')
        col1, col2 = st.columns((1.2,1))

        with col1:
            st.subheader('G. Chopstick Ball')
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
    col1, col2 = st.columns(2)

    with col1:
        st.write('---')
        st.subheader('Finalis Class Meeting Abu Dzar 2024')
        with st.popover("Finalis Ikhwan"):
            image=Image.open('finalis_a.png')
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


if selected=='Klasemen Ikhwan (1)':
   
    st.title('Klasemen Ikhwan Class Meeting Abu Dzar 2024')

    # Dictionary to hold image file paths and titles
    image_dict = {
        "Estafet": ["estafet_a.png","estafet_b.png","estafet_c.png"],
        "Futsal": ["futsal_a.png","futsal_b.png","futsal_c.png"],
        "Basket": ["basket_b.png","basket_c.png"],
        "Volly Sarung": ["volly_a.png","volly_b.png","volly_c.png"],
        "Blind Bottle": ["blind_a.png","blind_b.png","blind_c.png"],
        "Bola Beracun": ["bola_a.png","bola_b.png","bola_c.png"],
        "Chopstick Ball": ["chop_a.png"]
    }

    # Create a select box for the user to choose an image
    selected_image = st.selectbox("Pilih Jenis Lomba:", list(image_dict.keys()))

    if selected_image:
        st.write(f"Klasemen {selected_image.capitalize()}:")
    for image in image_dict[selected_image]:
        st.image(image, caption=image , use_column_width=True)

#KLASEMEN IKHWAN
if selected=='Klasemen Ikhwan':
   
    st.title('Klasemen Ikhwan Class Meeting Abu Dzar 2024')

#ESTAFET
    st.write('---')
    st.header('1. Klasemen Estafet')
    st.subheader('Klasemen Lomba Estafet Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Estafet Fase A"):
        st.subheader('Estafet Fase A')
        image=Image.open('ikhwan/estafet_a.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/3df0b4a1fe6a62518a64045cbe6e400560f236aba9774a5086084243.png)')
    with st.popover("Klasemen Estafet Fase B"):
        st.subheader('Estafet Fase B')
        image=Image.open('ikhwan/estafet_b.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/750e4c6e5ba0f825090a4cfc3f3b4b5ebec02aac318c802119a4b3d5.png)')
    with st.popover("Klasemen Estafet Fase C"):
        st.subheader('Estafet Fase C')
        image=Image.open('ikhwan/estafet_c.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/fa290bfa124e491b55e87cb39b91874888d4f139bfa0642c7168f8cf.png)')
        
    #FUTSAL
    st.write('---')
    st.header('2. Klasemen Futsal')
    st.subheader('Klasemen Lomba Futsal Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Futsal Fase A"):
        st.subheader('Futsal Fase A')
        image=Image.open('ikhwan/futsal_a.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/5192ea6f01aab750854566851556e61dca13e65870b219d690c00f3f.png)')
    with st.popover("Klasemen Futsal Fase B"):
        st.subheader('Futsal Fase B')
        image=Image.open('ikhwan/futsal_b.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/61902a2eef52ec2a77411f4f891b7f17fd237c0d2744eab5afd290b1.png)')
    with st.popover("Klasemen Futsal Fase C"):
        st.subheader('Futsal Fase C')
        image=Image.open('ikhwan/futsal_c.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/649558a18837335a51e3895f357bc6f5f0470aa395a8ea0410fd56fd.png)')


    #BASKET
    st.write('---')
    st.header('3. Klasemen Basket')
    st.subheader('Klasemen Lomba Basket Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Basket Fase B"):
        st.subheader('Basket Fase B')
        image=Image.open('ikhwan/basket_b.png')
        st.image(image,
                use_column_width=True) 
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/2dc0e7eb09a9e411ea2a907e0afbbf007c7ce41a5050ffa369abc968.png)')
    with st.popover("Klasemen Basket Fase C"):
        st.subheader('Basket Fase C')
        image=Image.open('ikhwan/basket_c.png')
        st.image(image,
                use_column_width=True) 
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/4687f9c909f15add1f1fe53b311307ceb1b608b69b4ad8443dd99b21.png)')

    #BLIND BOTTLE
    st.write('---')
    st.header('4. Klasemen Blind Bottle')
    st.subheader('Klasemen Lomba Blind Bottle Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Blind Bottle Fase A"):
        st.subheader('Blind Bottle Fase A')
        image=Image.open('ikhwan/blind_a.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/c02081d7e7dea0fd299a8003bd5323ee62e30dd4a5f8e94b9d3d6ae0.png)')
    with st.popover("Klasemen Blind Bottle Fase B"):
        st.subheader('Blind Bottle Fase B')
        image=Image.open('ikhwan/blind_b.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/d498d94818ad9ee4f796ebe48e745b2bc69f4feaef2c04de474c6416.png)')
    with st.popover("Klasemen Blind Bottle Fase C"):
        st.subheader('Blind Bottle Fase C')
        image=Image.open('ikhwan/blind_c.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/5aa89703c314324afcc03f4a4ca7860b37454b017a1a9f4adf7857b3.png)')

    #VOLLY SARUNG
    st.write('---')
    st.header('5. Klasemen Volly Sarung')
    st.subheader('Klasemen Lomba Volly Sarung Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Volly Sarung Fase A"):
        st.subheader('Volly Sarung Fase A')
        image=Image.open('ikhwan/volly_a.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/16532e7d195d54937a49617e2c87908ecfad58ba41f4b50c5d0046a4.png)')
    with st.popover("Klasemen Volly Sarung Fase B"):
        st.subheader('Volly Sarung Fase B')
        image=Image.open('ikhwan/volly_b.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/2d388a001972c17ba7dca906f8f926d8a9b2ccf81ca2acde3d7d78e9.png)')
    with st.popover("Klasemen Volly Sarung Fase C"):
        st.subheader('Volly Sarung Fase C')
        image=Image.open('ikhwan/volly_c.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/7c0844c0531f645da57c1af6c127cb30d67b724b4e82873682b6c6cc.png)')

    #BOLA BERACUN
    st.write('---')
    st.header('6. Klasemen Bola Beracun')
    st.subheader('Klasemen Lomba Bola Beracun Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Bola Beracun Fase A"):
        st.subheader('Bola Beracun Fase A')
        image=Image.open('ikhwan/bola_a.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/7d5c3a42a764bd2d9b3f074b97523281393119f2880b7f0eb86ea4ff.png)')
    with st.popover("Klasemen Bola Beracun Fase B"):
        st.subheader('Bola Beracun Fase B')
        image=Image.open('ikhwan/bola_b.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/46c15a396effd459e2d71975541fe45c256015ad0ef6587c75b1887c.png)')
    with st.popover("Klasemen Bola Beracun Fase C"):
        st.subheader('Bola Beracun Fase C')
        image=Image.open('ikhwan/bola_c.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/336c269bd9f71dece24a4b3c7924416d80a7faf1700d4e9c14bc88e2.png)')
        
    #Chopstick Ball
    st.write('---')
    st.header('7. Klasemen Chopstick Ball')
    st.subheader('Klasemen Lomba Chopstick Ball Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Chopstick Ball Fase A"):
        st.subheader('Bola Chopstick Ball A')
        image=Image.open('ikhwan/chop_a.png')
        st.image(image,
                   use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/67cd8b1e2398b770ecb863e8c4917a319cdd0b383b7445b363f99a36.png)')


#KLASEMEN AKHWAT
if selected=='Klasemen Akhwat':
#ESTAFET
    st.title('Klasemen Akhwat Class Meeting Abu Dzar 2024')
    
    st.write('---')
    st.header('1. Klasemen Estafet')
    st.subheader('Klasemen Lomba Estafet Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Estafet Fase A"):
            st.subheader('Estafet Fase A')
            image=Image.open('akhwat/estafet_aa.png')
            st.image(image,
                    use_column_width=True)
            st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')
    with st.popover("Klasemen Estafet Fase B"):
            st.subheader('Estafet Fase B')
            image=Image.open('akhwat/estafet_ba.png')
            st.image(image,
                    use_column_width=True)
            st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')
    with st.popover("Klasemen Estafet Fase C"):
            st.subheader('Estafet Fase C')
            image=Image.open('akhwat/estafet_ca.png')
            st.image(image,
                    use_column_width=True)
            st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')
        
    #FUTSAL
    st.write('---')
    st.header('2. Klasemen Futsal')
    st.subheader('Klasemen Lomba Futsal Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Futsal Fase A"):
        st.subheader('Futsal Fase A')
        image=Image.open('ikhwan/futsal_a.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')
    with st.popover("Klasemen Futsal Fase B"):
        st.subheader('Futsal Fase B')
        image=Image.open('ikhwan/futsal_b.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')
    with st.popover("Klasemen Futsal Fase C"):
        st.subheader('Futsal Fase C')
        image=Image.open('ikhwan/futsal_c.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')


    #BASKET
    st.write('---')
    st.header('3. Klasemen Basket')
    st.subheader('Klasemen Lomba Basket Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Basket Fase B"):
        st.subheader('Basket Fase B')
        image=Image.open('akhwat/basket_ba.png')
        st.image(image,
                use_column_width=True) 
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')
    with st.popover("Klasemen Basket Fase C"):
        st.subheader('Basket Fase C')
        image=Image.open('akhwat/basket_ca.png')
        st.image(image,
                use_column_width=True) 
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')

    #BLIND BOTTLE
    st.write('---')
    st.header('4. Klasemen Blind Bottle')
    st.subheader('Klasemen Lomba Blind Bottle Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Blind Bottle Fase A"):
        st.subheader('Blind Bottle Fase A')
        image=Image.open('akhwat/blind_aa.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')
    with st.popover("Klasemen Blind Bottle Fase B"):
        st.subheader('Blind Bottle Fase B')
        image=Image.open('akhwat/blind_ba.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')
    with st.popover("Klasemen Blind Bottle Fase C"):
        st.subheader('Blind Bottle Fase C')
        image=Image.open('akhwat/blind_ca.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')

    #VOLLY SARUNG
    st.write('---')
    st.header('5. Klasemen Volly Sarung')
    st.subheader('Klasemen Lomba Volly Sarung Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Volly Sarung Fase A"):
        st.subheader('Volly Sarung Fase A')
        image=Image.open('akhwat/volly_aa.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')
    with st.popover("Klasemen Volly Sarung Fase B"):
        st.subheader('Volly Sarung Fase B')
        image=Image.open('akhwat/volly_ba.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')
    with st.popover("Klasemen Volly Sarung Fase C"):
        st.subheader('Volly Sarung Fase C')
        image=Image.open('akhwat/volly_ca.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')

    #BOLA BERACUN
    st.write('---')
    st.header('6. Klasemen Bola Beracun')
    st.subheader('Klasemen Lomba Bola Beracun Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Bola Beracun Fase A"):
        st.subheader('Bola Beracun Fase A')
        image=Image.open('akhwat/bola_aa.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')
    with st.popover("Klasemen Bola Beracun Fase B"):
        st.subheader('Bola Beracun Fase B')
        image=Image.open('akhwat/bola_ba.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')
    with st.popover("Klasemen Bola Beracun Fase C"):
        st.subheader('Bola Beracun Fase C')
        image=Image.open('akhwat/bola_ca.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')
        
    #Chopstick Ball
    st.write('---')
    st.header('7. Klasemen Chopstick Ball')
    st.subheader('Klasemen Lomba Chopstick Ball Class Meeting Abu Dzar 2024')
    with st.popover("Klasemen Chopstick Ball Fase A"):
        st.subheader('Bola Chopstick Ball A')
        image=Image.open('akhwat/chop_aa.png')
        st.image(image,
                use_column_width=True)
        st.write('[Click to Preview>](https://class-meeting.streamlit.app/~/+/media/805bd8e79afe12773ae80034ed4f1a133036de44b2b75ead2f69ec90.png)')
