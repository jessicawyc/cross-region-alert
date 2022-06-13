# securityhub-auto-remediation

## standard control
set parameter 设置参数

```
region='us-west-2'
rulename='manualalert'
email='**@**.com'
buttonname='s3.5'
actionid='send2email'
```
## create rule 配置eventbridge rule
```
aws events put-rule \
--name $rulename \
--event-pattern "{\"source\":[\"aws.securityhub\"], \
\"detail-type\": [\"Security Hub Findings - Custom Action\"], \
  \"resources\": [\"$buttonarn\"]}"  --region=$region
```

eventbridge rule-event pattern
```
{
  "detail-type": ["Security Hub Findings - Imported"],
  "source": ["aws.securityhub"],
  "detail": {
    "findings": {
      "Compliance": {
        "Status": ["FAILED", "WARNING"]
      },
      "GeneratorId": ["aws-foundational-security-best-practices/v/1.0.0/S3.2"],
      "Workflow": {
        "Status": ["NEW"]
      }
    }
  }
}
```
