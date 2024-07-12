#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if not isinstance(subreddit, str) or not subreddit:
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if subreddit does not exist
        if response.status_code == 404:
            return 0
        # If request is successful, extract the number of subscribers
        response_data = response.json()
        return response_data.get("data", {}).get("subscribers", 0)
    except requests.RequestException:
        return 0
