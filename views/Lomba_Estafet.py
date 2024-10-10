import streamlit as st

with st.container():
    st.title("Seputar Lomba Estafet")
    st.write('Lomba estafet adalah')
    
    st.write("---")
    left_column, right_column = st.columns(2)
    st.subheader("Cara Bermain:")
    st.write(
        """
        - a
        - b
        - c
        """)