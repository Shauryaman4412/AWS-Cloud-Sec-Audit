<div align="center">

# 🔐 AWS Cloud Security Audit & Hardening

### End-to-end cloud security assessment — from intentional misconfiguration to full remediation

![AWS](https://img.shields.io/badge/AWS-Cloud_Security-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Prowler](https://img.shields.io/badge/Prowler-v5.39.1-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CIS](https://img.shields.io/badge/CIS_AWS_Benchmark-v3.0-red?style=for-the-badge)

</div>

---

## 📌 Project Overview

This project demonstrates a **complete cloud security audit lifecycle** against an AWS environment. A deliberately misconfigured AWS Free Tier account was built from scratch, assessed using **Prowler v5.39.1** across 632 automated checks, hardened against all critical findings, and re-scanned to prove measurable improvement.

The methodology mirrors real-world cloud security engagements:

```
PREPARE → SCAN → ANALYZE → REPORT → REMEDIATE → RE-SCAN → VERIFY
```

---

## 📊 Results

| Metric | Before Hardening | After Hardening |
|:---|:---:|:---:|
| Total checks | 632 | 632 |
| ❌ Failed | 118 (47.58%) | 113 (38.44%) |
| ✅ Passed | 124 (50%) | 174 (59.18%) |
| 🔴 Critical findings | 7 | 3 (accepted risk) |
| 🟠 High findings | 30 | 17 |
| 📦 Resources assessed | 56 | 64 |

> **+50 additional checks passing after hardening a 40% improvement in pass rate**

---

## 🛠️ Tools & Frameworks

| Tool | Version | Purpose |
|:---|:---|:---|
| Prowler | v5.39.1 | Automated cloud security scanning (632 checks) |
| AWS CLI | v2.x | Credential configuration and CLI verification |
| Python | 3.11 | Script runtime environment |
| Boto3 | Latest | Programmatic hardening verification (5 scripts) |

**Frameworks:** CIS AWS Benchmark v3.0 · MITRE ATT&CK Cloud · AWS Foundational Security Best Practices · AWS Well-Architected Security Pillar

---

## 🧪 Lab Setup — Intentional Misconfigurations

A dedicated AWS Free Tier account was configured with 8 intentional misconfigs to simulate a real-world insecure environment:

| # | Misconfiguration | Service | Severity | CIS Control |
|:---|:---|:---|:---:|:---|
| 1 | Root account — no MFA | IAM | 🔴 Critical | CIS 1.5 |
| 2 | IAM admin user — no MFA + AdministratorAccess | IAM | 🔴 Critical | CIS 1.10 |
| 3 | SSH open to 0.0.0.0/0 | EC2 | 🔴 Critical | CIS 5.2 |
| 4 | RDP open to 0.0.0.0/0 | EC2 | 🔴 Critical | CIS 5.3 |
| 5 | S3 bucket — public access enabled | S3 | 🔴 Critical | CIS 2.1.5 |
| 6 | CloudTrail disabled | CloudTrail | 🟠 High | CIS 3.1 |
| 7 | VPC Flow Logs disabled | VPC | 🟠 High | CIS 3.7 |
| 8 | EBS volume unencrypted | EC2 | 🟠 High | CIS 2.2.1 |

---

## 🔍 Scan Command

```bash
prowler aws --output-formats html json-ocsf --region ap-south-1
```

Prowler executed **632 checks** across IAM, EC2, S3, CloudTrail, CloudWatch, VPC, GuardDuty, Config, and KMS completing in under 3 minutes.

---

## 🚨 Critical Findings — Detailed Analysis

<details>
<summary><b>F-001 — Root account has no MFA [CRITICAL · CIS 1.5]</b></summary>

**Service:** IAM  
**Risk:** Root has unrestricted access to all AWS resources. A stolen password alone provides complete account takeover attacker can delete all resources, disable security controls, and exfiltrate all data.  
**Remediation:** Enabled virtual MFA via Google Authenticator. Two MFA devices now assigned.

</details>

<details>
<summary><b>F-002 — IAM user AdministratorAccess with no MFA [CRITICAL · CIS 1.10]</b></summary>

**Service:** IAM  
**Risk:** Stolen password = full admin access. No second factor exists to prevent unauthorized login. Attacker gains ability to create resources, exfiltrate data, and establish persistence.  
**Remediation:** Enabled MFA via authenticator app. Replaced AdministratorAccess with ReadOnlyAccess (least privilege).

</details>

<details>
<summary><b>F-003 — SSH open to 0.0.0.0/0 [CRITICAL · CIS 5.2]</b></summary>

**Service:** EC2  
**Risk:** Instance directly exposed to brute-force SSH attacks from anywhere on the internet. No IP restriction means any attacker globally can attempt access.  
**Remediation:** Deleted SSH inbound rule from security group entirely.

</details>

<details>
<summary><b>F-004 — RDP open to 0.0.0.0/0 [CRITICAL · CIS 5.3]</b></summary>

**Service:** EC2  
**Risk:** Internet-exposed RDP is the primary initial access vector for ransomware operators. High exploitability, high blast radius.  
**Remediation:** Deleted RDP inbound rule from security group.

</details>

<details>
<summary><b>F-005 — S3 bucket publicly accessible [CRITICAL · CIS 2.1.5]</b></summary>

**Service:** S3  
**Risk:** Bucket policy with `Principal: "*"` allowed unauthenticated read access to all objects risk of data exfiltration, compliance violations, and reputational damage.  
**Remediation:** Enabled all 4 Block Public Access settings. Deleted the public bucket policy.

</details>

---

## 🔧 Hardening Actions

| Fix | Service | Action Taken | Result |
|:---|:---|:---|:---:|
| Root MFA | IAM | Enabled virtual MFA via authenticator app | ✅ |
| IAM user MFA | IAM | Enabled MFA, replaced AdministratorAccess → ReadOnlyAccess | ✅ |
| EC2 open ports | EC2 | Deleted SSH, RDP, HTTP inbound rules from security group | ✅ |
| S3 public access | S3 | Enabled Block Public Access, deleted public bucket policy | ✅ |
| CloudTrail | CloudTrail | Created multi-region trail logging to S3 | ✅ |
| VPC Flow Logs | VPC | Created flow log capturing ALL traffic to CloudWatch Logs | ✅ |
| GuardDuty | GuardDuty | Enabled in ap-south-1 | ✅ |
| Password policy | IAM | 14-char min · all complexity · 90-day expiry · 24 history | ✅ |

---

## 🐍 Boto3 Verification Scripts

After manual hardening, **5 Python scripts** using the AWS Boto3 SDK were written to independently verify each control via direct AWS API calls stronger than console screenshots alone.

| Script | AWS API Called | CIS Control | Result |
|:---|:---|:---|:---:|
| `verify-s3-hardening.py` | `S3:GetPublicAccessBlock` | CIS 2.1.5 | ✅ PASS |
| `verify-cloudtrail.py` | `CloudTrail:DescribeTrails` + `GetTrailStatus` | CIS 3.1 | ✅ PASS |
| `verify-guardduty.py` | `GuardDuty:ListDetectors` + `GetDetector` | AWS FSB | ✅ PASS |
| `verify-iam.py` | `IAM:GetAccountPasswordPolicy` + `ListMFADevices` | CIS 1.8, 1.10 | ✅ PASS |
| `verify-vpc-flowlogs.py` | `EC2:DescribeFlowLogs` | CIS 3.7 | ✅ PASS |

> **Bonus finding:** The CloudTrail verification script discovered that log file validation (CIS 3.2) was disabled a gap not caught in the manual review. This demonstrates the real value of scripted verification beyond console checks.

---

## ✅ Accepted Risks — Remaining Critical Findings

| Risk ID | Finding | Decision | Justification |
|:---|:---|:---:|:---|
| AR-001 | Root uses virtual MFA not hardware MFA | Accept | Hardware token unavailable for lab. Virtual MFA provides strong protection. Compensating control: root not used for daily operations. |
| AR-002 | AdministratorAccess AWS managed policy exists | Accept | AWS managed policy cannot be deleted. NOT attached to any user. ReadOnlyAccess applied to all users. |

---

## 📈 Compliance Posture — Before vs After

| Framework | Before | After | Change |
|:---|:---:|:---:|:---:|
| AWS Account Security Onboarding | 92.31% fail | ~70% fail | ✅ Improved |
| AWS Foundational Security Best Practices | 57.53% fail | ~40% fail | ✅ Improved |
| AWS Well-Architected Security Pillar | 50.78% fail | ~38% fail | ✅ Improved |
| ASD Essential Eight | 52.5% fail | ~35% fail | ✅ Improved |
| AWS Control Tower Guardrails | 80.0% fail | ~55% fail | ✅ Improved |
| CIS AWS Benchmark (v3.0 - v7.0) | ~65% fail | ~54% fail | ✅ Improved |

---

## 📁 Repository Structure

```
CloudSecurityAudit/
├── README.md                              # This file
├── reports/
│   └── AWS_Security_Audit_FINAL.docx     # Full 32-page audit report with all evidence
└── scripts/
    ├── verify-s3-hardening.py             # S3 Block Public Access verification
    ├── verify-cloudtrail.py               # CloudTrail logging verification
    ├── verify-guardduty.py                # GuardDuty status verification
    ├── verify-iam.py                      # Password policy + MFA verification
    └── verify-vpc-flowlogs.py             # VPC Flow Logs verification
```

> 📄 The full audit report contains all before/after screenshots with sensitive values redacted.

---

## 💡 Key Takeaways

- Cloud environments are **insecure by default** security must be actively configured
- **IAM misconfigurations** (no MFA, overly permissive policies) are the highest risk category
- **Logging gaps** (CloudTrail, VPC Flow Logs, GuardDuty) leave environments completely blind to attacks
- **Open security groups** are trivially easy to exploit and trivially easy to fix
- Not all scanner findings require remediation **professional judgment** and accepted risk documentation matter as much as technical fixes
- **Scripted verification** catches gaps that manual console review misses

---

## 👤 Author

**Shauryaman Menaria**  
BTech CSE (Cybersecurity)
CompTIA Security+ · AWS Solutions Architect Associate (SAA-C03)  
TryHackMe — Top 4% globally (95+ rooms)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Shauryaman_Menaria-0077B5?style=flat&logo=linkedin)](https://linkedin.com/in/shauryaman-menaria)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-Top_4%25-212C42?style=flat&logo=tryhackme)](https://tryhackme.com/p/Shauryaman4412)

---

<div align="center">

*All sensitive values (account IDs, ARNs, IP addresses, access keys) have been redacted from all screenshots in the audit report.*

</div>
