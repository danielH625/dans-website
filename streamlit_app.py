import streamlit as st
from numpy import resize

# --- PAGE SETUP ---
home_page = st.Page(
    page="pages/home.py",
    title="Home",
    icon=":material/home:",
    default=True,
)
about_page = st.Page(
    page="pages/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
)
certification_page = st.Page(
    page="pages/certifications.py",
    title="Certifications",
    icon=":material/workspace_premium:",
)
resume_page = st.Page(page="pages/resume.py", title="My Resume", icon=":material/docs:")

# --- CTF WRITE UP PAGES ---
ncl_fall_2025 = st.Page(
    page="pages/ncl_2025_overview.py",
    title="NCL Fall 2025 Overview",
    icon=":material/contract_edit:",
)

# --- TOOLS ---
projects = st.Page(
    page="pages/projects.py",
    title="Projects/Tools List",
    icon=":material/code:",
)

# --- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation(
    {
        "Welcome": [home_page],
        "Info": [about_page, certification_page, resume_page],
        "CTF-Writeups": [ncl_fall_2025],
        "Projects/Tools": [projects],
    }
)

# --- SHARED ON ALL PAGES ---
st.logo("assets/danilslab_logo.png")
st.sidebar.text("降驤眠啹附鹮ꍥ 😎")

# --- RUN NAVIGATION ---
pg.run()
