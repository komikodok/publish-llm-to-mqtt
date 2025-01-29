from paho.mqtt import publish


broker = "mqtt.eclipseprojects.io"
port = 1883
topic = "generation-ai/1"


while True:
    message = input("Message from publisher: ")
    publish.single(topic=topic, hostname=broker, port=port, payload=message)