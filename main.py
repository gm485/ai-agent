#from functions.apiKeys import load_enviorn
import argparse

from functions.openai import openai_client;

import os;
from dotenv import load_dotenv;

def main():
    print("hello from ai agent")
    #api_key = load_enviorn();
    load_dotenv();
    api_key = os.environ.get("OPENROUTER_API_KEY");

    if api_key is None:
        raise RuntimeError("api key not found!, please address.")

    #gather user input
    parser = argparse.ArgumentParser(description="ChatBot");
    parser.add_argument("user_prompt", type=str, help="user prompt")
    args = parser.parse_args();
    #create a client
    client = openai_client(api_key);

    #print the prompt tokens and response tokens
    messages = [
        {"role": "user", "content": args.user_prompt}
    ]

    #get response from the model
    response = client.chat.completions.create(
        model = "openrouter/free",
        messages=messages,

    )
    prompt_tokens = response.usage.prompt_tokens;
    completion_tokens = response.usage.completion_tokens;
    print("User prompt", args.user_prompt)
    print("Prompt tokens: ", prompt_tokens)
    print("Response tokens: ", completion_tokens)
    print("Response:\n", response.choices[0].message.content)





if __name__ == "__main__":
    main()
