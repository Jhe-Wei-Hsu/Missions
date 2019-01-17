# Mission1 AWS白皮書閱讀

## 目標

同學們，能夠練習自讀白皮書，並嘗試抓出摘要與速讀，並進行聯想關練。


## 參考連結

https://d1.awsstatic.com/whitepapers/zh_TW/aws-overview.pdf


## 任務描述

骨肉分離，開一個新的Paper，將此文件的大綱列出，並把各綱裡的子目錄一並抓回，形成一個骨幹綱要，並以大小標標註之。

寫完之後，在Paper最上方寫一段閱讀後的感受。

----------
# 心得：
1. 可能**幫企業省錢**的定價方式：隨需、立即可用、按用量付費、節省基礎設施開銷
2. **幫企業省時間**的作法：按需佈建所需硬體資源類型、規模、運算等級，不用花時間及精力評估硬體需求。
3. **此白皮書中簡要列出所有服務的主要特點**(建議用關鍵字查詢原白皮書)。
4. 私有雲能做到的事，公有雲都做得到；**私有雲做不到的事，公有雲還是做得到**。
5. AWS的服務和相關文件非常詳盡，不該想著將所有服務都弄懂，而是**應該瞭解其應用核心概念**，並且知道該在哪個子平台尋找要使用的功能。
# 介紹 

Amazon Web Services **(AWS) 從 2006 年開始**以 Web 服務的形式為企業提供 IT 基礎設施服務，也稱為**雲端運算**。雲端運算的主要優點，就是能以可變成本(依業務需求調整)取代企業(前期)基礎設施支出。

----------
# 什麼是雲端運算？ 

透過雲端平台，依用量付費，經由網際網路提供計算、儲存、網路三大資源池，以及應用程式等資源，並且企業不需要投入基礎建設硬體及維運的資金。

----------
# 雲端運算的六大優勢 
## ● 將~~大筆~~開銷轉成變動費用
    ~~有可能~~比較便宜
