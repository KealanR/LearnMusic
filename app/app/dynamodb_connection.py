import boto3
from app import bcrypt
from app.user import User
from boto3.dynamodb.conditions import Key, Attr
                    
#link to dynamodb
dynamodb = boto3.resource('dynamodb')
#define variables for tables
userTable = dynamodb.Table('user_information')
questionTable = dynamodb.Table('questions')

def checkIfExistsSignUp(email):
    response = userTable.query(KeyConditionExpression=Key('email').eq(email))
    if (response['Count'] == 0):
        
        return True
    else:
        return False
        
def checkIfExistsLogin(email, password):
   
    response = userTable.query(KeyConditionExpression=Key('email').eq(email))
    if (response['Count'] == 1):
        item = response['Items'][0]
        if(bcrypt.check_password_hash(item['password'], password)):
            user = User(item['email'], item['username'])
            return user
    
    else:
        user = None
        return user


    
def signupDB(email, username, password):
    
    try:
        
        userTable.put_item(
            Item={
                'email': email,
                'username': username,
                'password': password
            })
    except Exception as e:
        print(e)
        pass

    
#scans db for list of questions and returns list
def questionList():
    response = questionTable.scan()
    
    return response['Items']
    
def specificQuestion(title):
    
    response = questionTable.query(KeyConditionExpression=Key('title').eq(title))
    if (response['Count'] == 1):
        item = response['Items'][0]
        return(item)
        
    else:
        return(None)
    
    
def checkTag():
    
    return scan_for_keyword().check_word(questionTable, 'tags', 'hey')
    

#posts question to the database
def postQuestionWithoutFile(username, title, description, tag):
    
    try:
        questionTable.put_item(
            Item={
                'username': username,
                'title': title,
                'description': description,
                'tag': tag
            })
        
    except Exception as e:
        print(e)
        pass
    
   
#posts question to the database
def postQuestionWithFile(username, title, description, tag, file_location):
    
    try:
        questionTable.put_item(
            Item={
                'username': username,
                'title': title,
                'description': description,
                'tag': tag,
                'file_location': file_location
            })
        
    except Exception as e:
        print(e)
        pass
    

def updateQuestionComments(title, username, comment, comment_username):
    try:
        questionTable.update_item(
            Key={
                'title': title,
                'username': username
            },
            UpdateExpression='SET comments = list_append(if_not_exists(comments, :comment), :comment_username)',
            ExpressionAttributeValues={
                ':comment': [{"S":comment}],
                ':comment_username': [{"S":comment_username}]
            }
            )
            
    except Exception as e:
        print(e)
        pass