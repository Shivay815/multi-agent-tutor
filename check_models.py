import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv() # Load your API key from .env

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not found in .env file.")
else:
    genai.configure(api_key=api_key)
    try:
        print("Listing available Gemini models and their supported methods:")
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"Model: {m.name} | Supported methods: {m.supported_generation_methods}")
    except Exception as e:
        print(f"An error occurred while listing models: {e}")