
# LLM Integration with MQTT

This project demonstrates how to integrate a Large Language Model (LLM) with the MQTT (Message Queuing Telemetry Transport) protocol. The goal is to enable seamless communication between an LLM (like llama's or other models) and IoT devices or systems that use MQTT for messaging.


## Prerequisites

- Python 3.8 or higher (tested with Python 3.11)

- An MQTT broker (e.g., Mosquitto, HiveMQ -> tested with broker "mqtt.eclipseprojects.io")

- An LLM API key (e.g., OpenAI, Hugging Face, or custom model -> tested using groq api key)

## Run Locally

Clone the repository or download the project directly from GitHub

```bash
  git clone https://github.com/komikodok/llm-integration-with-mqtt
```

Go to the project directory

```bash
  cd <project-directory>
```

Install dependencies

```bash
  pip install -r requirements.txt
```

## Environment

What needs to be added to .env
```bash  
BROKER = <broker>
PORT = <mqtt port>
TOPIC_MQTT_TO_LLM = <topic>

LLM = <the model you want>
GROQ_API_KEY = <your api key>
```