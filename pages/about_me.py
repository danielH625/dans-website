import streamlit as st

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/profile_pic.png", width=230)

with col2:
    st.title("Daniel Herrera", anchor=False)
    st.write(
        "U.S. Army Veteran | GIAC-Certified | Digital Forensics & Incident Response"
    )

    if st.button("✉️ Contact Me"):
        show_contact_form()


# --- ABOUT ME ---
st.write("\n")
st.subheader("About Me", anchor=False)

st.write(
    """
    I'm a GIAC-certified cybersecurity professional and U.S. Army veteran
    pursuing a B.S. in Applied Cybersecurity at SANS Technology Institute,
    with a focus on digital forensics, incident response, and computer
    investigations.

    Through advanced SANS coursework, hands-on forensic laboratories,
    and independent projects, I've developed practical experience in
    digital evidence acquisition, Windows artifact examination, memory
    forensics, and reconstructing system and user activity.

    I'm particularly interested in digital forensic examiner and
    investigator roles supporting law enforcement, government agencies,
    and organizations responding to cyber incidents.
    """
)


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)

st.write(
    """
    - **Education:** B.S. in Applied Cybersecurity at SANS Technology
      Institute (in progress); A.S. in Cybersecurity from Hagerstown
      Community College.
    - **GIAC Certifications:** GCFE, GCFA, GCIA, GCIH, GMON, GPYC,
      GSEC, and GFACT. Currently pursuing GBFA.
    - **Forensic Training:** SANS FOR498, FOR500, and FOR508, covering
      evidence acquisition, Windows forensic analysis, memory forensics,
      incident response, and threat hunting.
    - **Professional Experience:** Systems, network, and SharePoint
      administration, including developing AI-assisted cybersecurity
      workflows in an air-gapped environment.
    - **Investigative Projects:** NSA Codebreaker Challenge, National
      Cyber League competitions, and hands-on forensic investigations
      in virtualized lab environments.
    - **Military Background:** U.S. Army infantry veteran with
      experience in reconnaissance, intelligence reporting, and
      handling sensitive operational information.
    """
)


# --- HARD SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)

st.write(
    """
    - **Forensic Acquisition & Preservation:** Forensic imaging,
      live acquisition, RAM collection, write blocking, evidence
      integrity verification, chain of custody, and rapid triage.

    - **Computer Forensics:** Windows Registry, NTFS/MFT, USN Journal,
      Prefetch, Amcache, SRUM, Event Logs, ShellBags, LNK files,
      Jump Lists, browser artifacts, and USB device analysis.

    - **Investigative Analysis:** Memory forensics, timeline
      reconstruction, file carving, deleted data recovery,
      network forensics, intrusion analysis, and malware analysis.

    - **Forensic & DFIR Tools:** Magnet AXIOM/EDD, KAPE, FTK Imager,
      Arsenal Image Mounter, Eric Zimmerman Tools, Autopsy,
      Volatility 3, MemProcFS, Velociraptor, Plaso/log2timeline,
      Wireshark, NetworkMiner, and Binary Ninja.

    - **Cybersecurity & Networking:** Network traffic analysis,
      incident handling, intrusion detection, vulnerability
      assessment, TCP/IP, DNS, and security monitoring.

    - **Systems & Virtualization:** Windows, Linux, Proxmox VE,
      Docker, and isolated forensic laboratory environments.

    - **Programming & Scripting:** Python, Bash, PowerShell, and C.
    """
)
