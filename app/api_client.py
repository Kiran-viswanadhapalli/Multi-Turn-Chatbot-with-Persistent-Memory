from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("api key not found check your .env file")
client=OpenAI(api_key=api_key)

def chat(messages):
    model="gpt-5-mini"
    try:
        response=client.chat.completions.create(
            messages=messages,
            model=model
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"





