## Dead Letter Queue Processing


### Note
- Dead Letter Queue is just another queue, but it should be created before the main queue is created
- "Message Received" is the number of times message is received by poller
- During Lambda environment invocation, only 1 sqs message is polled, even though "batch size" is greater.
- Policies required for Lambda to poll SQS messages
    - sqs: ReceiveMessage
    - sqs: DeleteMessage
    - sqs: GetQueueAttributes

### Warnings
- While processing a batch of sqs messages, if few lambda fails after processing few messages, then all the batch will be considered failure.
It will be re-attempted after "Visibility Timeout".
If it meets "Dead Letter Queue - Message Received" limit, then messages will be routed to "Dead Letter Queue"

### Best Practices
- Create "cloudwatch alarm" that can monitor the "AverageMessagesVisible" number in "Dead Letter Queue", to avoid skipping too many messages.





