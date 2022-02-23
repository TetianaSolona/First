import concurrent.futures
import json
import requests

def subreddit_url():
    sub_url = ['chemistry', 'scient', 'pharm']
    urls = []
    for sub in sub_url:
        url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={sub}"
        urls.append(url)
    return urls


def get_subreddit_comment(url):
    response = requests.get(url)
    if response.ok:
        data = response.json()
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

with concurrent.futures.ThreadPoolExecutor(3) as executor:
    data = []
    for url in subreddit_url():
        data.append(executor.submit(get_subreddit_comment, url))