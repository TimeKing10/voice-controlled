import paho.mqtt.client as paho
import streamlit as st
import json

broker = "broker.mqttdashboard.com"
port = 1883
client = paho.Client("StreamlitApp")

def on_publish(client, userdata, result):
    print("El dato ha sido publicado\n")

def send_message(topic, gesture):
    client.connect(broker, port)
    client.on_publish = on_publish
    message = json.dumps({"gesto": gesture})
    ret = client.publish(topic, message)

st.title("Control de Dispositivo")

if st.button("Encender Luz"):
    send_message("cmqtt_And", "prender luz")
    st.success("La luz ha sido encendida.")

if st.button("Apagar Luz"):
    send_message("cmqtt_And", "apagar luz")
    st.success("La luz ha sido apagada.")
