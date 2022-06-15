# Public S3 Auto Block Auto Remediation
通过lambda读取securityhub发出的event,调用SSM-automation进行修复
## 配置2个IAM Role
### AutomationServiceRole
Step1 请使用官方提供的cloudformation template运行
Download and unzip the AWS-SystemsManager-AutomationServiceRole.zip file. 
https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-cf.html

Step2 此role只能执行基本Automation,本案例中需要赋予其block S3的权限,首先下载policy文件在本地
[autos3policy.json](/autos3policy.json)
再运行CLI
```
addpolicy='Auto4S3block'
rolename='AutomationServiceRole'
aws iam put-role-policy --role-name=$rolename --policy-name $addpolicy --policy-document file://autos3policy.json
```
### 配置Lambda IAM Role
请下载[lambdapolicy.json](/lambdapolicy.json)
下载[trust-lambda.json](/trust-lambda.json)

```
lambdapolicy='lambda-auto-s3'
rolename='lambda-auto-s3'
rolearn=$(aws iam create-role --role-name $rolename --assume-role-policy-document file://trust-lambda.json --query 'Role.Arn' --output text)
aws iam put-role-policy --role-name=$rolename --policy-name $addpolicy --policy-document file://lambdapolicy.json
```

## Create Lambda
```
function='auto-s3-public'
lambdaarn=$(aws lambda create-function \
    --function-name $function \
    --runtime python3.9 \
    --zip-file fileb://FSBP-S3public-lambda.zip \
    --handler FSBP-S3public-lambda.lambda_handler \
    --role $rolearn --region=$region --no-cli-pager --query 'FunctionArn' --output text)
```
创建成功后,登录平台lambda console,进入Configuration中配置两个环境变量:
key
```
documentname
```
value
```
AWSConfigRemediation-ConfigureS3BucketPublicAccessBlock
```
key
rolearn
```
rolearn
```
value 就是在第一步使用cloudformation生成的role的ARN 运行CLI后的输出结果
```
aws iam get-role   --role-name $rolename --query 'Role.Arn' --output text
```
Add trigger-Trigger configuration 选择Eventbridge,Rule-Existing rules 将第一步创建的Rule加进去


