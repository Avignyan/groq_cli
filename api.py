import requests
from typing import Dict, Any, Optional


class GroqAPI:
    def __init__(self, api_key: str, model: str = "compound-beta-mini"):
        self.api_key = api_key
        self.model = model
        self.base_url = "https://api.groq.com/openai/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def ask(
            self,
            prompt: str,
            max_tokens: int = 1024,
            temperature: float = 0.7
    ) -> Dict[str, Any]:
        """Send a prompt to the Groq API and get a response

        Args:
            prompt: The user's input question
            max_tokens: Maximum number of tokens to generate
            temperature: Controls randomness (0.0-1.0)

        Returns:
            Dict containing the response
        """
        try:
            # Format the message for the chat completion
            messages = [
                {
                    "role": "user",
                    "content": prompt
                }
            ]

            # Prepare the request data
            data = {
                "model": self.model,
                "messages": messages,
                "max_tokens": max_tokens,
                "temperature": temperature
            }

            # Make the API call
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=data
            )

            # Check for successful response
            response.raise_for_status()
            result = response.json()

            return {
                "text": result["choices"][0]["message"]["content"],
                "model": result["model"],
                "usage": result["usage"]
            }

        except Exception as e:
            return {
                "error": str(e),
                "text": None
            }