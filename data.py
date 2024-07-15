# data.py
from datetime import datetime

class Usuario:
    def __init__(self, alias, nombre, contactos):
        self.alias = alias
        self.nombre = nombre
        self.contactos = contactos
        self.mensajes_recibidos = []

    def add_message(self, sender, text):
        timestamp = datetime.now().strftime("%d/%m/%Y")
        self.mensajes_recibidos.append({"from": sender, "text": text, "date": timestamp})

# Base de datos de usuarios
BD = [
    Usuario("cpaz", "Christian", ["lmunoz", "mgrau"]),
    Usuario("lmunoz", "Luisa", ["mgrau"]),
    Usuario("mgrau", "Miguel", ["cpaz"])
]

def get_user_by_alias(alias):
    for user in BD:
        if user.alias == alias:
            return user
    return None

def get_contacts(alias):
    user = get_user_by_alias(alias)
    if user:
        contacts = []
        for contact_alias in user.contactos:
            contact_user = get_user_by_alias(contact_alias)
            if contact_user:
                contacts.append({"alias": contact_user.alias, "nombre": contact_user.nombre})
        return contacts
    return []

def send_message(sender_alias, receiver_alias, text):
    sender = get_user_by_alias(sender_alias)
    receiver = get_user_by_alias(receiver_alias)
    if sender and receiver and receiver_alias in sender.contactos:
        receiver.add_message(sender.nombre, text)
        return True
    return False

def get_received_messages(alias):
    user = get_user_by_alias(alias)
    if user:
        return user.mensajes_recibidos
    return []
