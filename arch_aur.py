#!/usr/bin/env python3

import requests
import feedparser
import html
import time
import re

quantity = 10
urls = ('https://archlinux.org/feeds/packages/all/stable-repos',
        'https://aur.archlinux.org/rss/modified')

length_line = 50
spaces = 2
pause = 10

news = [''] * quantity

for url in urls:
    try:
        response = requests.get(url=url, timeout=5)
        feeds = feedparser.parse(response.content)
    except Exception:
        feeds = None

    if feeds is None:
        exit()

    counter = 0
    for feed in feeds.entries:
        if 'category' in feed:
            if str(feed.category).lower() not in ('extra', 'core', 'multilib'):
                continue

        # text = html.unescape(feed.title).replace('x86_64', '')[:int(length_line/2)-spaces]
        text = html.unescape(feed.title)
        text = re.sub(r'( x86_64)|( any)', '', text)[:int(length_line/2)-spaces]
        line = f"{text}{(int(length_line/2)-len(text))*' '}"[:length_line]
        news[counter] += line
        counter += 1
        if counter >= quantity:
            break

    if counter < quantity:
        for i in range(quantity):
            if news[i] == '':
                news[i] = ' ' * int(length_line/2)

    time.sleep(pause)

news = [f'${{voffset 5}}$hr${{voffset 5}}',] + news
print('\n'.join(news))
# print(news)
