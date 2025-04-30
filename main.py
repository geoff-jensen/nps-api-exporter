from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into environment

api_key = os.getenv("NPS_API_KEY")

if not api_key:
    raise ValueError("NPS_API_KEY not found in environment variables!")

print(f"Using API key: {api_key}")
