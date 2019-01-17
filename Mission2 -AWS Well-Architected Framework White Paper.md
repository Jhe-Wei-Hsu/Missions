# Mission2 AWS白皮書閱讀


## 目標

理解雲架構的設計原則與神髓


## 參考資料

https://d1.awsstatic.com/whitepapers/architecture/AWS_Well-Architected_Framework.pdf


## 任務描述

骨肉分離，開一個新的Paper，將此文件的大綱列出，並把各綱裡的子目錄一並抓回，形成一個骨幹綱要，並以大小標標註之。

寫完之後，在Paper最上方寫一段閱讀後的感受。

閱讀全文，並將自己覺得重要的點，摘錄在Paper中。

----------
# Summary
1. AWS曾經面對過的問題和處理過的客戶很多，這是他們的經驗濃縮。
2. 本文多次提及AWS Cloud Watch，看起來是核心產品之一。
3. 五大支柱總結了所有在使用AWS可能遇到的問題面向。
4. 這本白皮書更偏向教你如何找到使用AWS時遇到問題的Trouble Shooting
5. 在白皮書中多次提到了變動的概念，說明AWS很清楚整個雲端的趨勢目前仍是不停變化的，所以他們也有一個Developer的論壇可供使用者討論，類似開源與共享的知識概念。
## 
## 
## 
# Introduction
## ● Definitions
## 前言：aws經驗豐富。
## **The** **5** **pillars of the AWS Well-Architected Framework**
6. Operational Excellence
7. Security
8. Reliability
9. Performance Efficiency
10. Cost Optimization(成本優化)
## 
## ※Some keyword: component, workload, milestones, architecture, techonology portfolio.
## 
## ● On Architecture
## 看不太懂，大概是關於客戶的架構決策和aws之前的經驗之類。
## ● General Design Principles
- **Stop guessing your capacity needs****-就是字面上的意思，用多少算多少。**
- **Test systems at production scale****--以實際上線的方式測試，但付出的成本較實際上線低。**
- **Automate to make architectural experimentation easier****-自動化**
- **Allow for evolutionary architectures**
- **Drive architectures using data-透過數據收集改善架構**
- **Improve through game days****-突發事件測試**
## 
# The Five Pillars of the Framework
![](https://d2mxuefqeaa7sj.cloudfront.net/s_59B9273F2F229588371304C2B28A5C30F341D6672B8B10288837AD4147475CE2_1545219609145_image.png)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_F61EE6377B8B7DCE82DDD3016E966D6C03F9973CBC962A22B3B32DE00D104951_1545223998885_Snipaste_2018-12-19_17-46-15.png)

## 1. Operational Excellence
## **Design Principles**
## **Definition**
## Best Practices
## Prepare
## Operate
## Evolve
## 
## **Key AWS Services**
## Prepare
## Operate
## Evolve
## 
## **Resources**
## Documentation-[DevOps and AWS](https://aws.amazon.com/devops/)
## Whitepaper-[Operational Excellence Pillar](https://d0.awsstatic.com/whitepapers/architecture/AWS-Operational-Excellence-Pillar.pdf)
## Video-[DevOps at Amazon](https://www.youtube.com/watch?v=esEFaY0FDKc)
## 
## 2. Security
## **Design Principles**
## Implement a strong identity foundation
##  Enable traceability
## Apply security at all layers
## Automate security best practices
## Protect data in transit and at rest
## Keep people away from data
## Prepare for security events
## 
## **Definition**
1. Identity and Access Management
2. Detective Controls
3. Infrastructure Protection
4. Data Protection
5. Incident Response
## 
## **Best Practices**
## Identity and Access Management
## Detective Controls
## Infrastructure Protection
## Data Protection
## Incident Response
## 
## **Key AWS Services**
## Identity and Access Management
## Detective Controls
## Infrastructure Protection
## Data Protection
## Incident Response
## 
## **Resources**
## Documentation
  •        AWS Cloud Security
  •        AWS Compliance
  •        AWS Security Blog
## Whitepaper
  •        Security Pillar
  •        AWS Security Overview
  •        AWS Security Best Practices
  •        AWS Risk and Compliance
## Video
  •        AWS Security State of the Union
  •        Shared Responsibility Overview
## 3. Reliability
## **Design Principles**
## Test recovery procedures
## Automatically recover from failure
## Scale horizontally to increase aggregate system availability
## Stop guessing capacity
## Manage change in automation
## 
## **Definition**
6. Foundations 
7. Change Management 
8. Failure Management
## 
## **Best Practices**
## Foundations
## Change Management
## Failure Management
## 
## **Key AWS Services**
## Foundations
## Change Management
## Failure Management
## 
## **Resources**
## Documentation
  •        Service Limits
  •        Service Limits Reports Blog
  •        Amazon Virtual Private Cloud
  •        AWS Shield
  •        Amazon CloudWatch
  •        Amazon S3
  •        AWS KMS
## Whitepaper
  •        Reliability Pillar
  •        Backup Archive and Restore Approach Using AWS
  •        Managing your AWS Infrastructure at Scale
  •        AWS Disaster Recovery
  •        AWS Amazon VPC Connectivity Options
## Video
## Product
## 4. Performance Efficiency
## **Design Principles**
## Democratize advanced technologies
## Go global in minutes
## Use serverless architectures
## Experiment more often
## Mechanical sympathy
## 
## **Definition**
9. Selection
10. Review
11. Monitoring
12. Tradeoffs
## 
## **Best Practices**
## Selection
  - Compute
    - Instances
    - Containers
    - Functions
  - Storage
  - Database
  - Network
## Review
## Monitoring
## Tradeoffs
## 
## **Key AWS Services**
## Selection
  - Compute
  - Storage
  - Database
  - Network
## Review
## Monitoring
## Tradeoffs
## 
## **Resources**
## Documentation
  •        Amazon S3 Performance Optimization
  •        Amazon EBS Volume Performance
## Whitepaper
  Performance Eﬃciency Pillar
## Video
  •        AWS re:Invent 2016: Scaling Up to Your First 10 Million Users (ARC201)
  •        AWS re:Invent 2017: Deep Dive on Amazon EC2 Instances
## 
## 5.Cost Optimization
## **Design Principles**
## Adopt a consumption model
## Measure overall efficiency
## Stop spending money on data center operations
## Analyze and attribute expenditure
## Use managed and application level services to reduce cost of ownership
## 
## **Definition**
## Expenditure Awareness
## Cost-Effective Resources
## Matching supply and demand
## Optimizing Over Time
## 
## **Best Practices**
## Expenditure Awareness
## Cost-Effective Resources
## Matching supply and demand
## Optimizing Over Time
## 
## **Key AWS Services**
## Expenditure Awareness
## Matching supply and demand
## Optimizing Over Time
## 
## **Resources**
## Documentation
  •        Analyzing Your Costs with Cost Explorer
  •        AWS Cloud Economics Center
  •        AWS Detailed Billing Reports
## Whitepaper
  Cost Optimization Pillar
## Video
  Cost Optimization on AWS
## Tool
  •        AWS Total Cost of Ownership (TCO) Calculators
  •        AWS Simple Monthly Calculator
## 
# The Review Process
## 審查流程
# Conclusion
# Contributors
# Further Reading
# Document Revisions
# Appendix: Questions, Answers, and Best Practices
## 
## 

