# 1.Public S3 Preventive Control
将所有需要公开的S3放在一个OU下边,将其它OU attach [scp-no-public-s3](/scp-no-public-s3)以阻止打开
# 2.Public S3 Auto Block Auto Remediation
通过lambda读取securityhub发出的event,调用SSM-automation对公开的S3进行自动修复
## 2.1 Securityhub中的基本配置方法
请见
## 2.2 后台自动化处理的配置方法
请见
# 3.Public S3 Sensitive Data detection
使用macie对新打开public access 的S3进行自动扫描,检查是否存在敏感数据
https://github.com/jessicawyc/macie-auto-scan-public/tree/main
