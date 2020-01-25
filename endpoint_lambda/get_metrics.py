import os
from datetime import datetime, timedelta
import simplejson as json
import boto3

cloudwatch = boto3.client('cloudwatch', region_name=os.environ['region_name'])


def get_metrics_handler(event, context):
    """
    lambda functions that handles http request and get twitter metric data from cloudwatch
    :param event:
    :param context:
    :return:
    """
    try:
        country = event['queryStringParameters']['country']
        period = int(event['queryStringParameters']['period'])
        start_time = datetime.strptime(event['queryStringParameters']['start_time'], '%Y-%m-%dT%H:%M:%S')
        end_time = datetime.strptime(event['queryStringParameters']['end_time'], '%Y-%m-%dT%H:%M:%S')
        response = cloudwatch.get_metric_statistics(
            Namespace=os.environ['metric_namespace'],
            MetricName='NumberOfTweets',
            Dimensions=[
                {
                    'Name': 'Country',
                    'Value': country
                },
            ],
            StartTime=start_time,
            EndTime=end_time,
            Period=period,
            Statistics=[
                'Sum'
            ]
        )
        print(response)
        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            resp = {
                "statusCode": response['HTTPStatusCode'],
                "body": json.dumps({
                    'code': response['HTTPStatusCode']
                }),
                "headers": {
                    "Content-Type": "application/json"
                }
            }
            return resp

        resp = {
            "statusCode": 200,
            "body": json.dumps({
                'Label': response['Label'],
                'Datapoints': response['Datapoints']
            }, default=str),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return resp

    except Exception as e:
        print(e)
        resp = {
            "statusCode": 500,
            "body": json.dumps({

            }),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return resp
