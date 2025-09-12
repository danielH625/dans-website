import streamlit as st
from numpy import resize

# --- PAGE SETUP ---
about_page = st.Page(
    page="pages/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
certification_page = st.Page(
    page="pages/certifications.py",
    title="Certifications",
    icon=":material/workspace_premium:",
)
writeup_1_page = st.Page(
    page="pages/test_ctf_writeup.py",
    title="NCL Fall 2025",
    icon=":material/contract_edit:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page])

# --- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation({
    "Info": [about_page, certification_page],
    "CTF-Writeups": [writeup_1_page],
})

# --- SHARED ON ALL PAGES ---
st.logo("assets/danilslab_logo.png")
# st.sidebar.text("Made Mediocre at Best 😎")
st.sidebar.text("降驤眠啹附鹮ꍥ 😎")

# --- RUN NAVIGATION ---
pg.run()
