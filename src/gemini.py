from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
key=os.environ.get('GEMINI_API_KEY')

client = genai.Client(apiKey={key})

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)
