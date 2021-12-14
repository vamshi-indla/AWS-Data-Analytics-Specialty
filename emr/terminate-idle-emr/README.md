## Terminate Idle EMR cluster

### Approach#1
- EMR cluster is not configured with Auto termination
- EMR cluster termination protection is off
- Cloudwatch Alarm Rule is defined to monitor EMR cluster idleness, using EMRShutdown
- When Alarm triggers, it sends SNS message
- SNS topic invokes Lambda function
- Lambda Function checks the Idle EMR clusters and shutsdown

### Approach#2
- EMR cluster is not configured with Auto termination
- EMR cluster termination protection is off
- Create a cron Cloudwatch rule to trigger lambda every n minutes. i.e Schedule Expression: rate(1 minute)
- set Lambda environment variable as MAX_IDLE_TIME_IN_MINUTES = 1
- Create IAM role and attach EMR policies ListCluster, ListSteps, elasticmapreduce:SetTerminationProtection, elasticmapreduce:TerminateJobFlows
- Lambda (scan-terminate-emr-lambda.py) scans all the EMR clusters for Idle clusters. Idle time threshold is defined as environment variable
- Lambda then terminates EMR cluster meeting the criteria