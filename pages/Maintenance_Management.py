import streamlit as st
from home import db_devices, db_users, db_reservations  # Importiere die Datenbanken aus der home-Datei
from datetime import time  # Datetime-Bibliothek für die Arbeit mit Zeitangaben
from tinydb import TinyDB, Query  # TinyDB für die Verwaltung von einfachen Datenbanken
import uuid  # uuid-Bibliothek zur Erzeugung von UUIDs (Universally Unique Identifier)

# Datenbankabfragen für Reservierungen, Geräte und Benutzer
reservations = db_reservations.all()
devices = db_devices.all()
users = db_users.all()

# Streamlit-Konfiguration für die Seite
st.set_page_config(page_title="Maintenance List")
st.write("# Maintenance List")
st.write("Sum of all Maintenance Costs per quarter: 60€")
st.write("## Next Maintenance")

# Streamlit-Menü erstellen
device_info = {device["device_name"]: {"cost_per_quarter": device["cost_per_quarter"]} for device in db_devices.all()}
device_names = list(device_info.keys())  # Liste der Gerätenamen aus der Datenbank extrahieren
device_name = st.selectbox("Select Device", device_names)  # Dropdown-Menü für Geräte erstellen
reservation_date = st.date_input("Date")  # Datumseingabe für die Reservierung
reservation_time = st.time_input("Time Start", value=time(8, 0), step=900)  # step=900 für 15-Minuten-Schritte
reservation_time_end = st.time_input("Time End", value=time(8, 0), step=900)  # step=900 für 15-Minuten-Schritte

# Button zum Hinzufügen von Wartungen
if st.button("Maintenance"):
    # Hier wird die Wartung in der Datenbank speichern
    new_maintenance = {
        "title": f"Maintenance for {device_name}",
        "start": f"{reservation_date}T{reservation_time}",
        "end": f"{reservation_date}T{reservation_time_end}",
        "resourceId": f"{device_name}",
        "color": "#0000FF",  # Beispiel für Farbe,
        "reservation_id": "0",  # Reservierungs-ID 0 für Wartungen
        "maintenance_id": str(uuid.uuid4())  # Erstellt eine zufällige UUID für die Wartung
    }
    db_reservations.insert(new_maintenance)

    # Reservierungs-ID anzeigen
    maintenance_id = new_maintenance["maintenance_id"]
    st.success(f"Successfully scheduled maintenance for {device_name} on {reservation_date} (Maintenance ID: {maintenance_id})")

# Funktion zur Stornierung von Wartungen
cancel_maintenance_id = st.text_input("Enter Maintenance ID to Cancel:")
if st.button("Cancel Maintenance"):
    # Hier wird die Wartung anhand der Maintenance-ID stornieren
    canceled_maintenance = db_reservations.remove(Query().maintenance_id == cancel_maintenance_id)

    if canceled_maintenance:
        st.success(f"Maintenance with ID {cancel_maintenance_id} has been canceled.")
    else:
        st.error(f"No maintenance found with ID {cancel_maintenance_id}.")

# Alle Wartungen mit Reservierungs-ID 0 aus der Datenbank abrufen
maintenance_with_reservation_id_zero = db_reservations.search((Query().reservation_id == "0"))

if maintenance_with_reservation_id_zero:
    st.write("## Maintenance Details")
    for maintenance in maintenance_with_reservation_id_zero:
        st.write(f"Device: {maintenance['resourceId']}")
        st.write(f"Start Date and Time: {maintenance['start']}")
        st.write(f"End Date and Time: {maintenance['end']}")
        st.write(f"Maintenance ID: {maintenance['maintenance_id']}")
        st.write(f"Cost for Maintenance: {device_info[maintenance['resourceId']]['cost_per_quarter']}")
else:
    st.warning("No maintenance records found.")