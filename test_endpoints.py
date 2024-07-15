import requests

base_url = "http://127.0.0.1:5000/mensajeria"

def test_listar_contactos(alias):
    response = requests.get(f"{base_url}/contactos?mialias={alias}")
    print(f"Listar Contactos ({alias}):", response.json())

def test_enviar_mensaje(mialias, aliasdestino, texto):
    response = requests.post(f"{base_url}/enviar?mialias={mialias}&aliasdestino={aliasdestino}&texto={texto}")
    print(f"Enviar Mensaje ({mialias} -> {aliasdestino}):", response.json())

def test_mensajes_recibidos(alias):
    response = requests.get(f"{base_url}/recibidos?mialias={alias}")
    print(f"Mensajes Recibidos ({alias}):", response.json())

if __name__ == "__main__":
    test_listar_contactos("cpaz")
    test_enviar_mensaje("cpaz", "lmunoz", "hola")
    test_mensajes_recibidos("lmunoz")
