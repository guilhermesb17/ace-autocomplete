import streamlit as st
from streamlit_ace import st_ace

lang=st.selectbox('Lingua', ['sql','custom', 'python'])

comp = ['custom1', 'custom2', 'custom3']

ace = st_ace(
    language=lang,
    theme='chrome',
    custom_completers='|valor1|valor2'
)