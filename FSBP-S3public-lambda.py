import json
import boto3
import os
client = boto3.client('ssm')
def lambda_handler(event, context):
    #读取security hub custom action finding,不能用于insight
    aws_account_id = event["account"]
    region = event['region']
    finding=event['detail']['findings'][0]
    assetType =finding["Resources"][0]['Type']
    if assetType != "AwsS3Bucket":
        return ('Skipping non-S3 asset type: ' + assetType)
    else:
        s3arn = finding["Resources"][0]['Id']
        s3name=s3arn[13:]
        print(s3name)
        response = client.start_automation_execution(
            DocumentName=os.environ['documentname'],
            Parameters={
                'BucketName': [s3name],
                'AutomationAssumeRole':[os.environ['rolearn']]
            }
            )
        return(response)
   
    return('done')
