#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)

    if response.status_code != 200:
        return 0

    try:
        results = response.json()
        if 'data' in results and 'subscribers' in results['data']:
            return results['data']['subscribers']
        else:
            print("Error: Malformed JSON response")
            return 0
    except Exception as e:
        print("Error:", e)
        return 0
