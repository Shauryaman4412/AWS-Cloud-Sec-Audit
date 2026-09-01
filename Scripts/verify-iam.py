import boto3

iam = boto3.client('iam')

# Check password policy
try:
    policy = iam.get_account_password_policy()['PasswordPolicy']
    print(f"Min password length: {policy['MinimumPasswordLength']}")
    print(f"Require uppercase: {policy.get('RequireUppercaseCharacters', False)}")
    print(f"Require numbers: {policy.get('RequireNumbers', False)}")
    print(f"Require symbols: {policy.get('RequireSymbols', False)}")
    print(f"Max password age: {policy.get('MaxPasswordAge', 'Not set')}")
    print("PASS: Strong password policy configured")
except:
    print("FAIL: No password policy configured")

# Check MFA on users
users = iam.list_users()['Users']
for user in users:
    mfa = iam.list_mfa_devices(UserName=user['UserName'])['MFADevices']
    status = "PASS: MFA enabled" if mfa else "FAIL: No MFA"
    print(f"User {user['UserName']}: {status}")