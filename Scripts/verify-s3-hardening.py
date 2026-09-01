# Example — verify S3 is still blocked
import boto3
s3 = boto3.client('s3')
response = s3.get_public_access_block(
    Bucket='cloudsec-audit-lab-shauryaman'
)
print(response)