# AWS-nytimes-TweetsAnalysis
#### @nytimes tweets analysis on AWS using <br>
Extracting and Saving tweets from @nytimes [nytimesTweetsExtraction](nytimesTweetExtraction.ipynb)
```
1. Authenticating using Twitter API tokens
2. Extracting tweet data id, datetime of created tweet, tweet text
3. Saving the extracted data into a csv file in a S3 bucket
4. Automating the above process using AWS Lambda, EventBridge
5. Using Cloud9 to create an EC2 instance to install the required python packages for AWS Lambda
6. Saving the tweets into a DynamoDB table for further analysis
```

### AWS Tools:
```
 1. Sagemaker
 2. EC2
 3. Cloud9
 4. S3
 5. Lambda
 6. EventBridge
 7. DynamoDB
```

### Resources:
1. [Tweepy](https://docs.tweepy.org/en/stable/index.html)
2. [SQLite](https://docs.python.org/3/library/sqlite3.html)
3. [AWS Sagemaker connection to S3 bucket](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-ex-notebook.html)
4. [Importing Modules into AWS Lambda](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-import-module-error-python/)
5. [AWS S3 data into DynamoDB](https://aws-dojo.com/excercises/excercise39/)
