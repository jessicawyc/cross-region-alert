# securityhub-auto-remediation

## General Step
通过配置custome action-eventbridge-automation对特定control进行自动修复
![架构图](/)
set parameter 设置参数

```
region='eu-west-2'
rulename='sechub-fsbp-s3'
buttonname='BlockPublicS3'
des='to auto block public s3'
actionid='blocks3'
email='**@qq.com'
```
## create rule 配置eventbridge rule
```
snsarn=$(aws sns create-topic   --name  $rulename  --region=$region  --output text --query 'TopicArn')
aws sns subscribe --topic-arn $snsarn --protocol email --notification-endpoint  $email --region=$region

buttonarn=$(aws securityhub create-action-target \
    --name $buttonname\
    --description $des \
    --id $actionid --region=$region  --output text --query 'ActionTargetArn')

aws events put-rule \
--name $rulename \
--event-pattern "{\"source\":[\"aws.securityhub\"], \
\"detail-type\": [\"Security Hub Findings - Custom Action\"], \
  \"resources\": [\"$buttonarn\"]}"  --region=$region
  
aws events put-targets --rule $rulename  --targets "Id"="1","Arn"=$snsarn --region=$region
```
### config email format in " Configure input transformer"
Target input transformer-Input path
```
{
  "Description": "$.detail.findings[0].Description",
  "Id": "$.detail.findings[0].Resources[0].Id",
  "account": "$.detail.findings[0].AwsAccountId",
  "region": "$.detail.findings[0].Resources[0].Region",
  "title": "$.detail.findings[0].Title"
}

```
template
```
"Hello team, based on security check : <title> in region:<region>"
"of account <account>"
"You just triggered the remediation action on resource"
"<Id>"
"It is now fixed, please kindly check."
"Have a nice day!"
```
## 配置后台自动化处理
Block public S3 请见 [publics3.md](/publics3.md)
