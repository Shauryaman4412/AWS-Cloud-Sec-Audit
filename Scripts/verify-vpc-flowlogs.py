import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')
flow_logs = ec2.describe_flow_logs()['FlowLogs']

if not flow_logs:
    print("FAIL: No VPC Flow Logs configured")
else:
    for log in flow_logs:
        print(f"Flow Log ID: {log['FlowLogId'][:12]}...")
        print(f"Status: {log['FlowLogStatus']}")
        print(f"Traffic type: {log['TrafficType']}")
        print(f"Destination: {log['LogDestinationType']}")
        print("PASS: VPC Flow Logs active" if log['FlowLogStatus'] == 'ACTIVE' else "FAIL")