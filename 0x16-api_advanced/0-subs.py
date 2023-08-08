#!/usr/bin/python3
"""Queries Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers of a subreddit"""
    res = requests.get('http://www.reddit.com/r/{}/about.json'.format(
                       subreddit), headers={'User-Agent': '0x16-api_advanced\
         harith'}).json()
    return res.get('data', {}).get('subscribers', 0)
