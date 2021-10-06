--unload a specific table from cluster#1, after connecting to its database
UNLOAD ('SELECT * FROM USERS_DATA') 
TO 's3://users-data-541210088175' 
IAM_ROLE '' 
FORMAT AS PARQUET

-- create table in destination cluster, after connecting to cluster#2 database
create table users_data(
  id_value varchar(64),
  name_first varchar(64),
  name_last varchar(64),
  location_country varchar(32),
  dob_age int,
  picture_large varchar(64),
  primary key(id_value)
)
distkey(location_country)
compound sortkey(id_value);

-- copy from s3 snapshot to redshift destination cluster
COPY users_data
FROM 's3://users-data-541210088175'
IAM_ROLE 'arn:aws:iam::541210088175:role/RedshiftS3'
FORMAT AS PARQUET;

--verify the Records
select * from users_data limit 10;