import streamlit as st
from home import db_devices, db_users, db_reservations


st.set_page_config(page_title="Device Management")

st.write("# Device Management")

st.write("### Create new device")
device_name = st.text_input("Device Name")
device_type = st.text_input("Device Type")
device_location = st.text_input("Device Location")
cost_per_quarter = st.number_input("Cost per quarter in €", step=0.01)

device_maintainer = st.selectbox("Select Device Maintainer", ["Peter", "Hans", "Max"])

if st.button("Add new Device") == True:
    db_devices.insert({'device_name': device_name})
    print(device_name, device_type, device_location, cost_per_quarter, device_maintainer)
    st.success("Device created successfully")


st.write("### Change device")

device_name = st.selectbox("Change Device Name", ["Device 1", "Device 2", "Device 3"])
device_type = st.text_input("Change Device Type")
device_location = st.text_input("Change Device Location")
cost_per_quarter = st.number_input("Change cost per quarter in €", step=0.01)

device_maintainer = st.selectbox("Change Device Maintainer", ["Peter", "Hans", "Max"])

if st.button("Change Device") == True:
    print(device_name, device_type, device_location, cost_per_quarter, device_maintainer)
    st.success("Device changed successfully")
