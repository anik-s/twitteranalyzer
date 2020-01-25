import os
import boto3
import simplejson as json

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['tweet_table']


def get_tweets(event, context):
    """
    lambda functions that handles http request to get already collected tweets
    :param event:
    :param context:
    """
    try:
        # fetch tweets from the database
        table = dynamodb.Table(table_name)
        filter_dict = {}
        if event['queryStringParameters'] is not None:
            l_e_key = event['queryStringParameters']['last_evaluated_key']
            if l_e_key != "":
                filter_dict['ExclusiveStartKey'] = int(l_e_key)
        result = table.scan(filter_dict)
        last_evaluated_key = ""
        if "LastEvaluatedKey" in result:
            last_evaluated_key = result["LastEvaluatedKey"]
        print(len(result['Items']))
        print("len")
        r_body = {
            "tweets": result['Items'],
        }
        if last_evaluated_key != "":
            r_body["last_evaluated_key"] = last_evaluated_key
        response = {
            "statusCode": 200,
            "body": json.dumps(r_body)
        }
        return response
    except Exception as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
        return response
