import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending"
#Doesn't execute the JavaScript code
response = requests.get(YOUTUBE_TRENDING_URL)

print(response.status_code)

with open("trending_vodeos.html","w") as f:
  f.write(response.text)

doc = BeautifulSoup(response.text,'html.parser')
print('Page title: ', doc.title)

#Find all the video divs
video_divs = doc.find_all('div',class_='style-scope ytd-video-renderer')
print(f"Found {len(video_divs)} videos" )