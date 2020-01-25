import os
import json
from boto3 import client as boto3_client
from custom_exception.exception import UnAuthorizedException, InternalException

access_token = "123"  # hard coded token due to lack of time


def start_flow_handler(event, context):
    """
    lambda functions that responses to http request and calls another lambda function which starts consumer for twitter
    stream
    :param event:
    :param context:
    """
    try:
        if 'Authorization' not in event['headers']:
            raise UnAuthorizedException('Unauthorized')
        bearer_token = event['headers']['Authorization']
        t = bearer_token.split('Bearer ')
        if len(t) != 2:
            raise UnAuthorizedException('Unauthorized')
        token = t[1]
        if token != access_token:
            raise UnAuthorizedException('Unauthorized')
        keywords = event['queryStringParameters']['keywords']
        lambda_client = boto3_client('lambda')
        msg = {"keywords": keywords}
        function_name = os.environ['service_name'] + '-' + os.environ['stage'] + '-' + \
                        os.environ['twitter_stream_lambda']
        resp = lambda_client.put_function_concurrency(FunctionName=function_name,
                                                      ReservedConcurrentExecutions=2)
        print(resp)
        invoke_response = lambda_client.invoke(FunctionName=function_name,
                                               InvocationType='Event',
                                               Payload=json.dumps(msg))
        if invoke_response['ResponseMetadata']['HTTPStatusCode'] != 202:
            raise InternalException(invoke_response['ResponseMetadata']['HTTPStatusCode'], "Lambda Invoke Problem")
        response = {
            "statusCode": 200,
            "body": json.dumps({
                "status": True
            }),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return response
    except UnAuthorizedException as ue:
        print(ue)
        resp = {
            "statusCode": ue.code,
            "body": json.dumps({
                "status": False,
                "message": ue.message
            }),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return resp
    except InternalException as ie:
        print(ie)
        resp = {
            "statusCode": ie.code,
            "body": json.dumps({
                "status": False,
                "message": ie.message,
            }),
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
                "status": False
            }),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return resp
