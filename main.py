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

# Generate Twitter objects
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

def main():
  end_day = date(int(YEAR), int(MONTH), int(DAY))
  today = date.today()
  delta = end_day - today
  days = delta.days + 1
  
  tweet = event + "まであと" + str(days) + "日です。"

  # Call Twitter API to tweet
  api.update_status(tweet)

if __name__ == '__main__':
  main()