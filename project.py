# importar libreria paho-mqtt para la conexión & time para las pausas
import paho.mqtt.client as mqtt
import time


# se piden los valores iniciales, IP, nombre de usuario y tópico (tienen que tener ambos la misma IP y tópico)
ip = input("ip: ")
user = input("Username: ")
topic = input("Topico: ")
port = 1883

# funciones callback 
def on_connect(client,userdata,flags,rc):
    print("Conexion Exitosa")
def on_message(client,userdata,message):
    msg = str(message.payload.decode("utf-8"))
    print(msg)

# funciones del cliente MQTT 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# conexión con el cliente
client.connect(ip,port)

# pausa de 1 segundo
time.sleep(1)

# comenzamos el loop y suscribimos el usuario al topico (tiene que ser el mismo los dos para poderse comunicar)
client.loop_start()
client.subscribe(topic)

time.sleep(1)

# funcionalidad para mandar mensajes con un bucle infinito que solo se rompe al mandar "stop"
while True:
    msg = input(">>>")
    chat = user + ": " + msg
    client.publish(topic,chat)
    if msg == "Stop" or msg == "stop":
        break

# nos desconectamos del cliente una vez cerrado el bucle y cerramos el loop
client.disconnect()
client.loop_stop()