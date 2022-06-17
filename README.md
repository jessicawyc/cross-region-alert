# 1.Public S3 Preventive Control
使用AWS Organizationsalce,将所有需要公开的S3放在一个OU下边,将其它OU attach [scp-no-public-s3](/scp-no-public-s3)以阻止任何人打开account级别的S3 public
# 2.Public S3 Auto Block
通过lambda读取securityhub发出的event,调用SSM-automation对公开的S3进行自动修复
## 2.1 Securityhub中的基本配置方法
请见[alertconfig.md](/alertconfig.md)
## 2.2 Lambda自动化处理的配置方法
请见[publics3.md](/publics3.md)
# 3.Public S3 Sensitive Data detection
在Securityhub中接收到新打开public S3的finding后,自动启动macie对S3进行自动扫描,检查S3是否存在敏感数据
请详见
https://github.com/jessicawyc/macie-auto-scan-public/tree/main

当发现保存有sensitive data的S3设置为public时,securityhub自动生成一条SIEM Alert
请详见:
https://github.com/jessicawyc/securityhub-siem-insight/tree/main/s3
