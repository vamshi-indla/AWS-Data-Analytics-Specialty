#list buckets
aws s3 list

#sycn bucket to current directory
aws s3 sync s3://data-123456 .

#see first n characters of s3 file
cut -c -n filename.parquet





