import boto3

dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
questionTable = dynamodb.create_table(
    TableName='questions',
    KeySchema=[
        {
            'AttributeName': 'title',
        'KeyType': 'HASH'
        },
        {
            'AttributeName': 'username',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
questionTable.meta.client.get_waiter('table_exists').wait(TableName='questions')

userTable = dynamodb.create_table(
    TableName='user_information',
    KeySchema=[
        {
            'AttributeName': 'email',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'username',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'email',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
    )
# Wait until the table exists.
userTable.meta.client.get_waiter('table_exists').wait(TableName='user_information')

# Print out some data about the table.
print(questionTable.item_count)
print(userTable.item_count)