#from functions.apiKeys import load_enviorn
import argparse
from prompts import system_prompt;
from functions.openai import openai_client;
import os;
import json;
from dotenv import load_dotenv;
from functions.call_functions import available_functions;

def main():
    print("hello from ai agent")
    #api_key = load_enviorn();
    load_dotenv();
    api_key = os.environ.get("OPENROUTER_API_KEY");

    if api_key is None:
        raise RuntimeError("api key not found!, please address.")

    #gather user input
    parser = argparse.ArgumentParser(description="ChatBot");
    parser.add_argument("user_prompt", type=str, help="user prompt");
    parser.add_argument("--verbose", action="store_true", help="enable verbose output");
    args = parser.parse_args();
    #create a client
    client = openai_client(api_key);

    #print the prompt tokens and response tokens
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt}
    ]

    #get response from the model
    response = client.chat.completions.create(
        model = "openrouter/free",
        messages=messages,
        tools=available_functions,
    )

    #grab the message
    message = response.choices[0].message;
    if message.tool_calls is not None:
        for tool_call in message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}");
            print(f"Calling function: {tool_call.function.name}({function_args})")


    prompt_tokens = response.usage.prompt_tokens;
    completion_tokens = response.usage.completion_tokens;
    if args.verbose:
        print("User prompt: ", args.user_prompt)
        print("Prompt tokens: ", prompt_tokens)
        print("Response:\n", response.choices[0].message.content)
        print("Response tokens: ", completion_tokens)
    else:
        print("Response:\n", response.choices[0].message.content)



if __name__ == "__main__":
    main()
