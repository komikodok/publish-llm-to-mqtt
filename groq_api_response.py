import requests
import os
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv('.env.example'))

groq_api = os.getenv('GROQ_API_KEY') # API key yg udah di copas dari groq diambil dari file .env
llm = os.getenv('LLM') # llm yg mau dipilih cek semua model di https://console.groq.com/docs/models misal "gemma2-9b-it"

def get_response(user_input: str):
    response = requests.post(
        url="https://api.groq.com/openai/v1/chat/completions",
        json={
                "model": llm,
                "messages": [{
                    "role": "user",
                    "content": user_input # prompt input
                }]
            },
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {groq_api}" 
        }
    )

    result = response.json()["choices"][0]["message"]["content"] # output dari llm

    return result