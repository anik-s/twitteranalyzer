import datetime
import os
from dateutil.parser import parse
import json
import boto3
import botocore
# from serverless_sdk import capture_exception
from collections.abc import Iterable


dynamodb = boto3.resource('dynamodb')
cloudwatch = boto3.client('cloudwatch')

table_name = os.environ['tweet_table']


def remove_empty_string(dic):
    if isinstance(dic, Iterable):
        for e in dic:
            if isinstance(dic[e], dict):
                dic[e] = remove_empty_string(dic[e])
            if isinstance(dic[e], str) and dic[e] == "":
                dic[e] = None
            if isinstance(dic[e], list):
                for entry in dic[e]:
                    remove_empty_string(entry)
    return dic


def publish_to_cloudwatch(tweet):
    """
    publishes country data to cloudwatch for the tweet
    :param tweet: the tweet dict
    """
    country = "NOT_PROVIDED"  # if country information is not provided then this value is used to publish metric
    if tweet['place'] is not None:
        country = tweet['place']['country']
    dt = parse(tweet["created_at"])
    cloudwatch.put_metric_data(
        Namespace=os.environ['metric_namespace'],
        MetricData=[
            {
                'MetricName': 'NumberOfTweets',
                'Dimensions': [
                    {
                        'Name': 'Country',
                        'Value': country
                    },
                ],
                'Timestamp': dt,
                'Value': 1,
            }
        ]
    )


def store_to_db(tweet):
    """
    :param tweet: the tweet dict
    raises exception if anything goes wrong
    """
    # store to db
    table = dynamodb.Table(table_name)
    validated_tweet = remove_empty_string(tweet)
    try:
        table.put_item(Item=validated_tweet)  # store to dynamo db
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            print("Tweet already exists. No need to store to DB ...")
        else:
            raise


def tweet_processor_handler(event, context):
    """
    the lambda handler triggered by sqs message
    :param event:
    :param context:
    """
    try:
        for record in event['Records']:
            ts = record['body']
            tweet = json.loads(ts)
            store_to_db(tweet)
            publish_to_cloudwatch(tweet)
    except Exception as e:
        # capture_exception(e)
        print(e)
        raise

