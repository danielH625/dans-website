import codecs

import streamlit as st

st.title("PyChef")
st.write("This is a knock off of cyberchef as just a fun personal project.")
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    dcode_ecode = st.radio("Encode or Decode", ["Encode", "Decode"])

with col2:
    encryption_algorithm = st.selectbox(
        "Select algorith:", ["...", "Binary", "Hex", "Base32", "Base64", "Rot13"]
    )

with col3:
    text = st.text_input("Enter text")

st.divider()

if dcode_ecode == "Encode":
    pass

elif dcode_ecode == "Decode":
    pass
