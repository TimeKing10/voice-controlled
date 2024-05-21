import paho.mqtt.client as paho
import streamlit as st
import json

broker = "broker.mqttdashboard.com"
port = 1883
client1 = paho.Client("StreamlitApp")

def on_publish(client, userdata, result):
    print("El dato ha sido publicado\n")

def send_message(topic, payload):
    client1.connect(broker, port)
    client1.on_publish = on_publish
    message = json.dumps(payload)
    ret = client1.publish(topic, message)

st.title("Control de Dispositivo")

if st.button('ON'):
    send_message("cmqtt_And", {"Act1": "ON"})
    st.success("El dispositivo ha sido encendido.")

if st.button('OFF'):
    send_message("cmqtt_And", {"Act1": "OFF"})
    st.success("El dispositivo ha sido apagado.")
