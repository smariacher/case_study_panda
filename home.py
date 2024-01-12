
import streamlit as st # Variante der Importierung wo immer .st vor den befehlen geschrieben werden muss.
from tinydb import TinyDB, Query # Variante der Importierung wo nichts mehr vor die Befehle geschrieben werden muss.

    
db_devices = TinyDB('./data/devices.json')
db_users = TinyDB('./data/users.json')
db_reservations = TinyDB('./data/reservations.json')
 



st.set_page_config(
    page_title="Home",
)

st.write("# Willkommen zur Geräteverwaltung des MCI")

