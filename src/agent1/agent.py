from openai import OpenAI
from config import OPENAI_API_KEY, MODEL, INITIAL_PROMPT
from colorama import Fore, Back, Style, init



client = OpenAI(api_key=OPENAI_API_KEY)

message = [
    INITIAL_PROMPT
]


print(f"{Fore.GREEN}Welcome to the Hafez Poems Chatbot!{Style.RESET_ALL}")
print(f"{Fore.GREEN}You can ask me anything about the Hafez Poems.{Style.RESET_ALL}")
print(f"{Fore.GREEN}To exit, type 'exit'.{Style.RESET_ALL}")

while True:
    user_input = input(f"{Fore.BLUE}You: {Style.RESET_ALL}")
    if user_input.lower() == "exit":
        break
    message.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(model=MODEL, messages=message)
    message.append({"role": "assistant", "content": response.choices[0].message.content})
    print(f"{Fore.RED}AI: {Style.RESET_ALL}{response.choices[0].message.content}")


