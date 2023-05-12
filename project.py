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