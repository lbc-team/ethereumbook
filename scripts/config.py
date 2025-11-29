import os
from dotenv import load_dotenv

load_dotenv(".env")


OPENROUTER_PREFIX = "openrouter:"

MODEL_GEMINI_20_FLASH = "google/gemini-2.0-flash-001"
OPENROUTER_MODEL_GEMINI_20_FLASH = OPENROUTER_PREFIX +  MODEL_GEMINI_20_FLASH


MAX_TOKENS = 8000  


