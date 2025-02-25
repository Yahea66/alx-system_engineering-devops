#!/usr/bin/python3
""""
module to retrieve subscribers data
"""


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    """
    import requests

    res = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                       headers={"USER-AGENT": "My-User-Agent"},
                       allow_redirects=False)

    if res.status_code >= 300:
        return 0

    return res.json().get("data").get("subscribers")
