import boto3

client = boto3.client('cloudtrail', region_name='ap-south-1')
trails = client.describe_trails()['trailList']

if not trails:
    print("FAIL: No CloudTrail trails found")
else:
    for trail in trails:
        status = client.get_trail_status(Name=trail['TrailARN'])
        print(f"Trail: {trail['Name']}")
        print(f"Logging: {status['IsLogging']}")
        print(f"Multi-region: {trail['IsMultiRegionTrail']}")
        print(f"Log validation: {trail['LogFileValidationEnabled']}")
        print("PASS: CloudTrail is active" if status['IsLogging'] else "FAIL: Logging disabled")