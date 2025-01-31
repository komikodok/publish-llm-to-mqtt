from paho.mqtt import publish

from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv(".env.example"))

broker = os.getenv("BROKER")
port = int(os.getenv("PORT"))
topic = os.getenv("TOPIC_MQTT_TO_LLM")

while True:
    message = input("Message from publisher: ")
    publish.single(topic=topic, hostname=broker, port=port, payload=message)