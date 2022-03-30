import pandas as pd
import time
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending"

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--headless')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_videos(driver):
  VIDEO_DIV_TAG = 'ytd-video-renderer'
  driver.get(YOUTUBE_TRENDING_URL)
  time.sleep(3)
  videos = driver.find_elements(By.TAG_NAME,value=VIDEO_DIV_TAG)
  print(f'Found {len(videos)} videos')
  return videos

def parse_video(video):
  title_tag = video.find_element(By.ID,"video-title")
  title = title_tag.text
  url = title_tag.get_attribute('href')  
  thumbnail_url = video.find_element(By.TAG_NAME,"img").get_attribute('src')
  channel_name = video.find_element(By.CLASS_NAME, "yt-formatted-string").text
  video_views = video.find_element(By.ID,"metadata-line").text[0:4]
  

  return {
    'title': title,
    'url': url,
    'thumbnail_url': thumbnail_url,
    'channel_name': channel_name,
    'views': video_views    
  }

  
if __name__ == "__main__":
  print('Creating driver')
  driver = get_driver()

  print('Fetching trending videos ')
  videos = get_videos(driver) 
  print(f'Found {len(videos)} videos')
  video = videos[0]
  print("Parsing the Top10 videos")

  videos_data = [parse_video(video) for video in videos ]
  print(videos_data)

  print("Save the data to the CSV")
  videos_df = pd.DataFrame(videos_data)
  print(videos_df)
  videos_df.to_csv('trending_Videos.csv')
  
