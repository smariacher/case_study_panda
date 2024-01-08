import streamlit as st

st.set_page_config(page_title="Reservation Management")

st.write("# Reservation Management")

st.write("### Reserve a device")

device_name = st.selectbox("Select Device", ["Device 1", "Device 2", "Device 3"])
device_date = st.date_input("Date")
device_time = st.time_input("Time")

if st.button("Reserve") == True:
    print(f"Sucessfully reserved device {device_name} on {device_date} at {device_time}")
    st.success(f"Sucessfully reserved device {device_name} on {device_date} at {device_time}")
