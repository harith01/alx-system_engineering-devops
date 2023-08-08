#!/usr/bin/python3
"""Queries Reddit API and and prints the titles of the
first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """Returns top 10 posts for a subreddit"""
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced:project:Harith'}
    params = {'limit': 10}
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return
    for post in res.json().get("data", {}).get("children", {}):
        print(post.get('data', {}).get('title'))
