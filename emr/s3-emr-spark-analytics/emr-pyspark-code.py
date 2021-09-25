from pyspark import SparkConf
from pyspark.sql import SparkSession

# input_dir = "hdfs:///user-data-acg/user-data-*.csv"
# output_dir = "hdfs:///results"

input_dir = "user-data-acg"
output_dir = "results.csv"

spark = SparkSession.builder.master("local") \
        .config(conf=SparkConf()).getOrCreate()

df = spark.read.format("csv")   \
        .option("header", "true") \
        .load(input_dir)

results = df.groupBy("`dob.age`", "`gender`") \
            .count()    \
            .orderBy("count", ascending=False)

results.show()

results.coalesce(1).write.csv(output_dir, sep=",", header="true")

# s3-dist-cp command to move files from s3 to HDFS for EMR processing
# s3-dist-cp --src=s3://vki-s3-files-for-emr12345/Data_Analytics_With_Spark_and_EMR/user-data-acg/ --dest=hdfs:///

# hadoop command to copy from s3 to hdfs
# hadoop distcp s3://vki-emr12345/user-data-acg/*.csv hdfs:///csvfiles/