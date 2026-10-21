#!/usr/bin/python3
"""Queries the Reddit API for a subreddit's subscriber count."""
import requests


def number_of_subscribers(subreddit):
    """Returns the total subscribers of a subreddit, or 0 if invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alu-api-advanced/1.0"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    return res.json().get("data", {}).get("subscribers", 0)
