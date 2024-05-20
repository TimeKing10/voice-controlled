import streamlit as st
import speech_recognition as sr
import paho.mqtt.client as mqtt

# Inicialización del cliente MQTT
mqtt_broker = "broker.mqttdashboard.com"
mqtt_port = 1883
mqtt_topic = "control_por_voz"

client = mqtt.Client("ControlPorVozClient")
client.connect(mqtt_broker, mqtt_port)

# Interfaz de usuario
st.title("Control por Voz")

# Funcionalidad de control por voz
def control_por_voz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Escuchando...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            st.write("Texto reconocido:", text)
            # Publicar el texto reconocido en el topic MQTT
            client.publish(mqtt_topic, text)
        except sr.UnknownValueError:
            st.write("No se pudo entender el audio")
        except sr.RequestError as e:
            st.write("Error en la solicitud:", e)

# Llamada a la función de control por voz
control_por_voz()
