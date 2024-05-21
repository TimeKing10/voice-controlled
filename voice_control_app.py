import paho.mqtt.client as paho
import time
import speech_recognition as sr
import json

def on_publish(client, userdata, result):
    print("El dato ha sido publicado\n")
    pass

def on_message(client, userdata, message):
    print(f"Mensaje recibido: {str(message.payload.decode('utf-8'))}")

broker = "broker.mqttdashboard.com"
port = 1883
client1 = paho.Client("APP_VOICE")
client1.on_message = on_message
client1.on_publish = on_publish
client1.connect(broker, port)

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` debe ser una instancia de `Recognizer`")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` debe ser una instancia de `Microphone`")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Di un comando:")
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio, language="es-ES")
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API no disponible"
    except sr.UnknownValueError:
        response["success"] = False
        response["error"] = "No se entendió el audio"

    return response

while True:
    command = recognize_speech_from_mic(recognizer, microphone)
    if command["transcription"]:
        print(f"Comando reconocido: {command['transcription']}")
        if "prender luces" in command["transcription"].lower():
            client1.publish("IMIA", json.dumps({"gesto": "prender luces"}))
        elif "apagar luces" in command["transcription"].lower():
            client1.publish("IMIA", json.dumps({"gesto": "apagar luces"}))
    elif not command["success"]:
        print("No se pudo obtener el comando")
    time.sleep(2)
