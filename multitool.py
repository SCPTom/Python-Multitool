import requests
import os
import json

### Variables

logo = f"""
\033[38;2;255;0;0m  █████████    █████████     ███████████                   ████ 
\033[38;2;255;128;0m ███░░░░░███  ███░░░░░███   ░█░░░███░░░█                  ░░███ 
\033[38;2;255;255;0m░███    ░░░  ███     ░░░    ░   ░███  ░   ██████   ██████  ░███ 
\033[38;2;128;255;0m░░█████████ ░███                ░███     ███░░███ ███░░███ ░███ 
\033[38;2;0;255;0m ░░░░░░░░███░███                ░███    ░███ ░███░███ ░███ ░███ 
\033[38;2;0;255;128m ███    ░███░░███     ███       ░███    ░███ ░███░███ ░███ ░███ 
\033[38;2;0;255;255m░░█████████  ░░█████████        █████   ░░██████ ░░██████  █████
\033[38;2;0;128;255m ░░░░░░░░░    ░░░░░░░░░        ░░░░░     ░░░░░░   ░░░░░░  ░░░░░ \033[38;2;255;255;255m
                                                                
                                                                
                                                                
"""

### Functions

def getHwid():
    print("\033[38;2;255;0;0mCPU Serial\033[38;2;255;255;255m")
    print(os.system("wmic cpu get ProcessorId"))

    print("\033[38;2;255;0;0mDisk Serial\033[38;2;255;255;255m")
    print(os.system("wmic diskdrive get SerialNumber"))

    print("\033[38;2;255;0;0mMotherboard Serial\033[38;2;255;255;255m")
    print(os.system("wmic baseboard get SerialNumber"))

import requests

def send_to_discord(webhook_url, content, botName):
    data = {
        "content": content,
        "username": botName  # This is optional, it sets the bot's name in Discord.
    }
    
    response = requests.post(webhook_url, json=data)
    
    if response.status_code == 204:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message: {response.status_code} - {response.text}")


while True:
    os.system(f'title SCTOOL - BY SCPROGRAMS')
    os.system("cls")
    print(logo)
    print("[1] IP Lookup")
    print("[2] Webhook Sender")
    print("[3] Show HWID")
    print("")
    x = input("Option: \033[38;2;0;128;255m")

    if x == "1":
        print("\033[38;2;255;255;255m")
        os.system("cls")
        print("IP Lookup")
        ip = input("Enter IP: ")
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
        print("")
        print(f"\033[38;2;255;0;0mCountry:\033[38;2;255;255;255m {data["country"]}")
        print(f"\033[38;2;255;0;0mCity:\033[38;2;255;255;255m {data["city"]}")
        print(f"\033[38;2;255;0;0mRegion:\033[38;2;255;255;255m {data["regionName"]}")
        print(f"\033[38;2;255;0;0mTimeZone:\033[38;2;255;255;255m {data["timezone"]}")
        print("")
        pause = input("Press Enter to return...")


    if x == "2":
        print("\033[38;2;255;255;255m")
        os.system("cls")
        webhook = input("Webhook URL: ")
        message = input("Message: ")
        botName = input("Bot Name: ")
        send_to_discord(webhook, message, botName)
        pause = input("Press Enter to return...")


    if x == "3":
        print("\033[38;2;255;255;255m")
        os.system("cls")
        getHwid()
        pause = input("Press Enter to return...")