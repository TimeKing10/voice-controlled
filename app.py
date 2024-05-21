import paho.mqtt.client as paho
import streamlit as st
import json

broker="broker.mqttdashboard.com"
port=1883
client1= paho.Client("APP_CERR")
client1.on_message = on_message
client1.on_publish = on_publish
client1.connect(broker,port)

def on_publish(client, userdata, result):
    print("El dato ha sido publicado\n")

def send_message(topic, payload):
    client.connect(broker, port)
    client.on_publish = on_publish
    message = json.dumps(payload)
    ret = client.publish(topic, message)

st.title("Control de Dispositivo")

if st.button("Encender Dispositivo"):
    send_message("cmqtt_And", {"gesto": "prender luces"})

if st.button("Apagar Dispositivo"):
    send_message("cmqtt_And", {"gesto": "apagar luces"})
