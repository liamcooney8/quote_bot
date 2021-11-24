import tweepy
import os
from dotenv import load_dotenv
from quote_data import choose_quote, df_dict
from time import sleep

load_dotenv()

bearer_token = os.getenv("BEARER_TOKEN")
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_key = os.getenv("ACCESS_KEY")
access_secret = os.getenv("ACCESS_SECRET")

client = tweepy.Client(bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret,
                        access_token=access_key,
                        access_token_secret=access_secret)


while True:
    tweet_info = choose_quote(df_dict)
    print(f"\nTweet: {tweet_info}")
    client.create_tweet(text=tweet_info)
    print("\nSuccessfully Tweeted")
    sleep(10)
