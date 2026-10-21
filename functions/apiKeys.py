import os

from dotenv import load_dotenv


def load_enviorn():
    load_dotenv();
    api_key = os.environ.get("OPENROUTER_API_KEY");

    return api_key;
