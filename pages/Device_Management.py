#Dokumentation für die devices.json
# device_name
# device_type
# device_location
# cost per quarter
# device_maintainer_id



#Hier arbeitet King Julien

import streamlit as st
from home import db_devices, db_users, db_reservations
from tinydb import TinyDB, Query

query = Query()

st.set_page_config(page_title="Device Management")

st.write("# Device Management")


#Bereich: Erstellen von neuen Geräten


st.write("### Create new device")

device_name = st.text_input("Device Name")
device_type = st.text_input("Device Type")
device_location = st.text_input("Device Location")
cost_per_quarter = st.number_input("Cost per quarter in €", step=0.01)




#Auswahl der Device Maintainer:

#Suchen der Leute bei denen Device Maintainer == true:
maintain_user_full = db_users.search(query.is_device_maintainer == True)
#Die JSON Objekte der Leute sind jetzt in einer Liste gespeichert.

#Hier werden die Namen der Leute in eine Liste geschrieben und dann in das Dropdown Menü geladen.
maintain_user_name = [user['user_name'] for user in maintain_user_full if 'user_name' in user]
device_maintainer_id = st.selectbox("Select Device Maintainer", maintain_user_name) 

#Jetzt muss noch die ID des Maintainers in die Datenbank geschrieben werden.
#Dazu muss die ID des Maintainers aus der Liste der JSON Objekte ausgelesen werden.
#Danach muss die ID des Maintainers in die Datenbank mit den anderen Daten geschrieben werden. 
maintain_save_id = [user['user_id'] for user in maintain_user_full if 'user_name' in user and user['user_name']] == device_maintainer_id

#WARUM KOMMT HIER FALSE RAUS ? DAVOR KAM DIE RICHTIGE NUMMER RAUS =!=!=!!=! XYZ


if st.button("Add new Device") == True:
    db_devices.insert({'device_name': device_name, 'device_type': device_type, 'device_location': device_location, 'cost_per_quarter': cost_per_quarter, 'device_maintainer_id': maintain_save_id})
    print(device_name, device_type, device_location, cost_per_quarter, maintain_save_id)
    st.success("Device created successfully")










#Bereich: Bearbeiten von bestehenden Geräten.


st.write("### Change device")


change_device_name = st.selectbox("Change Device Name", ["Device 1", "Device 2", "Device 3"])
#Die Namen der Devices die bereits in der Datenbank sind müssen hier noch reingeladen werden.
change_device_type = st.text_input("Change Device Type")
#Auf Basis der Auswahl des Devices soll hier der Typ dann editierbar angezeigt werden.
change_device_location = st.text_input("Change Device Location")
#Auf Basis der Auswahl des Devices soll hier die Location dann editiertbar angezeigt werden.
change_cost_per_quarter = st.number_input("Change cost per quarter in €", step=0.01)
#Auf Basis der Auswahl des Devices soll hier der Preis dann editierbar angezeigt werden.
change_device_maintainer_id = st.selectbox("Change Device Maintainer", ["Peter", "Hans", "Max"])
#Auf Basis der Auswahl des Devices soll hier der Preis dann editierbar angezeigt werden.
#Im Dropdown Menü sollten wieder nur die Leute angezeigt werden, die device_maintainer auf true gesetzt haben.

if st.button("Change Device") == True:
    print(change_device_name, change_device_type, change_device_location, change_cost_per_quarter, change_device_maintainer_id)
    #Änderungen sollen hier in die Datenbank geschrieben werden. 
    #Dazu muss das Objekt gesucht werden und dann die neuen Variablen an die jeweilige Position geschrieben werden.
    st.success("Device changed successfully")
