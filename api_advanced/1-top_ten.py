#!/usr/bin/python3
"""Prints the title of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Prints the first 10 hot post titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "PostmanRuntime/7.35.0"}
    params = {"limit": 10}
    try:
        res = requests.get(url, headers=headers, params=params,
                           allow_redirects=False)
        posts = res.json().get("data").get("children")
        for post in posts[:10]:
            print(post.get("data").get("title"))
    except Exception:
        print(None)
