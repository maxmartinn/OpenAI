from openai import OpenAI as OpenAIClient
from ConfigService import ConfigService


class OpenAI:
    """Singleton class to manage OpenAI client instance."""
    
    _instance = None
    _client = None
    _config_service = None

    def __new__(cls, config_service: ConfigService):
        """Ensure only one instance of OpenAI class exists."""
        if cls._instance is None:
            cls._instance = super(OpenAI, cls).__new__(cls)
            cls._config_service = config_service
            cls._instance._initialize()  
        return cls._instance

    def __init__(self, config_service: ConfigService):
        """No-op init since initialization is handled in __new__"""
        pass
    
    def _initialize(self):
        """Initialize the OpenAI client with configuration"""
        if not self._client:  # Only initialize if not already done
            api_key = self._config_service.get_openai_key()
            system_msg = self._config_service.get_system_message()
            self._client = OpenAIClient(
                api_key=api_key,
                default_headers={"system_message": system_msg}
            )
        
