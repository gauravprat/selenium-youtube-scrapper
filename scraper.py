import requests

YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending"
response = requests.get(YOUTUBE_TRENDING_URL)

print(response.status_code)