#!/usr/bin/python3
"""Recursively gets the titles of all hot posts of a subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of all hot post titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-api-advanced/1.0"}
    params = {"limit": 100, "after": after}
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        return None
    data = res.json().get("data", {})
    titles = [p.get("data", {}).get("title")
              for p in data.get("children", [])]
    hot_list = hot_list + titles
    after = data.get("after")
    if after is None:
        return hot_list if hot_list else None
    return recurse(subreddit, hot_list, after)
