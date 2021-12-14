## Athena

### Query Parquet formatted Cloudfront Logs stored in S3
### Approach#1
- Without Glue catalog, Athena can import data from S3 to database.table. Database, table, schema has to provided first though.

- Create database and table 
```
CREATE database aws_service_logs
--Create table and provide schema
```

- Load data from S3: location. S3 Location is provded while creating the table.
```
MSCK REPAIR TABLE aws_service_logs.cf_access_optimized 
```

- Query as you wish
```
SELECT METHOD, sum(bytes) AS TOTAL_BYTES FROM "aws_service_logs"."cf_access_optimized" 
where time between TIMESTAMP '2018-11-02' AND TIMESTAMP '2018-11-03'
GROUP BY METHOD ; 
```

### Approach#2

- Create a Glue OnDemand Crawler on datafiles, not complete Bucket.
- Table and Data is accessible in Athena directly
- Query as you wish