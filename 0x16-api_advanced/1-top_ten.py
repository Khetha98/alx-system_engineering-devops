#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API.
    If not a valid subreddit, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 10}

    req = requests.get(url, params=params)

    if req.status_code == 200:

        for get_data in req.json()["data"]["children"]:

            dat = get_data["data"]
            title = dat["title"]
            print(title)
    else:
        print(None)
