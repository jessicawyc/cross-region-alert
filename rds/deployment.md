# Deployment Process 部署说明

请下载所有文件到本地 Download all the related files here
### Set Parameter参数设置
```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text))
function='rds-replicate-siem'
lambdapolicy='lambda-rds-replicate-siem-policy'
rolename='lambda-rds-replicate-siem'
function='rds-replicate-siem'
rolearn=$(aws iam create-role --role-name $rolename --assume-role-policy-document file://trust-lambda.json --query 'Role.Arn' --output text)
aws iam put-role-policy --role-name=$rolename --policy-name $lambdapolicy --policy-document file://lambdapolicy.json
```

## Create Lambda in each region
```
for region in $regions; do
echo region
lambdaarn=$(aws lambda create-function \
    --function-name $function \
    --runtime python3.9 \
    --zip-file fileb://index.zip \
    --handler index.lambda_handler \
    --role $rolearn --region=$region --no-cli-pager --query 'FunctionArn' --output text)
done
```
