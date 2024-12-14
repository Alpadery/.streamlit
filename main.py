import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu
from streamlit_image_coordinates import streamlit_image_coordinates
from openpyxl import load_workbook

st.set_page_config(page_title='Class Meeting', layout='wide')

image=Image.open('LOGO CM.png')
st.image(image, use_column_width=True)

st.write("""
Dengan penuh rasa syukur, kami mengucapkan terima kasih sebesar-besarnya kepada semua pihak yang telah berpartisipasi dalam Class Meeting 2024. Terima kasih kepada peserta yang telah menunjukkan semangat dan antusiasme luar biasa, serta panitia yang telah bekerja keras untuk memastikan kelancaran acara. Kami juga mengapresiasi semua pihak yang memberikan dukungan dalam berbagai bentuk, baik langsung maupun tidak langsung.

Semoga acara ini tidak hanya sebagai ajang kompetisi dan hiburan, tetapi juga mempererat tali persaudaraan dan kerjasama. Terima kasih atas kontribusi dan partisipasinya. Sampai bertemu di kegiatan selanjutnya!

**TTD**
**Panitia Class Meeting 2024**
         """)
