import streamlit as st

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
         - **Penetration Testing Tools**: Nmap, Burp Suite, Metasploit, Hashcat, JohnTheRipper, CEwl, SQLMap, SMBeagle, SMBClient, FFuF, etc.
         - **Web Security**: Cross-site scripting (XXS), SQL injection, Insecure Direct Object Reference (IDOR), Directory Traversal 
         - **Networking**: Reconnaissance, service enumeration, TCP/IP fundamentals
         - **Scripting & Automation**: Python (basic exploit scripts, log parsing)
         - **Operating Systems & Enviornment**: Kali Linux, Arch Linux, Ubuntu, Windows 10/11, Proxmox/Docker lab deployments
         - TEST
         """)
