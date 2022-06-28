import requests

def neget(cat):
    url = f"https://inshortsv2.vercel.app/news?type={cat}"
    res = requests.get(url).json()
    return res