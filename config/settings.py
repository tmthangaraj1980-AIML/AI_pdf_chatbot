"""
Project Configuration
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY is None:
    raise ValueError("Google API Key not found. Check your .env file.")