from openai import OpenAI
import apikey 

#apikey = "",



import requests
import datetime
import pytz
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Coded by string
coded_by = "SUNNAM_SRIRAM_1"

# Function to print the banner once

#colorama.init()

import os

os.system("clear")





def banner():
    print("""
    \033[41m=[===> Mr. Tom | https://github.com/sunnamsriram1 <===]=\n\033[0m""")
banner()



# ANSI escape codes for text colors
class colors:
    # Reset
    RESET = '\033[0m'

    # Regular colors
    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[0;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    WHITE = '\033[0;37m'

    # Bold colors
    BOLD_BLACK = '\033[1;30m'
    BOLD_RED = '\033[1;31m'
    BOLD_GREEN = '\033[1;32m'
    BOLD_YELLOW = '\033[1;33m'
    BOLD_BLUE = '\033[1;34m'
    BOLD_PURPLE = '\033[1;35m'
    BOLD_CYAN = '\033[1;36m'
    BOLD_WHITE = '\033[1;37m'

# Example usage
# print(colors.RED + "This is red text!" + colors.RESET)
# print(colors.BOLD_GREEN + "This is bold green text!" + colors.RESET)



coded_by = "SUNNAM_SRIRAM_1"

def print_banner():
    india_timezone = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(india_timezone).strftime("%Y-%m-%d %I:%M:%S.%f %p")[:-3]
    banner = f"""\t<ul>
        <li>{Fore.YELLOW}Coded by</li>
        <li>{Fore.WHITE}{coded_by}</li>
        <li>{Fore.GREEN}Today (India Time): {current_time}</li>
    </ul>\n\n"""
    print(banner)

print_banner()







# Initialize the OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=apikey.API_KEY,
    #api_key="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",
)   #api_key=apikey.API_KEY,

try:
    while True:
        # Get user input
        print("\n")
        #user_input = input("Enter your question (or type 'exit' to quit): ")
        user_input = input("""\033[41m|Enter Your Question or type 'exit' to 'quit'|\033[0m:""")

        # Check for exit condition
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Call the API
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional
                "X-Title": "<YOUR_SITE_NAME>",  # Optional
            },
            extra_body={},
            model="deepseek/deepseek-r1-distill-llama-8b",
            messages=[{"role": "user", "content": user_input}],
        )

        # Print the response
        print(completion.choices[0].message.content)

except KeyboardInterrupt:
    print("\nProcess interrupted. Exiting gracefully...")
