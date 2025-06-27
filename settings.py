# settings.py
import os
from dotenv import load_dotenv, find_dotenv


dotenv_path: str = find_dotenv()

if not os.path.exists(dotenv_path):
    raise FileNotFoundError(f"Environment file not found: {dotenv_path}")
print('Successfully loading environment variables from:\n\t', dotenv_path)

load_dotenv(dotenv_path)

CLIENT_ID: str = os.environ.get("CLIENT_ID", "")
CLIENT_SECRET: str = os.environ.get("CLIENT_SECRET", "")
REDIRECT_URI: str = os.environ.get("REDIRECT_URI", "")
SCOPE: str = 'playlist-read-private'

if not CLIENT_ID or not CLIENT_SECRET or not REDIRECT_URI:
    raise ValueError("Missing required environment variables: CLIENT_ID, CLIENT_SECRETE, REDIRECT_URI")