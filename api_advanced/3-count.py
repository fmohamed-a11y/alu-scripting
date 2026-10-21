#!/usr/bin/python3
"""Recursively counts keywords in the hot post titles of a subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Prints a sorted count of the given keywords in hot post titles."""
    if counts is None:
        counts = {w.lower(): 0 for w in word_list}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-api-advanced/1.0"}
    params = {"limit": 100, "after": after}
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        return
    data = res.json().get("data", {})
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for word in title.lower().split():
            if word in counts:
                counts[word] += 1
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    totals = {}
    for w in word_list:
        key = w.lower()
        totals[key] = totals.get(key, 0) + counts[key]
    for word, count in sorted(totals.items(), key=lambda x: (-x[1], x[0])):
        if count > 0:
            print("{}: {}".format(word, count))
