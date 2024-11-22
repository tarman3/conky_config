#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------- Импорт библиотек ---------------------------

import requests
from datetime import datetime, timedelta
import re

# ---------------------------- Параметры -------------------------------

url_api = 'https://api.github.com/repos/FreeCAD/FreeCAD/commits'
number_news = 8
output_len = 50

# ----------------------------- Сенарий --------------------------------

d = datetime.today() - timedelta(hours=24)
since = d.strftime(f"%Y-%m-%dT%H-%M-%SZ")
#print(since)

request_string = f'{url_api}'#?since={since}&page=1'
#print(request_string,'\n')

output = []

try:
    data = requests.get(request_string, timeout=5).json()
    # print(len(data))
except Exception:
    data = None
    exit()

if len(data) > 0:
    count = 0
    for commit in data:
        commit_title = commit["commit"]["message"]
        commit_title = re.sub(r'(\r\n)|(\n)+', ' ', commit_title)

        output.append(commit_title[:output_len])
        count += 1
        if count >= number_news: break
    print('\n'.join(output))
