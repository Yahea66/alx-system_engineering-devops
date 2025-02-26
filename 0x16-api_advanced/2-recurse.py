#!/usr/bin/python3
"""
Mdule 3 to recrusively fetch the hot post titles
"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
     returns a list containing the titles
     of all hot articles for a given subreddit
    """
    import requests

    res = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       params={"count": count, "after": after},
                       headers={"USER-AGENT": "MY-USER-AGENT"},
                       allow_redirects=False)

    if res.status_code >= 400:
        return None

    lis = hot_list + [post.get("data").get("title")
                      for post in res.json().get("data").get("childern")]

    result = res.json()
    if not result.get("data").get("after"):
        return lis

    return recurse(subreddit, lis, result.get("data").get("count"),
                   result.get("data").get("after"))
