import streamlit as st  # Streamlit-Bibliothek für die Webanwendung
from home import db_devices, db_users, db_reservations  # Importiere die Datenbanken aus der home-Datei
from tinydb import TinyDB, Query  # TinyDB für die Verwaltung von einfachen Datenbanken
from streamlit_calendar import calendar  # Kalenderkomponente für Streamlit
from datetime import time  # Datetime-Bibliothek für die Arbeit mit Zeitangaben
import uuid  # uuid-Bibliothek zur Erzeugung von UUIDs (Universally Unique Identifier)


# Funktion zum Aktualisieren der Kalenderereignisse
def update_calendar_events():
    global calendar_events  # Zugriff auf die globale Variable (Globale Variable weil besser Zugriff im Code)
    reservations = db_reservations.all()# Reservierungen aus der Datenbank abrufen
    updated_calendar_events = []# Liste für Kalenderereignisse erstellen
    for reservation in reservations:# Durchlaufe alle Reservierungen in der Datenbank
        # Erstelle ein Ereignisobjekt für den Kalender
        event = {
            "title": reservation["title"],
            "start": reservation["start"],
            "end": reservation["end"],
            "resourceId": reservation["resourceId"],
            "color": reservation.get("color", ""),
            "reservation_id":reservation["reservation_id"],  
        }        
        updated_calendar_events.append(event)# Füge das erstellte Ereignis zur Liste von Kalenderereignissen hinzu
    
    calendar_events = updated_calendar_events# Aktualisiere die globale Variable mit den neuen Kalenderereignissen



calendar_events = []# Initialisiere die Liste der Kalenderereignisse

update_calendar_events()#Reservierung die bereits in der Datenbank sind hinzufügen

st.set_page_config(page_title="Reservation Management")# Streamlit-Seitenkonfiguration festlegen
# Überschriften für die Seite erstellen
st.write("# Reservation Management")
st.write("### Reserve a device")


# Die Datenbanken abrufen
users = db_users.all()
devices = db_devices.all()

# Konfigurationsoptionen für den Kalender festlegen(aus github Stremlit Kalender   https://github.com/im-perativa/streamlit-calendar/blob/master/README.md)
calendar_options = {
    "editable": "true",
    "selectable": "true",
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
    },
    "slotMinTime": "06:00:00",
    "slotMaxTime": "18:00:00",
    "initialView": "resourceTimelineDay",
    "resourceGroupField": "device",
    "resources": [
        {"id": str(device["device_name"]), "device": str(device["device_location"]), "title": str(device["device_name"])} for device in devices
    ],
}


# Benutzerdefiniertes CSS für den Kalender
custom_css = """
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
"""

#Streamlit Menü erstellen
device_names = [device["device_name"] for device in db_devices.all()]  # Liste der Gerätenamen aus der Datenbank extrahieren
device_name = st.selectbox("Select Device", device_names)  # Dropdown-Menü für Geräte erstellen
reservation_date = st.date_input("Date")  # Datumseingabe für die Reservierung
reservation_time = st.time_input("Time Start", value=time(8, 0), step=900)  # step=900 für 15-Minuten-Schritte
reservation_time_end = st.time_input("Time End", value=time(8, 0), step=900)  # step=900 für 15-Minuten-Schritte


if st.button("Reserve"): # Hier wird die Reservierung in der Datenbank speichern   
    new_reservation = {
        "title": f"Reservation for {device_name}",
        "start": f"{reservation_date}T{reservation_time}",
        "end": f"{reservation_date}T{reservation_time_end}",
        "resourceId": f"{device_name}",
        "color": "#FF5733",  # Beispiel für Farbe,
        "reservation_id": str(uuid.uuid4()),  # Erstellt eine zufällige UUID
        "maintenance_id":f"0"  # Erstellt eine zufällige UUID
    }
    db_reservations.insert(new_reservation)

    #Um die Kalenderereignisse zu aktualisieren
    update_calendar_events()

    # Reservierungs-ID anzeigen
    reservation_id = new_reservation["reservation_id"]
    st.success(f"Successfully reserved {device_name} on {reservation_date} (Reservation ID: {reservation_id})")

#Funktion zur Stornierung 
cancel_reservation_id = st.text_input("Enter Reservation ID to Cancel:")
if st.button("Cancel Reservation"):
    # Hier wird die Reservierung anhand der Reservierungs-ID stornieren
    canceled_reservation = db_reservations.remove(Query().reservation_id == cancel_reservation_id)

    if canceled_reservation:
        st.success(f"Reservation with ID {cancel_reservation_id} has been canceled.")
        #Um die Kalenderereignisse zu aktualisieren
        update_calendar_events()
    else:
        st.error(f"No reservation found with ID {cancel_reservation_id}.")


# Kalender erstellen und auf der Seite anzeigen
calendar = calendar(events=calendar_events, options=calendar_options, custom_css=custom_css)
st.write(calendar)
