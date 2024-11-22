#!/usr/bin/env python3

import subprocess

import feedparser
import html
import requests
from requests.packages import urllib3

# --------------------------------------------------------------------------------

# vpn_id='nl-170068'

url = ""    # Ссылка на rss/atom
quantity = 3                                        # Количество выводимых ответов
output_len = 50                                     # Длина выводимой строки

# --------------------------------------------------------------------------------

command = f"nmcli c show --active"
active_connections = subprocess.check_output(command, shell=True)

if b'vpn' not in active_connections:
    exit()

try:
    urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)
    response = requests.get(url=url, verify=False, timeout=5)
except Exception:
    exit()

output = [f'${{voffset 5}}$hr${{voffset 5}}',]

feeds = feedparser.parse(response.content)
counter = 1
for feed in feeds.entries:
    dateTime = html.unescape(feed.updated)
    dateTime = dateTime.split('+')[0]
    dateTime = dateTime.replace('T', ' ')
    dateTime = dateTime[5:-3]

    line = f'{dateTime} | {feed.author} | {feed.title}'
    output.append(line[:output_len])

    counter += 1
    if counter > quantity:
        break
print('\n'.join(output))
