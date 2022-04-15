#-*- coding: utf-8 -*-

import tweepy
import os
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import date

# Import keys from .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
CK = os.environ.get("CK")
CS = os.environ.get("CS")
AT = os.environ.get("AT")
AS = os.environ.get("AS")
YEAR = os.environ.get("YEAR")
MONTH = os.environ.get("MONTH")
DAY = os.environ.get("DAY")
EVENT = os.environ.get("EVENT")
HASHTAG = os.environ.get("HASHTAG")

# Generate Twitter objects
client = tweepy.Client(consumer_key=CK,
                       consumer_secret=CS,
                       access_token=AT,
                       access_token_secret=AS)

def main():
  end_day = date(int(YEAR), int(MONTH), int(DAY))
  today = date.today()
  delta = end_day - today
  days = delta.days
  
  tweet = EVENT + "まであと" + str(days) + "日 #" + HASHTAG

  # Call Twitter API to tweet
  response = client.create_tweet(text=tweet)
  print(response)

if __name__ == '__main__':
  main()