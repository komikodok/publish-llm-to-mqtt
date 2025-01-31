from paho.mqtt import client
from groq_api_response import get_response

from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv(".env.example"))

broker = os.getenv("BROKER")
port = os.getenv("PORT")
topic = os.getenv("TOPIC_MQTT_TO_LLM")

message = ""

def on_connect(client, userdata, flags, reason_code):
    print(f"Connected with result code {reason_code}")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    global message
    message = msg.payload.decode()
    print(f"Message from subscriber: {message}")


client = client.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port)

client.loop_start()

while True:
    if message:
        result = get_response(message)
        print(f"Bot Response: {result}")
    message = ""

client.loop_stop()