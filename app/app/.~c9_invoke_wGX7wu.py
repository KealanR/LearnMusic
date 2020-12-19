import boto3
from app import bcrypt
from app.user import User
from boto3.dynamodb.conditions import Key, Attr
from dynamo_scan import scan_for_keyword
                    
#link to dynamodb
dynamodb = boto3.resource('dynamodb')
#define variables for tables
userTable = dynamodb.Table('user_information')
questionTable = dynamodb.Table('questions')

def checkIfExistsSignUp(email):
    response = userTable.query(KeyConditionExpression=Key('email').eq(email))
    if (response['Count'] == 0):
        #print("empty")
        return True
    else:
        #print(response)
        return False
        
def checkIfExistsLogin(email, password):
   
    response = userTable.query(KeyConditionExpression=Key('email').eq(email))
    if (response['Count'] == 1):
        item = response['Items'][0]
        print(item['password'])
        if(bcrypt.check_password_hash(item['password'], password)):
            # user = User(item['email'], item['username'], True)
            user = User(item['email'], item['username'])
            return user
    
    else:
        #print(response)
        # user = User("", "", False)
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
    

    
def checkTag():
    
    print("TESTING TAG!!!!!!!!!!")
    return scan_for_keyword().check_word(questionTable, 'tags', 'hey')
    
def test(tableName, attrName, keyWord):
        
        table = dynamodb.Table(tableName)
        
        response = table.scan(FilterExpression=Attr(attrName).contains(keyWord))
        
        items = response['Items']
        print("the following items were found ", items)
        return items
        

#posts question to the database
def postQuestionWithoutFile(username, title, description):
    
    try:
        questionTable.put_item(
            Item={
                'username': username,
                'title': title,
                'description': description
            })
        
    except Exception as e:
        print(e)
        pass
    
   
#posts question to the database
def postQuestionWithFile(username, title, description, fileLocation):
    
    try:
        questionTable.put_item(
            Item={
                'username': username,
                'title': title,
                'description': description,
                'fileLocation': fileLocation
            })
        
    except Exception as e:
        print(e)
        pass
    

    