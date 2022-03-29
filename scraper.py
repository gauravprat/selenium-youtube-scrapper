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

  
if __name__ == "__main__":
  print('Creating driver')
  driver = get_driver()

  print('Fetching trending videos ')
  videos = get_videos(driver) 

  print(f'Found {len(videos)} videos')