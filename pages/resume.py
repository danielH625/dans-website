import base64
from pathlib import Path

import streamlit as st

# -- READ PDF FILE AND DISPLAY --
pdf_path = ("assets/Daniel_Herrera_Resume.pdf")

with open(pdf_path, "rb") as f:
  pdf_bytes = f.read()
  base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

# Embed PDF viewer
pdf_display = f"""
<iframe
    src="data:application/pdf;base64,{base64_pdf}"
    width="110%"
    height="900"
    type="application/pdf">
</iframe>
"""
st.markdown(pdf_display, unsafe_allow_html=True)

# -- DOWNLOAD RESUME BUTTON --
st.divider()
st.download_button(label="📥 Download PDF",
                   data=pdf_bytes,
                   file_name="resume.pdf",
                   mime="application/pdf")
