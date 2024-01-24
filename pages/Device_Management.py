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
from random import randint

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
device_user_selected = st.selectbox("Select Device Maintainer", maintain_user_name) 

#Ich benötige nun die ID des ausgewählten Users um diese in die Datenbank zu schreiben.
writing_user_id = [user['user_id'] for user in maintain_user_full if user['user_name'] == device_user_selected]
#Jetzt muss ich die writing_user_id noch unformatieren damit es eine Zahl ist und nicht eine Liste mit einer Zahl.
writing_user_id = writing_user_id[0]


#Hier werden die Informationen des neuen Gerätes in die Datenbank geschrieben.
if st.button("Add new Device") == True:
    device_id = randint(0,99999999999999999)
    while device_id in db_devices.search(query.device_id == device_id):
        device_id = randint(0,99999999999999999)
    db_devices.insert({'device_id': device_id, 'device_name': device_name, 'device_type': device_type, 'device_location': device_location, 'cost_per_quarter': cost_per_quarter, 'device_maintainer_id': writing_user_id})
    print(device_name, device_type, device_location, cost_per_quarter, writing_user_id)
    st.success("Device created successfully")











#Bereich: Bearbeiten von bestehenden Geräten.


st.write("### Change device")




#Die Namen der Devices die bereits in der Datenbank sind müssen hier noch reingeladen werden.
all_device_data = db_devices.all()
devices = [device['device_name'] for device in all_device_data if 'device_name' in device]
change_device_name = st.selectbox("Select Device", devices)
#ID des gewählten devices:
change_device_id = [device['device_id'] for device in all_device_data if device['device_name'] == change_device_name]
change_device_id = change_device_id[0] 



#Auf Basis der Auswahl des Devices soll hier der Typ dann editierbar angezeigt werden.
selected_change_device_type = db_devices.search(query.device_name == change_device_name)
change_device_type = st.text_input("Change Device Type", selected_change_device_type[0]['device_type']) # Funktioniert, da nur ein Objekt in der Liste ist.

#Auf Basis der Auswahl des Devices soll hier die Location dann editiertbar angezeigt werden.
selected_change_device_location = db_devices.search(query.device_name == change_device_name)
change_device_location = st.text_input("Change Device Location", selected_change_device_location[0]['device_location'])

#Auf Basis der Auswahl des Devices soll hier der Preis dann editierbar angezeigt werden.
selected_change_cost_per_quarter = db_devices.search(query.device_name == change_device_name)
change_cost_per_quarter = st.number_input("Change cost per quarter in €", step=0.01, value=selected_change_cost_per_quarter[0]['cost_per_quarter'])

#Auf Basis der Auswahl des Devices soll hier der Preis dann editierbar angezeigt werden.
#Im Dropdown Menü sollten wieder nur die Leute angezeigt werden, die device_maintainer auf true gesetzt haben.
#Wurde bereits oben für die Auswahl erstellt.
change_device_maintainer_name = st.selectbox("Change Device Maintainer", maintain_user_name)
#Hier muss ich noch wieder die ID rausfiltern: XYZ
change_device_maintainer_id = [user['user_id'] for user in maintain_user_full if user['user_name'] == change_device_maintainer_name]
change_device_maintainer_id = change_device_maintainer_id[0]



#Der Schreibvorgang fehlt noch hier XYZ.

if st.button("Change Device") == True:
    #Auf Basis der ID des Devices sollen die anderen Daten geupdated werden.
    db_devices.update({'device_name': change_device_name, 'device_type': change_device_type, 'device_location': change_device_location, 'cost_per_quarter': change_cost_per_quarter, 'device_maintainer_id': change_device_maintainer_id}, query.device_id == change_device_id)
    print(change_device_name, change_device_type, change_device_location, change_cost_per_quarter, change_device_maintainer_id)
    st.success("Device changed successfully")







#Probleme bei Editing:
#Auf Basis der Device ID soll das Objekt in der Datenbank geupdatet werden. Dafür muss zuerst die ID rausgefiltert werden. Schwierig bei Namensänderung.
#Lösung -> Änderung des Namens ist nicht möglich. Macht auch keinen Sinn, da der Benutzer des Programmes die ID nicht sieht.
