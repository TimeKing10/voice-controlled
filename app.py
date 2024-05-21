import paho.mqtt.client as paho
import streamlit as st
import json

broker = "broker.mqttdashboard.com"
port = 1883
client1 = paho.Client("APP_CERR")

def on_publish(client, userdata, result):
    print("El dato ha sido publicado\n")

def send_message(topic, payload):
    client1.connect(broker, port)  # Utiliza client1 en lugar de client
    client1.on_publish = on_publish
    message = json.dumps(payload)
    ret = client1.publish(topic, message)  # Utiliza client1 en lugar de client

st.title("Control de Dispositivo")

if st.button("Encender Dispositivo"):
    send_message("cmqtt_And", {"gesto": "prender luces"})

if st.button("Apagar Dispositivo"):
    send_message("cmqtt_And", {"gesto": "apagar luces"})
