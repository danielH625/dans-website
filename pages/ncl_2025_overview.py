import streamlit as st

st.title("NCL Fall 2025 Overview")
st.write(
    ">NCL prohibits public facing writeups of their challenges. This will be just a general overview along with my score card"
)

st.divider()

# -- GAME OVERVIEW --
st.subheader("Overview")
st.write("""
         The NCL CTF was broken into three phases, Practice Game, Individual Game, and Team Game. All three contained very similar categories such as Open Source Intelligence, Cryptography, Password Cracking, Log Analysis, Network Traffic Analysis, Forensics, Web Exploitation, Scanning and Reconnaissance, and Enumeration and Exploitation. As you progress through the various games, the difficulty increases with the team game being the most challenging.
         """)
st.write("""
         Overall, NCL is a ton of fun; they give you some extremely easy challenges and ones that give you imposter syndrome. I’ve done a handful of CTFs, and this was only the second time I got to play in a team game. Playing in the Team game was a ton of fun and really let me see others' perspective while working through challenges. Also, the ability to collaborate and work together was extremely rewarding.
         """)

st.divider()

# -- INDIVIDUAL SCOUTING REPORT --
st.subheader("Individual Game Scouting Report")
st.write("**Click the button below:**")
st.link_button("Individual Score Report",
               "https://cyberskyline.com/report/85J2L02FKXJ0")

# -- TEAM SCOUTING REPORT --
st.subheader("**Team Game Scouting Report**")
st.write("Click the button below:")
st.link_button("Team Score Report",
               "https://cyberskyline.com/report/7KEUFMEGFHPK")

st.divider()
