#!/usr/bin/python3
"""
It query subscribers on given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns total number of subscribers on given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "user-agent": "request"
    }
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return 0
    results = r.json().get("data")
    return results.get("subscribers")
