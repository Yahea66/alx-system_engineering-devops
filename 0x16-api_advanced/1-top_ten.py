#!/usr/bin/python3
"""
Module 2 to querying data from reddit API
"""


def top_ten(subreddit):
    """
    a function that queries the Reddit API
    and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    import requests

    res = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                       .format(subreddit),
                       headers={"USER-AGENT": "MY-USER-AGENT"},
                       allow_redirects=False)

    if res.status_code >= 300:
        print('None')

    else:
        for post in res.json().get("data").get("children"):
            print(post.get("data").get("title"))
