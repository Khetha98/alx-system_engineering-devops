#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit) -> int:
    """
    Queries the Reddit API and returns the number of subscribers

    Args:
        subreddit (str): subreddit to query

    Returns:
        (int): number of subscribers
    """
    # Returns the number of subscribers for a given subreddit
    base_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        request = requests.get(base_url, headers={'User-Agent': 'Agent Uche'}, allow_redirects=False)
        data = request.json()
        return data['data']['subscribers']
    except Exception:
        return 0
