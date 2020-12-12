import boto3, user
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')

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

    