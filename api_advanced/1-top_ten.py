#!/usr/bin/python3
"""Prints the title of the first 10 hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Prints the first 10 hot post titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-api-advanced/1.0"}
    params = {"limit": 10}
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return
    for post in res.json().get("data", {}).get("children", []):
        print(post.get("data", {}).get("title"))
