# securityhub-auto-remediation

## standard control
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
