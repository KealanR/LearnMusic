import boto3
from boto3.dynamodb.conditions import Key, Attr
import keys

dynamodb = boto3.resource('dynamodb',
                    aws_access_key_id = keys.aws_access_key_id,
                    aws_secret_access_key = keys.aws_secret_access_key,
                    aws_session_token = keys.aws_session_token)

userTable = dynamodb.Table('users')
questionTable = dynamodb.Table('questions')

def questionList():
    
    response = questionTable.scan()
    items = response['Items']
    return items
# def signup(email, password):
    
#     if userTable.query(KeyConditionExpression=Key('email').eq(email)) != null:
#         return Flase
        
#     else:
#         userTable.put_item(
#         Item = {
#             'email': email,
#             'password': password
#             }
#         )
    
    
    
    
    
# login(email, password):

    