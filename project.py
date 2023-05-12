import paho.mqtt.client as mqtt
import time

ip = input("ip: ")
user = input("Username: ")
topic = input("Topico: ")
port = 1883

def on_connect(client,userdata,flags,rc):
    print("Conexion Exitosa")
def on_message(client,userdata,message):
    msg = str(message.payload.decode("utf-8"))
    print(msg)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(ip,port)

client.loop_start()
client.subscribe(topic)

client.disconnect()
client.loop_stop()