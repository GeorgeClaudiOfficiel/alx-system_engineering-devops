#!/usr/bin/python3
"""
A function that queries the Reddit API then returns the number of subscribers
for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API then returns the number of
    subscribers for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
