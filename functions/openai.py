from openai import OpenAI


def openai_client(api_key):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    return client;
