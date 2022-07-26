import json
import boto3
from io import StringIO
import pandas as pd
import tweepy
import os


# Helper function to save data in a S3 Bucket
def save_to_s3(bucket, data):
    
    # Connecting to the S3 resource
    s3 = boto3.client('s3')
    s3_resource = boto3.resource('s3')
    
    # Calling a buffer
    csv_buffer = StringIO()
    
    # Creating a dataframe
    data = pd.DataFrame(data, columns=['id', 'created_at', 'tweet', 'tweet_length'])
    # Saving the dataframe into a csv file
    data.to_csv(csv_buffer)
    
    # Saving the csv file into the S3 bucket
    s3_resource.Object(bucket, 'nytimes.csv').put(Body=csv_buffer.getvalue())
    
    
# Helper function to extract tweets from @nytimes
def get_tweets(bucket, token):
    """
    To
        Authenticate with Bearer Token
        Extract the tweets
    
    Return
        100 tweets data
    """
    # Authenticating
    client = tweepy.Client(bearer_token=token)
    
    #  Communicating with @nytimes
    response = client.search_recent_tweets("nytimes", tweet_fields=["id", "created_at", "text"], max_results=100)
    
    # Extracting tweets from the response
    tweets = response.data
    data = [(tweet.id, tweet.created_at, tweet.text, len(tweet.text)) for tweet in tweets]
    
    # Saving to S3 bucket
    save_to_s3(bucket, data)


# Configurations
token = "*"
bucket = "twitter-analytics-database"


# Lambda function to extract and save tweets from @nytimes
def lambda_handler(event, context):
    # TODO implement
    get_tweets(bucket, token)
    return {
        'statusCode': 200,
        'body': json.dumps('Tweets Extracted!')
    }