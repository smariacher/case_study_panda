


from tinydb import TinyDB, Query # Variante der Importierung wo nichts mehr vor die Befehle geschrieben werden muss.

db_devices = TinyDB('./data/devices.json')
db_users = TinyDB('./data/users.json')
db_reservations = TinyDB('./data/reservations.json')

query = Query()

abc = db_users.search(query.is_device_maintainer == True)

print(abc)

