# Public S3 Auto Block Auto Remediation
通过lambda读取securityhub发出的event,调用SSM-automation进行修复
## 配置SSM-Automation IAM Role
### AutomationServiceRole
Step1 请使用官方提供的cloudformation template运行
Download and unzip the AWS-SystemsManager-AutomationServiceRole.zip file. 
https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-cf.html

Step2 此role只能执行基本Automation,本案例中需要赋予其block S3的权限,首先下载policy文件在本地
[autos3policy.json]()
再运行CLI
```
addpolicy='Auto4S3block'
rolename='AutomationServiceRole'
aws iam put-role-policy --role-name=$rolename --policy-name $addpolicy --policy-document file://autos3policy.json
```

## 配置Lambda
新建一个python 3.8环境的lambda function后,需要配置两个环境变量
rolearn就是在第一步使用cloudformation生成的role的ARN
```
documentname	AWSConfigRemediation-ConfigureS3BucketPublicAccessBlock
rolearn	arn:aws:iam::<accoundid>:role/AutomationServiceRole
```

### 需要给现有的lambda Role 增加调用automation的权限,运行

```
  ,
        {
            "Action": "ssm:StartAutomationExecution",
            "Effect": "Allow",
            "Resource": [
                "arn:aws:ssm:<region>:*:automation-definition/AWSConfigRemediation-ConfigureS3BucketPublicAccessBlock:$DEFAULT"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": "arn:aws:iam::<accoundid>:role/AutomationServiceRole",
            "Condition": {
                "StringLikeIfExists": {
                    "iam:PassedToService": "ssm.amazonaws.com"
                }
            }
        }
```
