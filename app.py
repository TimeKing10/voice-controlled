import paho.mqtt.client as paho
import streamlit as st
import json

broker = "broker.emqx.io"
port = 1883
client1 = paho.Client("StreamlitApp")

def on_publish(client, userdata, result):
    print("El dato ha sido publicado\n")

def send_message(topic, payload):
    client1.connect(broker, port)
    client1.on_publish = on_publish
    message = json.dumps(payload)
    ret = client1.publish(topic, message)

st.title("Control de Luces")

if st.button('Encender'):
    send_message("cmqtt_And", {"gesto": "ON"})
    st.success("El LED ha sido encendido.")

if st.button('Apagar'):
    send_message("cmqtt_And", {"gesto": "OFF"})
    st.success("El LED ha sido apagado.")
