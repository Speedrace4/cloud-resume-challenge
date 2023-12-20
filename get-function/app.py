import json, boto3

client = boto3.client('dynamodb')
TableName = 'cloud-resume-challenge'

#Lambda Function
def lambda_handler(event, context):
    response = client.update_item(
            TableName='cloud-resume-challenge',
            Key = {
                'stat': {'S': 'view-count'}
                },
            UpdateExpression = 'ADD Quantity :inc',
            ExpressionAttributeValues = {":inc" : {"N": "1"}},
            ReturnValues = 'UPDATED_NEW'
            )

    value = {"count": response['Attributes']['Quantity']['N']}
        
    return {      
            'statusCode': 200,
            "headers": {
            'Access-Control-Allow-Origin' : 'http://cloud-resume-challenge44.s3-website.us-east-2.amazonaws.com',
            'Access-Control-Allow-Headers':'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Credentials' : True,
            'Content-Type': 'application/json'
                        },
            'body': json.dumps(value)}
