import streamlit as st
from st_social_media_links import SocialMediaIcons

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
  contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap='small', vertical_alignment='center')
with col1:
  st.image("./assets/profile_pic.png", width=230)
with col2:
  st.title("Daniel Herrera", anchor=False)
  st.write("Army Veteran | Cybersecurity student at SANS.edu.")
  if st.button("✉️ Contact Me"):
    show_contact_form()

# -- ABOUT ME --
st.write("\n")
st.subheader("About Me")
st.write("""
         GIAC-certified cybersecurity student passionate about defense, offense, incident handling, and real-world problem solving. Currently earning a B.S. in Applied Cybersecurity while developing practical skills through CTFs, lab environments, and advanced coursework.
         """)

# --- EXPIRENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write("""
         - Bachelor's student in Applied Cybersecurity at SANS Technology Institute (in progress)
         - Hands-on experience running a home lab with vulnerable machines for practice in exploitation and defense
         - Active participant in Capture the Flag (CTF) competitions in various categories
         - Exposure to penetration testing methodology (reconnaissance, scanning, exploitation, post-exploitation)
         - Passion for cybersecurity and eagerness to learn form real-world security challenges
         """)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write("""
         - **Cybersecurity & Network Analysis**: Network scanning, incident handling, intrusion detection, defense-in-depth, log analysis, network hardening
         - **Tools & Frameworks**: Nmap, Masscan, Wireshark, tcpdump, Metasploit, SQLMap, FFuF, Hashcat, John the Ripper, Responder, Aircrack-ng, RITA/Zeek 
         - **Operating Systems & Environments**: Windows 10/11, Kali Linux, Arch Linux, Ubuntu, Proxmox VE, Docker containers
         - **Programming & Scripting**: Python, Bash, basic PowerShell, basic C
         - **Concepts**: TCP/IP, DNS, cryptography, firewalls, access control, PKI, vulnerability exploitation & mitigation
         """)

# --- SOCIALS ---
st.divider()

social_media_links = [
    "https://github.com/danielH625",
    "https://www.linkedin.com/in/daniel-herrera14"
]

social_media_icons = SocialMediaIcons(social_media_links)
social_media_icons.render()
