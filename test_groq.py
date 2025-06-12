import os
from dotenv import load_dotenv
import requests

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Print masked key for verification
if api_key:
    masked_key = api_key[:4] + "*" * (len(api_key) - 8) + api_key[-4:]
    print(f"Found API key: {masked_key}")
else:
    print("No API key found in .env file")

# Test direct API call
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
data = {
    "model": "compound-beta-mini",
    "messages": [{"role": "user", "content": "who is the president of the United States?"}],
    "max_tokens": 100
}

try:
    print("Sending request to Groq API...")
    response = requests.post(url, headers=headers, json=data)
    print(f"Status code: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print("Success! Response:")
        print(f"- Model: {result['model']}")
        print(f"- Response: {result['choices'][0]['message']['content'][:50]}...")
        print(f"- Tokens used: {result['usage']['total_tokens']}")
    else:
        print(f"Error response: {response.text}")
except Exception as e:
    print(f"Error: {e}")