import os
from dotenv import load_dotenv


class Config:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        # Get API key from environment variable
        self.api_key = os.getenv("GROQ_API_KEY")

        # Model configuration - using compound-beta-mini as specified
        self.model = os.getenv("GROQ_MODEL", "compound-beta-mini")

        # Default parameters
        self.max_tokens = int(os.getenv("MAX_TOKENS", "1024"))
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))

    def validate(self):
        """Validate configuration settings"""
        if not self.api_key:
            raise ValueError(
                "GROQ_API_KEY not found. Please set it in your environment "
                "variables or .env file."
            )
        return True