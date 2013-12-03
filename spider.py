#!/usr/bin/env python
# coding: utf-8

import feedparser
from jinja2 import Environment, FileSystemLoader
import os

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

env = Environment(loader=FileSystemLoader(os.path.join(PROJECT_PATH, 'templates')))

def main():
    # En lajvprenumeration från hitta.sverok.se!
    kwargs = {}
    feed = feedparser.parse('http://hitta.sverok.se/subscriptions/get/c4169383d92e705ba18b884ee825b0e6', **kwargs)

    items = []
    fields = ['title', 'author', 'links', 'summary']
    for x in feed.entries:
        item            = {f : x[f] for f in fields}
        item['links']   = [y['href'] for y in item['links']]
        item['summary'] = item['summary'].replace('\n\n', '</p>\n<p>').replace('\n', '<br>\n')
        items.append(item)

    template = env.get_template('index.html')
    print template.render(items=items).encode('utf-8')

if __name__ == '__main__':
    main()

