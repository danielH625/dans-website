import streamlit as st

st.title("My Projects and Tools")
st.divider()

col1, col2 = st.columns([0.2, 0.8])
with col1:
    st.link_button("Hash-Identifier", "https://github.com/danielH625/Hash-Identifier")
    st.link_button("PyChef", "https://github.com/danielH625/PyChef/tree/main")

with col2:
    st.write("CLI tool that can identify hashes individually or from a file.")
    st.write(
        "CLI tool that encodes and decodes various ciphers. (inspired by CyberChef)"
    )
