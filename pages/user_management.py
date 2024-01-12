# DATENBANK schaut so aus:
# user_id (zufällige Zahl von 0 bis viel)
# user_name 
# user_mail
# is_device_maintainer (true if user maintaines device)
# maintaines_device (the device the user maintaines)

import streamlit as st
from home import db_users, db_devices
from random import randint
from tinydb import TinyDB, Query

st.set_page_config(page_title="User Management")

st.write("# User Management")
st.write("### Create new User")
user_mail = st.text_input("E-Mail")
username = st.text_input("Username")
maintaines_device = None

is_device_maintainer = st.checkbox("Device Maintainer")

all_device_data = db_devices.all()
devices = [device['device_name'] for device in all_device_data if 'device_name' in device]

if is_device_maintainer == True:
    maintaines_device = st.selectbox("Select Device", devices)

is_booking_guy = st.checkbox("Access for booking devices")


all_users = db_users.all()
used_ids = [user['user_name'] for user in all_users if 'user_id' in user]


if st.button("Add new User") == True:
    user_id = randint(0,99999999999999999)
    while user_id in used_ids:
        user_id = randint(0,99999999999999999)
    
    db_users.insert({'user_id':user_id,'user_name':username, 'user_mail': user_mail, 'is_device_maintainer':is_device_maintainer,'maintaines_device': maintaines_device})
    print(user_id ,user_mail, username, is_device_maintainer, is_booking_guy)
    st.success("User created successfully")
