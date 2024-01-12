import streamlit as st

st.set_page_config(page_title="Device Management")

st.write("# Device Management")

st.write("### Create new device")
username = st.text_input("Device Name")
device_type = st.text_input("Device Type")
device_location = st.text_input("Device Location")
cost_per_quarter = st.number_input("Cost per quarter in €", step=0.01)

device_maintainer = st.selectbox("Select Device Maintainer", ["Peter", "Hans", "Max"])

if st.button("Add new Device") == True:
    print(username, device_type, device_location, cost_per_quarter, device_maintainer)
    st.success("Device created successfully")


st.write("### Change device")

username = st.selectbox("Change Device Name", ["Device 1", "Device 2", "Device 3"])
device_type = st.text_input("Change Device Type")
device_location = st.text_input("Change Device Location")
cost_per_quarter = st.number_input("Change cost per quarter in €", step=0.01)

device_maintainer = st.selectbox("Change Device Maintainer", ["Peter", "Hans", "Max"])

if st.button("Change Device") == True:
    print(username, device_type, device_location, cost_per_quarter, device_maintainer)
    st.success("Device changed successfully")
