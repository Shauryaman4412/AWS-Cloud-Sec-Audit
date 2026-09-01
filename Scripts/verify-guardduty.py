import boto3

client = boto3.client('guardduty', region_name='ap-south-1')
detectors = client.list_detectors()['DetectorIds']

if not detectors:
    print("FAIL: GuardDuty not enabled")
else:
    detector = client.get_detector(DetectorId=detectors[0])
    print(f"Detector ID: {detectors[0][:8]}...")
    print(f"Status: {detector['Status']}")
    print(f"Finding frequency: {detector['FindingPublishingFrequency']}")
    print("PASS: GuardDuty is active" if detector['Status'] == 'ENABLED' else "FAIL")