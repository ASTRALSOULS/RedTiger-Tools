from Options.Options import *

import requests
import json
import time

Title("Webhook Spammer")

def send_webhook_message(webhook_url, message):
    payload = {'content': message}
    headers = {'Content-Type': 'application/json'}


    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


webhook_url = input(f"{color.RED}\n[?] | URL Webhook -> {color.RESET}")
if webhook_url.lower().startswith("https://discord.com/api/webhooks"):

    message_to_send = input(f"{color.RED}[?] | Message -> {color.RESET}")

    def repetition_action(nombre_de_repetitions):
     for i in range(1, nombre_de_repetitions + 1):
        try:
            send_webhook_message(webhook_url, message_to_send)
            print(f'{color.LIGHTRED_EX}[+] {color.RED}Message Send | Message: "{color.CYAN}{message_to_send}{color.RED}" | Webhook: "{color.CYAN}{webhook_url}{color.RED}" | n°{i}{color.RESET}')
        except:
            print(f'{color.LIGHTRED_EX}[X] {color.RED}Erreur | Message: "{color.CYAN}{message_to_send}{color.RED}" | Webhook: "{color.CYAN}{webhook_url}{color.RED}"{color.RESET}')
            time.sleep(1)
else:
    ErrorUrl
                
try:
        nombre_repetitions = int(input(f"{color.RED}[?] | Number of Repetitions -> {color.RESET}"))
        repetition_action(nombre_repetitions)
except:
        ErrorNumber

LAPprint(f"{color.RED}\n{nombre_repetitions} message(s) sent !")
time.sleep(5)
Reset()

        