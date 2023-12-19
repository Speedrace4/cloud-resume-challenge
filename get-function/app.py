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
                        'Access-Control-Allow-Origin' : '*',
                        'Access-Control-Allow-Headers': '*',
                        'Access-Control-Allow-Credentials': '*',
                        'Content-Type': 'application/json'
                        },
            'body': json.dumps(value)}
