#!/usr/bin/env python3

import requests
import feedparser
import html

urls = (
    "https://www.opennet.me/opennews/opennews_all_utf.rss",
    # "/home/user/Downloads/feed.atom",
    )

quantity = 5
row_length = 50

for url in urls:
    # print(url)

    try:
        response = requests.get(url=url, timeout=5)
    except Exception:
        response = None

    if response:
        feeds = feedparser.parse(response.content)
        # print(feeds)
        count = 0
        output = [f'${{voffset 5}}$hr${{voffset 5}}',]
        for feed in feeds.entries:
            output.append(html.unescape(feed.title)[:row_length])
            count += 1
            if count >= quantity: break
        print('\n'.join(output))
