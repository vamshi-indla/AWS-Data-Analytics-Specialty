
### Download csv

1. Download csv 

```sh
curl -O -l https://raw.githubusercontent.com/linuxacademy/content-aws-database-specialty/master/S06_Additional%20Database%20Services/redshift-data.csv
```

2. make bucket 
```sh
aws s3 mb s3://redshift-import-20211016
```

3. Load data into bucket
```sh
aws s3api put-object --bucket redshift-import-20211016 --key redshift-data.csv --body redshift-data.csv
```

4. confirm the data load to bucket
```sh
aws s3 ls s3://redshift-import-20211016
```

5. Download JSON data 
```sh
curl -O -l curl -O -l https://raw.githubusercontent.com/linuxacademy/content-aws-database-specialty/master/S06_Additional%20Database%20Services/redshift-data.json

ls
```

6. create dynamodb table
```sh
aws dynamodb create-table --table-name redshift-import --attribute-definitions AttributeName=ID,AttributeType=N --key-schema AttributeName=ID,KeyType=HASH --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5

aws dynamodb list-tables
```

7. Import Json data to DynamoDB Table 
```sh
aws dynamodb batch-write-item --request-items file://redshift-data.json
aws dynamodb scan --table-name redshift-import
```

8. Create new role and associate it in Redshift cluster
Make sure role allows redshift to access S3 bucket (List and Get policies) and Dynamodb (Scan and Describe)

9. Describe redshift Clusters
```sh
aws redshift describe-clusters | head -25
export PGHOST=redshiftcluster-v8joirpmrjbk.cfnd62xosxoj.us-east-1.redshift.amazonaws.com
arn:aws:iam::827039240043:role/redshift-import
s3://redshift-import-20211016
```

10. Connect to redshift cluster 
```sh
psql masteruser -p 5439 import-test
```

11. Create Table 
```sh
create table users_import (ID int, Name varchar, Department varchar, ExpenseCode int);
```

12. Copy from s3 to redshift table 
```sh
copy users_import from 's3://redshift-import-20211016/redshift-data.csv' iam_role 'arn:aws:iam::827039240043:role/redshift-import' delimiter ',';
select * from users_import ;
```

13. Copy from dynamodb to redshift table
```sh
copy users_import from 'dynamodb://redshift-import' iam_role 'arn:aws:iam::827039240043:role/redshift-import' readratio 50 ;
```




