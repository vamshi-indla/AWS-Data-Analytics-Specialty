#list buckets
aws s3 ls

#sycn bucket to current directory
aws s3 sync s3://data-123456 .

#see first n characters of s3 file
cut -c -n filename.parquet

#copy file to buckets
aws s3 cp file1.txt s3://data-123456 

#move file to buckets
aws s3 cp file1.txt s3://data-123456 



