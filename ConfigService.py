import os
import json
from dotenv import load_dotenv

class ConfigService:
    
    _openai_key = None
    _openai_system_msg = None
    _instance = None

    def load_openai_key(self): 
        openai_key = os.getenv('OPENAI_API_KEY')
        if not openai_key:
                raise ValueError("OPENAI_API_KEY environment variable not found")
        return openai_key
    
    def load_system_msg(self):
            with open('config.json', 'r') as f:
                config = json.load(f)
            return config['assistant']['system_message']

    def get_openai_key(self):
         return self._openai_key
    
    
    def get_system_message(self):
         return self._openai_system_msg

        
         
    def __new__(cls):
        if cls._instance is None:
            load_dotenv()
            cls._instance = super(ConfigService, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self._openai_key = self.load_openai_key()
        self._openai_system_msg = self.load_system_msg()
    

    