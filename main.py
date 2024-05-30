import streamlit as st


st.title("Petro Data Software")


st.file_uploader("Uploaded Files", type=[".segy", ".segv", ".sgy"], accept_multiple_files=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
st.button("Upload to Hard drive", key="Hard drive")
st.button("Upload to Cloud", key="Cloud", type="primary")

