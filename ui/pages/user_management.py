import streamlit as st

st.set_page_config(page_title="Benutzer Verwaltung")

st.write("# User Management")

st.write("### Create new User")
username = st.text_input("Username")
password = st.text_input("Password")

is_admin = st.checkbox("Admin")

is_device_maintainer = st.checkbox("Device Maintainer")
if is_device_maintainer == True:
    st.selectbox("Select Device", ["Device 1", "Device 2", "Device 3"])

is_booking_guy = st.checkbox("Access for booking devices")

if st.button("Add new User") == True:
    print(username, password, is_admin, is_device_maintainer, is_booking_guy)
    st.success("User created successfully")
