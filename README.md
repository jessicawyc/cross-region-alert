# securityhub-auto-remediation

## standard control
通过配置custome action-eventbridge-automation对特定control进行自动修复
set parameter 设置参数

```
region='us-west-2'
rulename='sechub-fsbp-s3.2'
buttonname='s3.2'
des='to auto fix fsbp s3.2'
actionid='s3.2'
```
## create rule 配置eventbridge rule
```
buttonarn=$(aws securityhub create-action-target \
    --name $buttonname\
    --description $des \
    --id $actionid --region=$region  --output text --query 'ActionTargetArn')
aws events put-rule \
--name $rulename \
--event-pattern "{\"source\":[\"aws.securityhub\"], \
\"detail-type\": [\"Security Hub Findings - Custom Action\"], \
  \"resources\": [\"$buttonarn\"]}"  --region=$region
```
Others
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
