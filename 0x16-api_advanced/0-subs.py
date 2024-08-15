#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit
    the active subscribers.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
