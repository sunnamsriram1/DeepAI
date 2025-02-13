import pyttsx3
from openai import OpenAI



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



# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    #api_key=apiky.api,
    api_key="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",  # Make sure to keep the key secure
)

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Set properties for voice (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
engine.setProperty('voice', voices[1].id)  # Set female voice (index 1 usually)

# Initialize conversation history
conversation_history = []

while True:
    # Get user input
    user_input = input("You: ")

    # If the user types 'exit', break the loop
    if user_input.lower() == 'exit':
        print("Exiting conversation.")
        break

    # Add user message to conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Send the conversation to the OpenAI model for a response
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional
            "X-Title": "<YOUR_SITE_NAME>",  # Optional
        },
        model="deepseek/deepseek-r1-distill-llama-70b",  # Change model if needed
        messages=conversation_history
    )

    # Get the model's response and add it to the conversation history
    model_response = completion.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": model_response})

    # Print the model's response
    print(f"AI: {model_response}")
    
    # Use pyttsx3 to speak the assistant's response
    engine.say(model_response)
    engine.runAndWait()
