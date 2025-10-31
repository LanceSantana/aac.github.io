from google import genai
from dotenv import load_dotenv
import os

# Load your .env file
load_dotenv()

# Get your key from environment
key = os.environ.get("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=key)   # ✅ lowercase api_key and pass variable directly

# Generate a response
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

# Print the text response
print(response.text)
