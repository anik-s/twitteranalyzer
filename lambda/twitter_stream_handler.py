import os
import boto3
import tweepy

consumer_key = os.environ['twitter_consumer_key']
consumer_secret = os.environ['twitter_consumer_secret']
access_token = os.environ['twitter_access_token']
access_token_secret = os.environ['twitter_access_token_secret']

cloudwatch = boto3.client('cloudwatch')
sqs = boto3.resource('sqs', region_name=os.environ['region_name'])
queue = sqs.get_queue_by_name(QueueName=os.environ['queue'])

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def send_to_sqs(tweet):
    """
    sends twitter data to sqs for further processing
    :param tweet: the twitter data in string
    """
    response = queue.send_message(MessageBody=tweet)
    print(response)


class TwitterStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        """
        triggered when a new tweet arrives
        :param data: a tweet data
        :return: bool
        """
        send_to_sqs(data)
        return True

    def on_error(self, status_code):
        """
        triggered by error that may originate from twitter stream
        :param status_code:
        :return: bools
        """
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False
        # returning non-False reconnects the stream, with backoff.


def twitter_stream_consumer(event, context):
    """
    the lambda handler that handles  twitter feed
    :param event:
    :param context:
    :return:
    """
    keywords = event["keywords"]
    k_list = keywords.split(",")
    t_stream_listener = TwitterStreamListener()
    t_stream = tweepy.Stream(auth=api.auth, listener=t_stream_listener)
    t_stream.filter(track=k_list)
