import tweepy
import os
from dotenv import load_dotenv
from quote_data import choose_quote, df_dict
import time
import datetime
import schedule
import logging

load_dotenv()
logging.getLogger().setLevel(logging.INFO)

bearer_token = os.getenv("BEARER_TOKEN")
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_key = os.getenv("ACCESS_KEY")
access_secret = os.getenv("ACCESS_SECRET")

client = tweepy.Client(
    bearer_token=bearer_token, 
    consumer_key=consumer_key, 
    consumer_secret=consumer_secret,
    access_token=access_key,
    access_token_secret=access_secret
    )


def create_tweet():
    tweet_info = choose_quote(df_dict)
    logging.info(f"Tweet: {tweet_info}")
    client.create_tweet(text=tweet_info)
    logging.info(f"Tweet created successfully at {datetime.datetime.now()}")


# Time in UTC
schedule.every().day.at("15:30").do(create_tweet)
schedule.every().day.at("17:00").do(create_tweet)
schedule.every().day.at("23:00").do(create_tweet)

while True:
    # schedule.run_pending()
    # time.sleep(1)
    create_tweet()
    time.sleep(15)