import boto3
client = boto3.client('dynamodb')
createResponse = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName' : 'pet_species',
            'AttributeType' : 'S'
        },
        {
            'AttributeName' : 'pet_id',
            'AttributeType' : 'N'
        }
    ],
    KeySchema=[
        {
            'AttributeName' : 'pet_species',
            'KeyType' : 'HASH'
        },
        {
            'AttributeName' : 'pet_id',
            'KeyType' : 'RANGE'
        }
    ],
    BillingMode = 'PAY_PER_REQUEST', 
    TableName = 'PetInventory'
)

#Table creation response
print(createResponse)

# Describe Table
statusResponse = client.describe_table(TableName='PetInventory')
print(statusResponse)

# list tables
listResponse = client.list_tables()
print(listResponse)

# delete table_name
deleteResponse = client.delete_table(TableName = 'PetInventory')