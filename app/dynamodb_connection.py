import boto3
from boto3.dynamodb.conditions import Key, Attr
import keys

# dynamodb = boto3.resource('dynamodb',
#                     aws_access_key_id = keys.aws_access_key_id,
#                     aws_secret_access_key = keys.aws_secret_access_key,
#                     aws_session_token = keys.aws_session_token)
                    
#link to dynamodb
dynamodb = boto3.resource('dynamodb')
#define variables for tables
userTable = dynamodb.Table('user_information')
questionTable = dynamodb.Table('questions')

def checkIfExists(email):
    response = userTable.query(KeyConditionExpression=Key('email').eq(email))
    if (response['Count'] == 0):
        #print("empty")
        return True
    else:
        #print(response)
        return False
    
    
def signupDB(email, username, password):
    # userInfo = {
    #     'email': email, 
    #     'userame': username, 
    #     'password': password
    # }
    userTable.put_item(
        Item={
            'email': email,
            'username': username,
            'password': password
        })

#scans db for list of questions and returns list
def questionList():
    response = questionTable.scan()
    
    return response['Items']
   
#posts question to the database
def postQuestion(question):
    
    try:
        questionTable.put_item(question)
        
    except Exception as e:
        pass
    

    