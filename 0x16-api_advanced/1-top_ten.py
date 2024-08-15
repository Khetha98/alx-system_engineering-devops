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
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}
    
    try:
        req = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if req.status_code == 200:
            try:
                data = req.json()
                posts = data.get("data", {}).get("children", [])
                if not posts:
                    print(None)
                    return
                for post in posts:
                    title = post["data"].get("title")
                    if title:
                        print(title)
            except ValueError:
                print(None)
        else:
            print(None)
    except requests.RequestException:
        print(None)
