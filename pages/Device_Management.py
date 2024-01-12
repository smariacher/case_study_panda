#Dokumentation für die devices.json
# device_name
# device_type
# device_location
# cost per quarter
# device_maintainer_id



#Hier arbeitet King Julien

import streamlit as st
from home import db_devices, db_users, db_reservations


st.set_page_config(page_title="Device Management")

st.write("# Device Management")


#Erstellen von neuen Geräten


st.write("### Create new device")

device_name = st.text_input("Device Name")
device_type = st.text_input("Device Type")
device_location = st.text_input("Device Location")
cost_per_quarter = st.number_input("Cost per quarter in €", step=0.01)
device_maintainer_id = st.selectbox("Select Device Maintainer", ["Peter", "Hans", "Max"]) 
#Zugriff auf Simons Datenbank über die ID
#Hier fehlt noch die ID. Aktuell wird der Name ausgewählt und dieser in der Datenbank gespeichtert.
#Ziel: Name auswählen und ID speichern. Dazu muss die Datenbank von Simon gelesen werden und alle mit
#Device_maintainer = True in der Liste ausgegeben werden.
#Beim Speichern dann nur die ID in die Datenbank übergeben.


if st.button("Add new Device") == True:
    db_devices.insert({'device_name': device_name, 'device_type': device_type, 'device_location': device_location, 'cost_per_quarter': cost_per_quarter, 'device_maintainer_id': device_maintainer_id})
    print(device_name, device_type, device_location, cost_per_quarter, device_maintainer_id)
    st.success("Device created successfully")




#Bearbeiten von bestehenden Geräten.


st.write("### Change device")

device_name = st.selectbox("Change Device Name", ["Device 1", "Device 2", "Device 3"])
device_type = st.text_input("Change Device Type")
device_location = st.text_input("Change Device Location")
cost_per_quarter = st.number_input("Change cost per quarter in €", step=0.01)

device_maintainer_id = st.selectbox("Change Device Maintainer", ["Peter", "Hans", "Max"])

if st.button("Change Device") == True:
    print(device_name, device_type, device_location, cost_per_quarter, device_maintainer_id)
    st.success("Device changed successfully")
