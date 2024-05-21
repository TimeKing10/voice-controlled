import paho.mqtt.client as paho
import streamlit as st
import json

broker = "broker.mqttdashboard.com"
port = 1883
client1 = paho.Client("WokwiControl")

def on_publish(client, userdata, result):
    print("El dato ha sido publicado\n")

def send_message(topic, payload):
    client1.connect(broker, port)
    client1.on_publish = on_publish
    message = json.dumps(payload)
    ret = client1.publish(topic, message)

st.title("Control de Luz")

if st.button('Encender Luz'):
    send_message("cmqtt_And", {"gesto": "prender luces"})

if st.button('Apagar Luz'):
    send_message("cmqtt_And", {"gesto": "apagar luces"})

