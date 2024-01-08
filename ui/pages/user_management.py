import streamlit as st

st.set_page_config(page_title="User Management")

st.write("# User Management")

st.write("### Create new User")
user_mail = st.text_input("E-Mail")
username = st.text_input("Username")

is_device_maintainer = st.checkbox("Device Maintainer")
if is_device_maintainer == True:
    st.selectbox("Select Device", ["Device 1", "Device 2", "Device 3"])

is_booking_guy = st.checkbox("Access for booking devices")

if st.button("Add new User") == True:
    print(user_mail, username, is_admin, is_device_maintainer, is_booking_guy)
    st.success("User created successfully")
