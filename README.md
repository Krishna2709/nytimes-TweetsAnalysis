# :one: Analyzing tweets from @nytimes using Prefect :toolbox:
#### @nytimes tweets analysis :chart_with_upwards_trend:
```
1. Authenticating using Twitter API tokens
2. Extracting tweet data id, datetime of created tweet, tweet text
3. Saving the extracted data into a csv file
4. Automating the above process using Prefect - extracting 100 most recent tweets every 3 days
```
#### To-do :hammer_and_wrench:
```
1. Dockerize the application
2. ETL operations - Data Pre-processing
3. Exploratory Data Analysis
4. Analytics dashboard using D3.js
5. Tweets Classification model and Updating the dashboard
6. Dockerizing the whole application
```

# :two: Analyzing tweets using AWS
#### @nytimes tweets analysis on AWS :chart_with_upwards_trend:
```
1. Authenticating using Twitter API tokens
2. Extracting tweet data id, datetime of created tweet, tweet text
3. Saving the extracted data into a csv file in a S3 bucket
4. Automating the above process using AWS Lambda, EventBridge
5. Using Cloud9 to create an EC2 instance to install the required python packages for AWS Lambda
6. Saving the tweets into a DynamoDB table for further analysis
```

#### AWS Tools :hammer_and_pick:
```
 1. Sagemaker
 2. EC2
 3. Cloud9
 4. S3
 5. Lambda
 6. EventBridge
 7. DynamoDB
```

## :briefcase: Resources
1. [Tweepy](https://docs.tweepy.org/en/stable/index.html)
2. [Prefect](https://docs.prefect.io/)
3. [SQLite](https://docs.python.org/3/library/sqlite3.html)
4. [AWS Sagemaker connection to S3 bucket](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-ex-notebook.html)
5. [Importing modules into AWS Lambda](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-import-module-error-python/)
6. [AWS S3 data into DynamoDB](https://aws-dojo.com/excercises/excercise39/)
