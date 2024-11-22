#!/usr/bin/env python3

import requests
import feedparser
import html
import re

urls = (
    "https://blog.freecad.org/rss",)

quantity = 1
row_length = 50

output = []
for url in urls:
    # print(url)

    try:
        response = requests.get(url=url, timeout=3)
    except Exception:
        response = None

    if response:
        feeds = feedparser.parse(response.content)
        # print(feeds)
        count = 0
        for feed in feeds.entries:
            text = html.unescape(feed.title)
            text = re.sub(r'2024$', '', text)   # $ - text ends with '2024'
            # print(text)
            if len(urls) == 2:
                text = text[:int(row_length/2)-2]
            output.append(text)
            count += 1
            if count >= quantity: break

print('  '.join(output))
