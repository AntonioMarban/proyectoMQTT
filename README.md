# proyectoMQTT
proyecto herramientas computacionales: el arte ed la 


<div style="text-align: justify">
El código es un script de Python que utiliza la biblioteca paho.mqtt.client para establecer una conexión MQTT con un servidor y permitir la comunicación de mensajes en un tópico específico. Proporciona una funcionalidad básica de chat, donde el usuario puede enviar mensajes y recibir mensajes de otros clientes suscritos al mismo tópico.

El código se divide en varias secciones y utiliza funciones proporcionados por la biblioteca "paho.mqtt.client" para establecer la conexión MQTT, suscribirse a un tópico, enviar y recibir mensajes.


* Es necesario correr "pip install paho-mqtt" para que la conexion con el servidor MQTT sea exitosa.
* Es necesario dar una ip publica en la que este corriendo mosquitto.
* Para despues dar el usuario y el topico al que se va a suscribir.
* Es importante que el topico sea el mismo para ambos clientes.
* Para salir se debe escribir "stop" o "Stop".
</div>