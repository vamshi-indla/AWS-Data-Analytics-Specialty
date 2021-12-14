
# Ec2->Kinesis Agent-Firehose->S3

Send Ec2 log messages to S3 using Firehose. Ec2 data is ingested using Kinesis Agent

### Ec2 Bootstrap
sudo yum update -y
sudo yum install –y aws-kinesis-agent
sudo chkconfig aws-kinesis-agent on #start the agent during system startup
wget http://media.sundog-soft.com/AWSBigData/LogGenerator.zip
unzip LogGenerator.zip
chmod a+x LogGenerator.py
sudo mkdir -p /var/log/cadabra
cd /etc/aws-kinesis

### In EC2 Terminal
sudo nano config.json
Attach IAM role with persmissions to EC2, for it to write to Kinesis firehose
change filepattern to the location of logs: /var/log/cadabra/*.log* and firehose name: PurchaseLogs
sudo service aws-kinesis-agent start #start the kinesis agent
cd ~
sudo ./LogGenerator.py 10000
tail -f /var/log/aws-kinesis-agent/aws-kinesis-agent.log #check status of ingestion to firehose
