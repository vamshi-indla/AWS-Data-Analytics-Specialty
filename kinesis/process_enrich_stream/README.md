### Architecture


incoming-orders Data Stream -> process_enrich_stream_lamdbda -> enriched-orders -> Kinesis Analytics filtering > 100.00 -> Kinesis Firehose + Lambda Transforming the incoming data -> S3 bucket