import time
import random
import os

# Signatur
os.system('cls' if os.name == 'nt' else 'clear')

name = """

███╗░░██╗███████╗░██████╗░█████╗░███████╗████████╗░██████╗
████╗░██║██╔════╝██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝
██╔██╗██║█████╗░░╚█████╗░██║░░██║█████╗░░░░░██║░░░╚█████╗░
██║╚████║██╔══╝░░░╚═══██╗██║░░██║██╔══╝░░░░░██║░░░░╚═══██╗
██║░╚███║███████╗██████╔╝╚█████╔╝██║░░░░░░░░██║░░░██████╔╝
╚═╝░░╚══╝╚══════╝╚═════╝░░╚════╝░╚═╝░░░░░░░░╚═╝░░░╚═════╝░

"""

name_lines = name.split("\n")

name_placeholder = [[' ']*len(line) for line in name_lines]

characters_in_name = [char for char in name if char != ' ' and char != '\n']
total_characters = len(characters_in_name)

initial_pause = 0.2
final_pause = 0.000000000000001
pause_step = (initial_pause - final_pause) / (total_characters * 2)

current_pause = initial_pause

while characters_in_name:
    for i, line in enumerate(name_lines):
        for j, char in enumerate(line):

            if char != ' ' and name_placeholder[i][j] == ' ' and random.random() < 0.05 + 0.95 * (1 - len(characters_in_name) / total_characters):
                name_placeholder[i][j] = char
                characters_in_name.remove(char)

    print('\033[H')
    print('\n'.join([''.join(line) for line in name_placeholder]))
    time.sleep(current_pause)
    current_pause = max(final_pause, current_pause - pause_step)

def typing_animation(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()


typing_animation("created by Nepomuk Crhonek\n")


def print_big_title(text):
    # Create a big title using the input text
    big_title = ''
    for char in text:
        big_title += char.upper() + ' '

    # Print the big title
    print(big_title)


print_big_title("change currency\n")

# program start

import urllib.request
import json

api_key = "7a2fc537b131f27b688c5a68"

def convert_currency():
    base_currency = input("Enter the currency code you want to convert from: ")
    target_currency = input("Enter the currency code you want to convert to: ")
    amount = float(input("Enter the amount to convert: "))

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

        if data["result"] == "error":
            error_message = data["error-type"]
            print("Error:", error_message)
        else:
            exchange_rate = data["conversion_rate"]
            converted_amount = amount * exchange_rate
            print(f"Conversion result: {amount} {base_currency} = {converted_amount} {target_currency}")

convert_currency()