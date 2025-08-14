from openai import OpenAI
from config import OPENAI_API_KEY, MODEL, INITIAL_PROMPT
from colorama import Fore, Back, Style, init
from tools.registry import get_tools, call_tool
from classifier import sklearnclassifier, llmclassifier

client = OpenAI(api_key=OPENAI_API_KEY)


# classifier = sklearnclassifier() or llmclassifier()
classifier = llmclassifier()


messages = [
    INITIAL_PROMPT
]


print(f"{Fore.GREEN}Welcome to the Hafez Poems Chatbot!{Style.RESET_ALL}")
print(f"{Fore.GREEN}You can ask me anything about the Hafez Poems.{Style.RESET_ALL}")
print(f"{Fore.GREEN}To exit, type 'exit'.{Style.RESET_ALL}")
need_user_input = True

while True:
    if need_user_input:
        user_input = input(f"{Fore.BLUE}You: {Style.RESET_ALL}")
        if user_input.lower() == "exit":
            break
        if classifier.relevant(user_input):
            classifier.update(user_input, "relevant")
        else:
            classifier.update(user_input, "not_relevant")
            continue

        messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools= get_tools())
    message = response.choices[0].message
    messages.append(message.to_dict())
    if message.function_call:
        tool_name = message.function_call.name
        tool_args = message.function_call.arguments
        response = call_tool(tool_name, tool_args)
        messages.append({"role": "function", "name": tool_name, "content": response})
        need_user_input = False
        continue
    elif message.content:
        need_user_input = True
        print(f"{Fore.RED}AI: {Style.RESET_ALL}{message.content}")
        continue
    else:
        continue




