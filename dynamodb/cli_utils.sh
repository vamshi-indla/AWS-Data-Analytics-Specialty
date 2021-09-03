#create table
aws dynamodb create-table \
    --table-name PetInventory \
    --attribute-definitions \
        AttributeName=pet_species,AttributeType=S \
        AttributeName=pet_id,AttributeType=N \
    --key-schema \
            AttributeName=pet_species,KeyType=HASH \
            AttributeName=pet_id,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST