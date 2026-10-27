#from functions.apiKeys import load_enviorn
import argparse
import sys;
from prompts import system_prompt;
from functions.openai import openai_client;
import os;
import json;
from dotenv import load_dotenv;
from functions.call_functions import available_functions, call_function;


def main():
    print("hello from ai agent")
    #api_key = load_enviorn();
    load_dotenv();
    api_key = os.environ.get("OPENROUTER_API_KEY");
    backup_api_key = os.environ.get("OPENROUTER_BACKUP_API_KEY")

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
    try:
        for _ in range(20):
            #get response from the model
            response = client.chat.completions.create(
                model = "openrouter/free",
                messages=messages,
                tools=available_functions,
            )

            message = response.choices[0].message
            messages.append(message)
            if message.tool_calls is not None:
            #grab the message or messages
                for tool_call in message.tool_calls:
                    result_message = call_function(tool_call, verbose=args.verbose)

                    if result_message["content"] is None:
                        raise Exception("error: content is empty on result message")
                        break
                    if args.verbose:
                        print(f"-> {result_message['content']}")

                    messages.append(result_message)
            else:
                print(message.content)
                break
        else:
            print("nothing to display")
            sys.exit(1)

    except Exception as e:
        print(f"Error: {e}")

#agent loop ends here
if __name__ == "__main__":
    main()
