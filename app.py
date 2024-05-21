import paho.mqtt.client as mqtt
import streamlit as st
import json

broker = "broker.mqttdashboard.com"
port = 1883
topic = "cmqtt_And"
client_id = "StreamlitApp"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker MQTT")
    else:
        print("Error de conexión: ", rc)

def on_publish(client, userdata, mid):
    print("Mensaje publicado con éxito")

def send_message(gesture):
    try:
        client = mqtt.Client(client_id)
        client.on_connect = on_connect
        client.on_publish = on_publish
        client.connect(broker, port)
        message = json.dumps({"gesto": gesture})
        client.publish(topic, message)
        client.disconnect()
    except Exception as e:
        print("Error al enviar el mensaje MQTT:", e)

st.title("Control de Dispositivo")

if st.button("Encender Luz"):
    send_message("prender luz")
    st.success("La luz ha sido encendida.")

if st.button("Apagar Luz"):
    send_message("apagar luz")
    st.success("La luz ha sido apagada.")