## ● 從規模經濟獲得優勢 
![https://wiki.mbalib.com/zh-tw/%E8%A7%84%E6%A8%A1%E7%BB%8F%E6%B5%8E](https://wiki.mbalib.com/w/images/4/4f/Economies_of_scale.png)



## ● 停止預估容量
    用多少算多少
## ● 速度和靈活性
    迅速部署
## ● 停止花費資金在自有資料中心的營運及維護
    然後花費資金在AWS雲服務上
## ● 幾分鐘內將業務擴展到全球
    降低延遲，提高可用性
----------
# 雲端運算的類型 
## ● 雲端運算模型 

**① 基礎設施即服務 (IaaS)**

    可自由運用三大資源池

**② 平台即服務 (PaaS)**

    應用已套裝的硬體及作業系統，其上的應用程式管理交由使用者自訂。

**③ 軟體即服務 (SaaS)**

    就是賣軟體或單一服務，比如E-MAIL服務。


## ● 雲端運算部署模型 

**①** [**雲端**](https://aws.amazon.com/tw/what-is-cloud-computing/)
**②** [**混合**](https://aws.amazon.com/tw/enterprise/hybrid/)**(混合雲)**
**③** [**現場部署**](https://aws.amazon.com/tw/enterprise/hybrid/)**(私有雲)**

----------
# [全球基礎設施](https://aws.amazon.com/tw/about-aws/global-infrastructure/) 

AWS的基礎建設及備援機制介紹。
AWS 雲端基礎設施以區域與可用區域 (Available Zones) 為中心來建置的。有多個 「AZ」的實體位置稱為「區域」(Region)。AZ 由一或多個分散的資料中心所組成，每個都有備援電源、聯網和連線能力，且置放在不同的機構。

----------
# 安全與合規
## ● [安全性](https://aws.amazon.com/tw/security/) 
  - 保護資料安全、達到合規要求、省錢、快速擴展
  - AWS 雲端可提供共同的責任模式。AWS 會管理雲端本身的安全，但雲端內部的安全用戶要自行負責。
## ● [合規](https://aws.amazon.com/tw/compliance/) 
  - 各式國際標準，可在[風險與合規白皮書](http://d0.awsstatic.com/whitepapers/compliance/AWS_Risk_and_Compliance_Whitepaper.pdf)及 [AWS 安全中心](http://aws.amazon.com/security/)取得更多詳細資訊。
----------
# Amazon Web Services 雲端平台
## ● [AWS 管理主控台](https://aws.amazon.com/tw/console/) (with [mobile](https://aws.amazon.com/tw/console/mobile/))
## ● [AWS 命令列界面](http://aws.amazon.com/cli)
## ● [軟體開發套件](https://aws.amazon.com/tools/)
## ● 運算
  - [**Amazon Elastic Compute Cloud (Amazon EC2)**](http://aws.amazon.com/ec2/)
    - 隨需執行個體
    - [預留執行個體](http://aws.amazon.com/ec2/purchasing-options/reserved-instances/)
    - [競價型執行個體](http://aws.amazon.com/ec2/purchasing-options/spot-instances/)
  - [Amazon EC2 Container Service (ECS)](http://aws.amazon.com/ecs/)
  - [Amazon EC2 Container Registry](https://aws.amazon.com/ecr/)
  - [Amazon Lightsail](https://amazonlightsail.com/)
  - [AWS Batch](https://aws.amazon.com/batch)
  - [**AWS Elastic Beanstalk**](http://aws.amazon.com/ec2/purchasing-options/spot-instances/)
    - 一種易用的服務，可在 Apache、Nginx、Passenger 和 Internet Information Services (IIS) 等類似的伺服器上，部署及擴展以 Java、.NET、PHP、Node.js、 Python、Ruby、Go 及 Docker 等開發的 Web 應用程式與服務。
    - AWS Elastic Beanstalk 可自動進行部署，從容量佈建、負載平衡、自動擴展到應用程式健全狀況監控等。
  - [**AWS Lambda**](http://aws.amazon.com/lambda/)
    -  Lambda 可執行幾乎任何類型應用程式或後端服務的程式碼，且無需任何管理。
    - 只需支付使用時的運算時間，未執行程式碼時無需付費。
  - [Auto Scaling](http://aws.amazon.com/autoscaling/)
## ● 儲存
  - [**Amazon Simple Storage Service (Amazon S3)**](http://aws.amazon.com/s3/)
    - 簡便、耐久、可擴展性、安全無虞、可用性、低成本、簡易資料傳輸、整合性、易於管理
  - [**Amazon Elastic Block Store**](http://aws.amazon.com/ebs/)
    - 高效能磁碟區、可用性、加密、存取管理、快照
  - [Amazon Elastic File System](https://aws.amazon.com/efs/)
  - [Amazon Glacier](http://aws.amazon.com/glacier/)
  - [AWS Storage Gateway](http://aws.amazon.com/storagegateway/)
## ● 資料庫
  - [Amazon Aurora](https://aws.amazon.com/rds/aurora/)
    - 高效能、高度安全、MySQL和PostgreSQL相容、可高度擴展、高可用性、耐久性、全受管
  - [Amazon Relational Database Service (Amazon RDS)](http://aws.amazon.com/rds/)
    - 快速且易設定、可高度擴展、可用與耐久、安全無虞、經濟實惠
    - 支援PostgreSQL, MySQL, MariaDB, Oracle, Microsoft SQL Server
  - [Amazon DynamoDB](http://aws.amazon.com/dynamodb/)
    - 快速一致的效能、可高度擴展、全受管、靈活
    - 事件驅動程式設計-整合AWS [Lambda](http://aws.amazon.com/lambda/)
    - 更精細的存取控制權-整合AWS [IAM](http://aws.amazon.com/iam/)
  - [Amazon ElastiCache](http://aws.amazon.com/elasticache/)
    - 支援兩種記憶體內引擎：[Redis](https://aws.amazon.com/elasticache/)、[Memcached](http://www.memcached.org/)
## ● 遷移
  - [AWS Application Discovery Service](https://aws.amazon.com/application-discovery)
  - [AWS Database Migration Service](https://aws.amazon.com/dms/)
  - [AWS Server Migration Service](https://aws.amazon.com/server-migration-service)
  - [AWS Snowball](https://aws.amazon.com/snowball/)
  - [AWS Snowball Edge](https://aws.amazon.com/snowball-edge)
  - [AWS Snowmobile](https://aws.amazon.com/snowmobile)
## ● 聯網與內容交付
  - [Amazon Virtual Private Cloud (Amazon VPC)](http://aws.amazon.com/vpc/)
  - [Amazon CloudFront](http://aws.amazon.com/cloudfront/)
  - [Amazon Route 53](http://aws.amazon.com/route53/)
  - [AWS Direct Connect](http://aws.amazon.com/directconnect/)
  - [Elastic Load Balancing](http://aws.amazon.com/elasticloadbalancing/)
## ● 開發人員工具
  - [AWS CodeCommit](https://aws.amazon.com/codecommit/)
  - [AWS CodeBuild](https://aws.amazon.com/codebuild)
  - [AWS CodeDeploy](https://aws.amazon.com/codedeploy/)
  - [AWS CodePipeline](https://aws.amazon.com/codepipeline/)
  - [AWS X-Ray](https://aws.amazon.com/xray)
## ● 管理工具 
  - [**Amazon CloudWatch**](http://aws.amazon.com/cloudwatch/)
    - 一項針對 AWS 雲端資源和在 AWS 上執行的應用程式進行監控的服務。CloudWatch 可以收集和追蹤指標、收集和監控日誌檔、設定警示，以及自動對 AWS 資源的變更做出反應。
  - [**Amazon EC2 Systems Manager**](https://aws.amazon.com/ec2/systems-manager/)
    - 工具：Run Command、狀態管理員、庫存、維護時段、修補程式管理員、自動化、參數存放區
  - [AWS CloudFormation](http://aws.amazon.com/cloudformation/)
  - [AWS CloudTrail](http://aws.amazon.com/cloudtrail/)
  - [AWS Config](https://aws.amazon.com/config/)
  - [AWS OpsWorks](https://aws.amazon.com/opsworks/)
  - [AWS Service Catalog](http://aws.amazon.com/servicecatalog/)
  - [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor/)
  - [AWS Personal Health Dashboard](https://aws.amazon.com/premiumsupport)
  - [AWS Managed Services](https://aws.amazon.com/managed-services)
## ● 安全、身分和合規產品
  - Amazon Cloud Directory
  - AWS Identity and Access Management
  - Amazon Inspector
  - AWS Certificate Manager
  - AWS CloudHSM
  - AWS Directory Service
  - AWS Key Management Service
  - AWS Organizations
  - AWS Shield
  - AWS WAF
## ● Analytics
  - Amazon Athena
  - Amazon EMR
  - Amazon CloudSearch
  - Amazon Elasticsearch Service
  - Amazon Kinesis
    - Amazon Kinesis Firehose
    - Amazon Kinesis Analytics
    - Amazon Kinesis Streams
  - Amazon Redshift
  - Amazon QuickSight
  - AWS Data Pipeline
  - AWS Glue
## ● 人工智慧
  - Amazon Lex
  - Amazon Polly
  - Amazon Rekognition
  - Amazon Machine Learning
## ● 行動服務
  - AWS Mobile Hub
    - 應用程式分析、應用程式內容交付、雲端邏輯、NoSQL資料庫、推送通知、使用者資料儲存、使用者登入、連接器、對話型機器人、使用者互動
    - Amazon Cognito
    - Amazon Pinpoint
    - AWS Device Farm
    - AWS Mobile SDK
    - Amazon Mobile Analytics
## ● 應用程式服務
  - AWS Step Functions
  - [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
    - 一種全受管的服務，可讓開發人員輕鬆地建立、發佈、維護、監控和保護任何規模的 API。
  - Amazon Elastic Transcoder
  - Amazon SWF
## ● 簡訊
  - Amazon SQS
  - Amazon SNS
  - Amazon SES
## ● 商業生產力
  - Amazon WorkDocs
  - Amazon WorkMail
  - Amazon Chime
## ● 桌面和應用程式串流
  - Amazon WorkSpaces
  - Amazon AppStream 2.0
## ● 物聯網
  - AWS IoT 平台
  - AWS Greengrass
  - AWS IoT Button
## ● 遊戲開發
  - Amazon GameLift
  - Amazon Lumberyard


----------
# 後續步驟

如何開始使用AWS

## ● [介紹短片](https://aws.amazon.com/training/intro_series/)


----------
# 結論

 AWS 提供的服務可迅速的結合在一起，用於支援幾乎所有的工作。


----------
# 作者群

族繁不及備載，詳見[原白皮書](https://d1.awsstatic.com/whitepapers/zh_TW/aws-overview.pdf)。


