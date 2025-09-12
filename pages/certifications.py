from types import new_class

import streamlit as st
import streamlit.components.v1 as components
from numpy import test

# --- BADGE HTML LINKS ---

gfact_html = """
<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="3077ffe2-f0fa-4c8b-bf3b-eb6612c9fccd" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
"""

gsec_html = """
<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="d1e17ec8-9ab7-47a2-9db1-31f88e45a4ae" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
"""

gcih_html = """
<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="437aaf1b-28a8-4533-b177-06dfe9714c15" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
"""

advisory_html = """
<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="b219444d-2a56-4a51-8e39-bbb621cf9dcb" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
"""

us_cyber_html = """
<blockquote class="badgr-badge" style="font-family: Helvetica, Roboto, &quot;Segoe UI&quot;, Calibri, sans-serif;"><a href="https://badgr.com/public/assertions/BqzhC6MFReWtVFdLvu1pqQ"><img width="120px" height="120px" src="https://api.badgr.io/public/assertions/BqzhC6MFReWtVFdLvu1pqQ/image"></a><p class="badgr-badge-name" style="hyphens: auto; overflow-wrap: break-word; word-wrap: break-word; margin: 0; font-size: 16px; font-weight: 600; font-style: normal; font-stretch: normal; line-height: 1.25; letter-spacing: normal; text-align: left; color: #ffffff;">Season IV, US Cyber Open - Beginner's Game Room Participant</p><script async="async" src="https://badgr.com/assets/widgets.bundle.js"></script></blockquote>
"""

ncae_html = """
<blockquote class="badgr-badge" style="font-family: Helvetica, Roboto, &quot;Segoe UI&quot;, Calibri, sans-serif;"><a href="https://badgr.com/public/assertions/SybnZhsjRQSEYke5g9sZOA"><img width="120px" height="120px" src="https://api.badgr.io/public/assertions/SybnZhsjRQSEYke5g9sZOA/image"></a><p class="badgr-badge-name" style="hyphens: auto; overflow-wrap: break-word; word-wrap: break-word; margin: 0; font-size: 16px; font-weight: 600; font-style: normal; font-stretch: normal; line-height: 1.25; letter-spacing: normal; text-align: left; color: #ffffff;">2024 Competitor</p><script async="async" src="https://badgr.com/assets/widgets.bundle.js"></script></blockquote>
"""

st.title("SANS Certifications")

sans_col1, sans_col2, sans_col3, = st.columns(3, gap='small')
with sans_col1:
  st.subheader("GIAC Advisory Board")
  st.write("Credly badge link below:")
  components.html(advisory_html, height=250)

  st.subheader("GIAC Certified Incident Handler (GCIH)")
  st.write("Credly badge link below:", anchor=False)
  components.html(gcih_html, height=250)

with sans_col2:
  st.subheader("GIAC Foundational Cybersecurity Technologies (GFACT)")
  st.write("Credly badge link below:")
  components.html(gfact_html, height=250)

with sans_col3:
  st.subheader("GIAC Security Essentials Certification (GSEC)")
  st.write("Credly badge link below:")
  components.html(gsec_html, height=250)

st.divider()

st.title("CTF Badges")

ctf_col1, ctf_col2 = st.columns(2, gap='small')
with ctf_col1:
  st.subheader("US Cyber Open")
  st.write("Canvas badge link below:")
  components.html(us_cyber_html, height=250)

with ctf_col2:
  st.subheader("NCAE Cyber Games")
  st.write("Canvas badge link below:")
  components.html(ncae_html, height=250)
