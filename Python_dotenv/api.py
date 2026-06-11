import os
from dotenv import load_dotenv
from google import genai

# 1. Load the secret API key from your local .env file
load_dotenv()
api_key = os.getenv("Gemini")

# 2. Fire up the Google GenAI Client
client = genai.Client(api_key=api_key)

# 3. Ask Gemini a question programmatically
print("🛰️ Connecting to Gemini...")
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Tell me in one sentence why learning AI engineering is a great career move.',
)

# 4. Print the final answer to your terminal
print("\n🤖 GEMINI RESPONSE:")
print(response.text)
print("--------------------")
