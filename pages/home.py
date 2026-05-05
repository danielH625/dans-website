import streamlit as st
from st_social_media_links import SocialMediaIcons

st.title("Home")

st.write("Welcome to my portfolio! I'm going to be using this site to keep \
        a list of all my certs, resume, tools, CTF write-ups, etc.")
st.write("This site is consistently being updated and added to. In \
        other words it's still under developement.")
st.write("Feel free to check out my socials below.")


# --- SOCIALS ---
st.divider()

social_media_links = [
    "https://github.com/danielH625",
    "https://www.linkedin.com/in/daniel-herrera14",
    "https://medium.com/@daniel_herrera",
]

social_media_icons = SocialMediaIcons(social_media_links)
social_media_icons.render()
