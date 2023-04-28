from os import getenv
from os.path import isfile

from dotenv import load_dotenv

if isfile(".env"):
    load_dotenv(".env")
DEBUG = getenv("DEBUG", False)
if type(DEBUG) != bool:
    DEBUG = DEBUG.lower() == "true"
print(f"DEBUG: {DEBUG}")

if __name__ == "__main__":
    pass