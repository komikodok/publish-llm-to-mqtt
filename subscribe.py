from paho.mqtt import client


broker = "mqtt.eclipseprojects.io"
port = 1883

message = ""

def on_connect(client, userdata, flags, reason_code):
    print(f"Connected with result code {reason_code}")
    client.subscribe("generation-ai/1")

def on_message(client, userdata, msg):
    global message
    message = msg.payload.decode()
    print(f"Message from subscriber: {message}")


client = client.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port)

client.loop_start()
print(message if message else "Else")
while True:
    if message:
        print(message if message else "Else")
    message = ""
client.loop_stop()