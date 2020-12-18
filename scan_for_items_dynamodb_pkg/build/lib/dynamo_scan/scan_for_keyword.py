import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')

#this function will take in a table name, attrribute name and a key word
# it will then scan the table to see if there are any matches
#it will return a list of all appliciple matches
class ScanForKeyWord():
    
    def check_word(self, tableName, attrName, keyWord):
        
        table = dynamodb.Table(tableName)
        
        response = table.scan(FilterExpression=Attr(attrName).eq(keyWord))
        
        items = response['Items']
        print("the following items were found ", items)
        return items
        