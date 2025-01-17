import openai
import os
from dotenv import load_dotenv
import json

class OpenAI:
    _instance = None
    _client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OpenAI, cls).__new__(cls)
            load_dotenv()
            api_key = os.getenv('OPENAI_API_KEY')
            if not api_key:
                raise ValueError("OPENAI_API_KEY environment variable not found")
            with open('config.json', 'r') as f:
                config = json.load(f)
                print(f"Hello World! I am {config['assistant']['system_message']}")
            cls._client = openai.OpenAI(api_key=api_key)
        return cls._instance

    def __init__(self):
        pass
