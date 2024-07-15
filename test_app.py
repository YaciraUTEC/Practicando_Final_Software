# test_app.py

import unittest
from app import app

class MensajeriaTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_enviar_exito(self):
        # Prueba de éxito: Enviar mensaje exitoso
        response = self.app.post('/mensajeria/enviar?mialias=cpaz&aliasdestino=lmunoz&texto=hola')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Realizado en", response.data)

    def test_enviar_error_parametros_faltantes(self):
        # Prueba de error: Faltan parámetros (texto)
        response = self.app.post('/mensajeria/enviar?mialias=cpaz&aliasdestino=lmunoz')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"All parameters (mialias, aliasdestino, texto) are required", response.data)

    def test_enviar_error_destinatario_invalido(self):
        # Prueba de error: Destinatario no es contacto del remitente
        response = self.app.post('/mensajeria/enviar?mialias=cpaz&aliasdestino=unknown&texto=hola')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Receiver not in contact list or invalid sender/receiver", response.data)

    def test_enviar_error_remitente_invalido(self):
        # Prueba de error: Remitente no existe
        response = self.app.post('/mensajeria/enviar?mialias=unknown&aliasdestino=lmunoz&texto=hola')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Receiver not in contact list or invalid sender/receiver", response.data)

if __name__ == '__main__':
    unittest.main()
