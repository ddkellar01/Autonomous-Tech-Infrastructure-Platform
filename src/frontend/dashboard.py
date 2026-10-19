import streamlit as st
import json
import os

st.title("Autonomous Tech & Infrastructure Dashboard")
st.sidebar.header("Control Panel")

if st.sidebar.button("Run Scout Cycle"):
    st.success("Scout cycle triggered successfully!")

st.subheader("Latest Scout Intelligence Report")
if os.path.exists("scout_report.json"):
    with open("scout_report.json", "r") as f:
        report_data = json.load(f)
    st.json(report_data)
else:
    st.info("No scout report generated yet. Run a cycle to populate data.")
