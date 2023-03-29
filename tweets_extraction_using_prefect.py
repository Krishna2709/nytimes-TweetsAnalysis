import os
import pandas as pd
import prefect
import tweepy

from dotenv import load_dotenv
from prefect import task, flow

@task
def extract_tweets(token: str, tweeter_handle: str) -> list:
    
    # Authenticating
    client = tweepy.Client(bearer_token=token)

    #  Communicating with @nytimes
    response = client.search_recent_tweets(tweeter_handle, tweet_fields=["id", "created_at", "text"], max_results=100)
    
    # Extracting tweets from the response
    tweets = response.data
    data = [(tweet.id, tweet.created_at, tweet.text, len(tweet.text)) for tweet in tweets]
    
    return data

@task
def save_tweets_to_csv(data: list) -> None:
    data = pd.DataFrame(data, columns=['id', 'created_at', 'tweet', 'tweet_length'])
    data.to_csv('tweets.csv', index=False, header=True)

@flow
def extract_tweets_flow(token: str, tweeter_handle: str):
    tweets = extract_tweets(token, tweeter_handle="nytimes")
    save_tweets_to_csv(tweets)

if __name__ == "__main__":

    #Twitter API credentials
    load_dotenv()
    os.getenv("TWITTER_BEARER_TOKEN")

    token = os.getenv("TWITTER_BEARER_TOKEN")

    # Twitter handle to extract tweets from
    tweeter_handle = "nytimes"
 
    extract_tweets_flow(token, tweeter_handle)