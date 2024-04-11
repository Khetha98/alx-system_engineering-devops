#!/usr/bin/python3
"""
100-count
"""

import requests
from collections import Counter


def count_words(subreddit, word_list, after=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data["data"]["children"]

    titles = [post["data"]["title"].lower().rstrip('.,!_') for post in posts]

    counts = Counter(titles)

    for word in word_list:
        word_count = counts.get(word.lower(), 0)
        if word_count > 0:
            print(f"{word.lower()}: {word_count}")

    after = data["data"]["after"]

    if after is not None:
        count_words(subreddit, word_list, after)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        count_words(subreddit, word_list)
