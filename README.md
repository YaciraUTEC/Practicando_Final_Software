# Practicando_Final_Software
## Caso de estudio
Desarrollar un software que implemente un sistema de mensajeria.
Se debe soportar las operaciones:

-	Contactos: Lista los contactos de un alias con su nombre.
-	Enviar Mensaje: Envía un mensaje de texto a un contacto (validar que esté en la lista de contactos)..
-	Mensajes Recibidos: Muestra la lista de mensajes recibidos por el usuario

### Pregunta 1
En un repositorio Github, desarrollar el código fuente (se recomienda usar Python, pero no es obligatorio) que implemente los endpoints:

```
/mensajeria/contactos?mialias=XXXX
/mensajeria/enviar?mialias=XXXX&aliasdestino=YYYY&texto=ZZZZ
/mensajeria/recibidos?mialias=XXXX
```
***Comprobamos que el code si funciona***
- Get: Contactos
/assets/get_contactos.png
### Pregunta 2 (4 puntos)

Realizar 4 pruebas unitarias para un caso de éxito y tres de error. Incluir las pruebas unitarias en el mismo repositorio Github.

Adicionar comentarios en cada prueba indicando el caso de prueba.


### Pregunta 3 (4 puntos)

Se requiere realizar un cambio en el software para realizar “broadcast” a todos los contactos. Adicionalmente se debe contabilizar el número de mensajes y “cobrar” un valor por mensaje.

Qué cambiaría en el código (Clases / Métodos) - No implementación.
Nuevos casos de prueba a adicionar.
Cuánto riesgo hay de “romper” lo que ya funciona?


