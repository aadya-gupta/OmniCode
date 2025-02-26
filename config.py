from dotenv import load_dotenv
import os
import google.generativeai as genai
from google.generativeai import GenerativeModel

load_dotenv()
api_key = os.getenv("API_KEY")

genai.configure(api_key = api_key)

model = GenerativeModel("gemini-1.5-pro", safety_settings={"harassment": "block_none"})