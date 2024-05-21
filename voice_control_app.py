import os
import paho.mqtt.client as mqtt
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator

# Configuración del cliente MQTT
broker = "broker.mqttdashboard.com"
port = 1883
topic = "IMIA"

# Función para enviar comandos al ESP32 a través de MQTT
def send_command(command):
    client = mqtt.Client("PythonClient")
    client.connect(broker, port)
    client.publish(topic, command)
    client.disconnect()

# Función para reconocer voz
def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Escuchando...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="es-ES")
        print("Texto reconocido: ", text)
        return text
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return ""
    except sr.RequestError as e:
        print("Error al solicitar resultados; {0}".format(e))
        return ""

# Función principal
def main():
    command = recognize_speech()

    if command:
        if "prender luces" in command.lower():
            send_command('{"gesto":"prender luces"}')
        elif "apagar luces" in command.lower():
            send_command('{"gesto":"apagar luces"}')

if __name__ == "__main__":
    main()
