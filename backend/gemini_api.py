from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Gemini key from .env
key = os.environ.get("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=key)

# --- Simple interactive loop ---
print("✅ Gemini Text Generator Ready! Type 'exit' to quit.")
while True:
    prompt = input("\n🗣 Enter your message: ")
    if prompt.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        print("\n🤖 Gemini:", response.text)
    except Exception as e:
        print("❌ Error:", e)
