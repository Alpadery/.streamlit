import streamlit as st

#page setup
about_page = st.page(
    page = "views/about_CM.py",
    title = 'Class Meeting Abu Dzar 2024',
    default = True,
)

project_1_page = st.page(
    page = "views/Lomba_Estafet.py",
    title = "Lomba Estafet",
    icon = '👌',
)

#NAVIGATION SETUP
pg = st.navigation(pages = [about_page, project_1_page])

#RUN NAVIGATION
pg.run()