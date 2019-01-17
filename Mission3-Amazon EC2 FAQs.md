# Mission3 AWS服務QnA閱讀


## 目標

知道AWS官方產品通常會有QnA，這些QnA經常出現在考題與工作情境中。


## 參考資料


https://aws.amazon.com/tw/ec2/faqs/



## 任務描述

看過問題大綱要，看過問題描述，把自己覺得不錯或不會的QA摘要進一份Paper中。

並針對不會的QA，再進行額外資料搜索，將搜索到的資料，放在該Paper該問題的下方。
 

----------
# [一般問題](https://paper.dropbox.com/doc/Amazon-EC2--AUKFEst2TKbVU2TLK_HU7GlHAg-bEPXcqVRSFcCnkm649e5j#:uid=352338735166992942697134&h2=%E4%B8%80%E8%88%AC%E5%95%8F%E9%A1%8C)

**問：開發人員現在可以實現哪些以前無法做到的事情？**
Amazon EC2無須前期投資，也不影響效能。
足夠「彈性」可讓開發人員即時擴展，滿足流量或需求上限。當運算需求改變時，也可以即時反應，開發人員可隨時控制資源用量。
(傳統託管服務通常在固定時段內提供固定資源，表示當用量快速變化時，使用者反應能力會受限)

**問：如何在 Amazon EC2 環境中執行系統？**

1. API：**應用程式介面**（英語：**a**pplication **p**rogramming **i**nterface，縮寫作 **API**），就是[軟體](https://zh.wikipedia.org/wiki/%E8%BD%AF%E4%BB%B6)系統不同組成部分銜接的協定。~~由於近年來軟體的規模日益龐大，常常需要把複雜的系統劃分成小的組成部分，編程介面的設計十分重要。程式設計實踐中，編程介面的設計首先要使軟體系統的職責得到合理劃分。良好的~~[~~介面~~](https://zh.wikipedia.org/wiki/%E6%8E%A5%E5%8F%A3)~~設計可以降低系統各部分的相互依賴，提高組成單元的~~[~~內聚性~~](https://zh.wikipedia.org/wiki/%E5%85%A7%E8%81%9A%E5%8A%9B_(%E8%A8%88%E7%AE%97%E6%A9%9F%E7%A7%91%E5%AD%B8))~~，降低組成單元間的~~[~~耦合~~](https://zh.wikipedia.org/wiki/%E8%80%A6%E5%90%88%E5%8A%9B_(%E8%A8%88%E7%AE%97%E6%A9%9F%E7%A7%91%E5%AD%B8))~~程度，從而提高系統的可維護性和可延伸性。~~
2. [Amazon EC2 Spot 執行個體](https://aws.amazon.com/tw/ec2/spot/)
   AWS 雲端中的**備用運算容量**，可提供相對於隨需價格更高的折扣。EC2 Spot 執行個體可優化 AWS 雲端成本，您可以相同的預算將應用程式的輸送量擴展高達 10 倍。您只需在啟動 EC2 執行個體時選擇 Spot，就能將成本降到隨需價格的十分之一。
3. [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/tw/ebs/) 
  可在 AWS 雲端提供用於 [Amazon EC2](https://aws.amazon.com/tw/ec2/) 執行個體的**持久性區塊儲存磁碟區**。每個 Amazon EBS 磁碟區會在其可用區域內自動複寫，以保護您免於元件故障的威脅，同時提供高可用性和耐久性。Amazon EBS 磁碟區為您提供執行工作負載所需的一致性和低延遲效能。

**問：對於****根裝置****，使用本機執行個體存放區與使用 Amazon Elastic Block Store (Amazon EBS) 有什麼區別？**
啟動 Amazon EC2 執行個體時，您可以將根裝置資料存放在 Amazon EBS 或者本機執行個體存放區上。使用 Amazon EBS 時，根裝置中的資料將獨立於執行個體的存留期保留下來。這可讓您停止執行個體並在以後重新啟動，與您將筆記型電腦關機並在再次需要時重新啟動相似。
另一方面，本機執行個體存放區僅在執行個體的生命週期內保留。這是一種最經濟的啟動執行個體方式，因為資料沒有存放到根裝置中。例如，有些客戶使用此選項執行大型網站，透過複製每個執行個體來應對 Web 流量。

**問：Amazon EC2 是否與 Amazon S3 結合使用？--就是我們上課幹的事**
對於具備本機執行個體儲存體支援之根裝置的執行個體，Amazon EC2 與 Amazon S3 可結合使用。藉助 Amazon S3，開發人員可以存取 Amazon 用於執行其全球網站網路的資料儲存體基礎設施，它不僅具備高度的可擴展性和可靠性，而且快速、經濟實惠。為了能在 Amazon EC2 環境中執行系統，開發人員使用提供的工具將其 AMI 載入 Amazon S3 中，並在 Amazon S3 和 Amazon EC2 之間移動。請參閱[如何使用 Amazon EC2 載入並存放我的系統](https://aws.amazon.com/tw/ec2/faqs/#How_do_I_load_and_store_my_systems_with_Amazon_EC2)以獲得更多有關 AMI 的詳細資訊。

**問：我可以在 Amazon EC2 中執行多少個執行個體？**
記得這裡有張表可以參考即可。

**問：Amazon EC2 是否使用 ECC 記憶體？**
簡言之，有。
**修正錯誤記憶體**（英語：Error-correcting code memory，縮寫**ECC memory**），即能夠實現錯誤檢查和糾正錯誤技術的內存。ECC內存還需要[CPU](https://zh.wikipedia.org/wiki/CPU)和[主板](https://zh.wikipedia.org/wiki/%E4%B8%BB%E6%9D%BF)支持，並在[BIOS](https://zh.wikipedia.org/wiki/BIOS)中進行相應的設置，目前只應用在大多數[伺服器](https://zh.wikipedia.org/wiki/%E4%BC%BA%E6%9C%8D%E5%99%A8)主板。

----------
# 計費

**問：使用 Amazon EC2 如何計價和收費？**
按用量付費。顯示的定價是小時費率，但視執行個體而定，可能需要為執行個體類型支付每小時或每秒 (最低限制 60 秒) 費率。執行未滿一小時的執行個體依執行個體用量計費。
**在不同區域的 AWS 服務之間傳輸資料**時，將在**傳輸的兩端收取網際網路數據傳輸費**。其他 Amazon Web Services 的使用與 Amazon EC2 分開計費。
有關 EC2 定價資訊，請瀏覽 [EC2 詳細資訊頁面上的定價部分](https://aws.amazon.com/ec2/pricing/)。

**問：我的 Amazon EC2 系統的帳單週期怎麼計算？**
從 Amazon EC2 啟動 AMI 執行個體的啟動序列時開始計費。該執行個體終止時停止計費。
**停止執行個體時**，不會收取已停止執行個體的費用，但是**會收取**任何 Amazon **EBS 磁碟區儲存的費用**。若要進一步了解，請瀏覽 [AWS 文件](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html)。

**問：如果我有兩個執行個體分別在不同的區域，那麼資料傳輸將如何收費？**
每個執行個體需按照網際網路資料傳輸費用收取資料傳入和傳出費。
如果這兩個執行個體之間傳輸資料，則**第一個**執行個體需收取網際網路**資料傳出費**，**第二個**執行個體需收取網際網路**資料傳入費**。

**問：價格含稅嗎？**
簡言之，除日本外都不用。

----------
# 硬體資訊

**問：我的應用程式堆疊將在哪類硬體上執行？**
請直接參閱 [Amazon EC2 執行個體類型](https://aws.amazon.com/ec2/instance-types/)

**問：什麼是「EC2 運算單位」，為什麼要引入此單位？**
又稱ECU。
Amazon EC2 透過多種衡量標準，為每個執行個體提供一致且可預計的 CPU 容量。為了便於開發人員可以在不同的執行個體類型之間比較 CPU 容量，定義了 Amazon EC2 運算單位。
分配給特定執行個體的 CPU 量以 EC2 運算單位來表示，並以 EC2 運算單位來管理效能的一致性和可預計性。

**問：Amazon EC2 執行個體類型的區域可用性如何？**
請參閱 [Amazon EC2 定價。](https://aws.amazon.com/ec2/pricing/)

----------
# 安全性

如需 AWS 安全性的詳細資訊，請參閱 [Amazon Web Services：安全程序概觀](https://d1.awsstatic.com/whitepapers/aws-security-whitepaper.pdf)白皮書和 [Amazon EC2 running Windows Security Guide](http://developer.amazonwebservices.com/connect/entry.jspa?externalID=1767)。

----------
# 彈性 IP

結論：一般用戶只需要5個公有IP，有更多需求請向AWS申請。

**問：為什麼我的彈性 IP 地址與執行中的執行個體沒有關聯時需要收費？**
因為公有IP要錢，佔著不用是浪費資源。

**問：是否可以為彈性 IP 地址配置反向 DNS 記錄？**
可以配置彈性 IP 地址的反向 DNS 記錄。請注意，必須有指向該彈性 IP 地址的對應正向 DNS 記錄，才能建立反向 DNS 記錄。

----------
# 可用區域

**問：如何確保我與另一開發人員處於同一可用區域中？**
我們目前不支援協調不同 AWS 開發人員帳戶啟動到同一可用區域的功能。

----------
# Nitro Hypervisor

**問：什麼是 Nitro Hypervisor？**
C5 執行個體推出後引進了全新的 Hypervisor，也就是 Nitro Hypervisor。
Nitro Hypervisor 是 Nitro 系統的一個元件，主要為 EC2 執行個體**提供 CPU 和記憶體隔離**。VPC 聯網和 EBS 儲存資源由專用硬體元件 Nitro Card 實作，該元件是所有最新一代 EC2 執行個體系列的一部分。Nitro Hypervisor 採用核心 Linux Kernel 虛擬機器 (KVM) 技術，但不包含一般用途作業系統元件。
**簡言之，比傳統虛擬化效能更好的虛擬化。**

**問：Nitro Hypervisor 如何讓客戶受惠？**
Nitro Hypervisor 透過移除主機系統軟體元件，為 EC2 虛擬執行個體提供一致的效能和增強的運算和記憶體資源。這可讓 AWS 提供較大的執行個體大小 (像是 c5.18xlarge)，將伺服器中幾乎所有資源提供給客戶。

![http://www.brendangregg.com/blog/2017-11-29/aws-ec2-virtualization-2017.html](http://www.brendangregg.com/blog/images/2017/ec2-types-numbered.png)


**問：是否所有 EC2 執行個體都將使用 Nitro Hypervisor？**
最終所有新的執行個體類型都將使用 Nitro Hypervisor

**問：使用 Xen Hypervisor 和使用 Nitro Hypervisor 的執行個體是否會有不同？**
是。例如，在 Nitro Hypervisor 下執行的執行個體是從使用 NVMe 界面的 EBS 磁碟區啟動。在 Xen 下執行的執行個體從模擬的 IDE 硬碟啟動，再切換到 Xen 半虛擬化區塊型儲存設備驅動程式。


# 增強型聯網

**問：此功能包含哪些聯網功能？**
目前，我們使用 SR-IOV (單一根 I/O 虛擬化) 支援增強型聯網功能。SR-IOV 是一種裝置虛擬化方法，與傳統實作相比，它不僅能提高 I/O 效能，同時還能降低 CPU 利用率。

**問：使用增強型聯網是否需要支付額外的費用？**
不需要，增強型聯網沒有額外費用。要利用增強型聯網，必須在 VPC 中受支援的執行個體類型上啟動相應的 AMI。

**問： 哪些執行個體類型提供 NVMe 執行個體儲存體？**
高 I/O 執行個體使用以 NVMe 為基礎的本機執行個體儲存體，為應用程式提供極高的低延遲性和 I/O 容量，最適合需要數百萬 IOPS 的應用程式。

# Elastic Fabric Adapter (EFA)

**問：為什麼應該使用 EFA？**
EFA 為緊密耦合的 HPC 應用程式提供雲端的可擴展性、靈活性和彈性。緊密耦合的 HPC 應用程式可透過 EFA 存取比傳統 TCP 管道更低、更一致的延遲和更高的輸送量，以提高擴展能力。

**問：哪些類型的應用程式可受益於使用 EFA？**
高效能運算 (HPC) 應用程式可在一個執行個體叢集分配運算工作負載，以便進行平行處理。HPC 應用程式的範例包括計算流體動力學 (CFD)、碰撞模擬和天氣模擬。

**問：哪些執行個體類型支援 EFA？**
EFA 目前可用於 C5n.18xlarge、C5n.9xlarge 和 P3dn.24xl 執行個體大小。

**問：現在是否可使用 EFA？**
EFA 目前提供預覽模式。請[註冊](https://pages.awscloud.com/elastic-fabric-adapter-preview.html)申請存取權

----------
# Amazon Elastic Block Store (EBS)

**問：系統終止時我的資料會發生什麼情況？**
存放於本機執行個體存放區中的資料僅在執行個體存活期間保留。不過，存放在 Amazon EBS 磁碟區上的資料將獨立於執行個體的生命週期保留下來。
建議將**本機執行個體存放區用於臨時資料**，而對於**需要保存較長時間的資料**，**建議使用 Amazon EBS 磁碟區**，或將資料**備份到 Amazon S3**

**問：Amazon EBS 磁碟區預計可以給我帶來什麼樣的效能？**
Amazon EBS 提供四種最新一代的磁碟區類型，其可分成兩種主要類別：適用於交易工作負載的 SSD 支援儲存和適用於輸送量密集型工作負載的 HDD 支援儲存。
如需詳細資訊，請參閱 [EBS 產品詳細資訊頁面](https://aws.amazon.com/ebs/details/)；如需有關效能的其他資訊，請參閱 [Amazon EC2 使用者指南的 EBS 效能部分](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSPerformance.html)。

**問：什麼是輸送量最佳化 HDD (st1) 和冷 HDD (sc1) 磁碟區類型？**
ST1 磁碟區由硬碟 (HDD) 提供支援，非常適合用於經常存取、包含龐大資料集和大型 I/O 的輸送量密集型工作負載
SC1 磁碟區是由硬碟 (HDD) 提供支援，並提供所有 EBS 磁碟區類型中每 GB 的最低成本。它非常適合包含大量不常使用資料集且存取頻率較低的工作負載。與 st1 類似，sc1 提供高載模式

**問：是否支援多個執行個體存取一個磁碟區？**
**目前不支援**。

**問：使用 Amazon EBS 共享快照時如何收費？**
如果您共享快照，則**其他使用者製作您快照的複本時**，免費。如果您**製作其他使用者的共享磁碟區的複本**，會收取正常的 **EBS 費用**。

**※EBS快照區分為Private及Public，別人分享過來的會在Private，另外Amazon EBS 磁碟區和快照可以加密**

相關問題請參閱 [Amazon EBS 常見問答集頁面](https://aws.amazon.com/ebs/faqs/)。

----------
# Amazon Elastic File Storage (EFS)

**問：如何從 Amazon EC2 執行個體存取檔案系統？**
**使用標準 Linux 掛載命令**及檔案系統的 DNS 名稱，將檔案系統掛載在 Amazon EC2 以 Linux 為基礎的執行個體上。
**Amazon EFS 與所有 Amazon EC2 執行個體類型相容**，且可從 Linux AMI 存取。您可以混合和搭配與單一檔案系統連接的執行個體類型。

**問：如何將資料載入檔案系統？**
可將資料從 Amazon EC2 執行個體或現場部署資料中心伺服器載入 Amazon EFS 檔案系統。

**問：如何從 VPC 外存取檔案系統？**
VPC 內的 Amazon EC2 執行個體可以直接存取檔案系統，而 VPC 外的 Amazon EC2 Classic 執行個體可使用 [ClassicLink](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html) 掛載檔案系統。 
現場部署伺服器可透過到 VPC 的 [AWS Direct Connect](https://aws.amazon.com/directconnect/) 連線掛載檔案系統。

**問：可連接至檔案系統的 Amazon EC2 執行個體數量為何？**
數千，基本上正常使用時不會問到這個問題。

EFS相關問答請參閱[Amazon EFS 常見問答集頁面](https://aws.amazon.com/efs/)。

----------
# Amazon CloudWatch

**問：Amazon CloudWatch 接收和彙總資料的最小時間間隔精細度是多少？**
 1 分鐘

**問：Amazon CloudWatch 支援哪些作業系統？**
所有 Amazon EC2 執行個體，且適用於 Amazon EC2 服務目前支援的所有作業系統。

**問：如果停用某個 Amazon EC2 執行個體的監控，是否會遺失指標資料？**
可以接收自開始監控執行個體起最多 2 週內的指標資料。
兩週後，若已停用 Amazon EC2 執行個體監控，則該執行個體的指標資料將不可用。

**問：是否可以存取已終止的 Amazon EC2 執行個體或已刪除之 Elastic Load Balancer 的指標資料？**
是。 會存放 2 週的指標資料。

**問：Amazon CloudWatch 監控費用是否會因所監控的 Amazon EC2 執行個體類型而不同？**
否

----------
# Amazon EC2 Auto Scaling

[**Amazon EC2 Auto Scaling**](https://aws.amazon.com/ec2/autoscaling/?sc_channel=ba&sc_campaign=ec2-autoscaling&sc_country=mult&sc_geo=mult&sc_category=mult&sc_outcome=aware) **是全受管服務**，旨在自動啟動或終止 Amazon EC2 執行個體，以確保擁有足夠的 Amazon EC2 執行個體數量來處理應用程式負載。
EC2 Auto Scaling 可協助您透過 EC2 執行個體的叢集管理來維護應用程式可用性，叢集管理可偵測並替換運作狀態不佳的執行個體，並根據您定義的條件，自動擴展或縮減的 Amazon EC2 容量。

詳細資訊，請參閱 [Amazon EC2 Auto Scaling 常見問答集](https://aws.amazon.com/ec2/autoscaling/faqs)。

----------
# Elastic Load Balancing

**問：Elastic Load Balancing 服務提供哪些負載平衡選項？**
Elastic Load Balancing 提供兩種類型的負載平衡器，這兩者都具備高可用性、自動擴展及穩健的安全功能。
 [Classic Load Balancer](https://aws.amazon.com/elasticloadbalancing/classicloadbalancer/) ，其可依據應用程式或是網路層級的資訊來路由流量，適用於跨多個 EC2 執行個體的簡易負載平衡。
  [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/applicationloadbalancer/) 可依據進階應用程式層級的資訊 (包含請求的內容) 來路由流量，適用於需要進階路由功能、微型服務和以容器為基礎架構的應用程式。

----------
# 預留執行個體(Reserved Instances)

**問：什麼是預留執行個體？**
預留執行個體 (RI) 是一種 EC2 產品，當您簽訂一年期或三年期的合約時，可獲得 EC2 用量的大幅折扣。
使用特定的執行個體系列時，標準 RI 可為 EC2 執行個體用量提供大幅的折扣。[可轉換 RIs](https://aws.amazon.com/tw/ec2/faqs/#convertible) 則可提供您合約期間變更執行個體組態的選項，而且仍然可以獲得 EC2 用量的折扣。

**問：RI 是否提供容量保留？**
是，**當標準或可轉換 RI 的範圍涵蓋特定可用區域 (AZ)** 時，會保留完全符合 RI 組態的執行個體容量 (「**可用區域 RI**」)。
也可選擇放棄保留容量，改為購買範圍涵蓋某個區域的標準或可轉換 RI (「**區域 RI**」)。區域 RI 會自動對區域中的可用區域和執行個體大小套用用量折扣。

**問：何時需要購買可用區域 RI？**
想利用容量保留功能時。

**問：何時需要購買區域 RI？**
不需要容量保留功能時。

**問：什麼是可用區域和執行個體大小彈性？**
可用區域彈性可將 RI 折扣費率套用到區域中任何可用區域的用量，而執行個體大小彈性可將 RI 折扣費率套用到執行個體系列內任何大小的用量。

**問：哪些類型的 RI 提供執行個體大小彈性？**
含預設租用的 Linux/Unix 區域 RI 提供執行個體大小彈性。
**Windows、Windows 含 SQL Standard、Windows 含 SQL Server Enterprise、Windows 含 SQL Server Web、RHEL 與 SLES 等其他平台的 RI 不提供**執行個體大小彈性。

**問：執行個體大小彈性如何運作？**
請參閱[官網標準](https://aws.amazon.com/tw/ec2/faqs/)

**可在合約期間內變更 RI、RI 執行個體類型**

**問：RI 有哪些不同的付款選項？**
**全額預付**選項，以一次預付款支付整個 RI 期間的費用。
**部分預付**選項，支付較低的預付款，然後在 RI 的合約期間內，按折扣後的小時費率支付執行個體費用。
**不預付**選項，不需支付任何預付款，並在合約期限內提供小時費率的折扣。

**問：RI 是否適用於 Spot 執行個體或專用主機上執行的執行個體？**
否，要降低使用專用主機的成本，請購買專用主機保留。

**問：是否可在購買 RI 時獲得折扣？**
是，EC2 針對 RI 購買提供分級折扣。這些折扣是根據您在每個區域有效 RI 的總定價 (非折扣價格) 來決定。
細項請參閱[Q&A對應表](https://aws.amazon.com/tw/ec2/faqs/)
要進一步了解，請參閱[了解預留執行個體折扣定價方案](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-reserved-instances-application.html#reserved-instances-discounts)部分 (在 [Amazon EC2 使用者指南](http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/Welcome.html)中)。

**問：如果使用合併帳單，如何計算數量折扣？**
如果您使用合併帳單，AWS 將使用您所有整合帳戶中活動 RI 的總定價來確定套用哪個數量折扣層級。
若要確定目前的數量折扣層級，請參閱[了解預留執行個體折扣定價方案](http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/concepts-reserved-instances-tiers.html)部分 (在 [Amazon EC2 使用者指南](http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/Welcome.html)中)。
註--可轉換 RI 不符合數量折扣資格

----------
# 可轉換預留執行個體(Convertible RI)

一種預留執行個體類型，其屬性可在合約期間內進行變更

**問：什麼時候應該購買可轉換 RI，而不是標準 RI？**
可轉換 RI 適合可持續使用 EC2 執行個體三年以換取 EC2 大幅使用折扣、不確定未來執行個體需求或想受惠於價格變更的客戶。

**問：可轉換 RI 有哪些期限選項？**
如同標準 RI，您可以選購一年期或三年期的可轉換 RI。

**問：是否可交換可轉換 RI，以受惠於符合不同執行個體類型、作業系統、租用或付款選項的可轉換 RI？**
是，交換可轉換 RI 時，可選取新的執行個體類型、作業系統、租用或付款選項。 您還可彈性選擇要交換一部分的可轉換 RI，或在一次交換中合併多個可轉換 RI 的值。

**問：是否可將可轉換或標準 RI 從一個區域轉移到其他區域？**
否，RI 與特定區域相關聯。

**問：如何變更可轉換 RI 的組態？**
使用 EC2 管理主控台或 [GetReservedInstancesExchangeQuote API](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetReservedInstancesExchangeQuote.html)，變更可轉換 RI 的組態。 
也可彈性選擇要交換一部分的可轉換 RI，或在一次交換中合併多個可轉換 RI 的值。

**問：可轉換 RI 的交換如何運作？**
當您將一個可轉換 RI 交換成另一個，EC2 會確保轉換程序期間可轉換 RI 的總價值不會改變。

**問：總價值如何定義？**
總價值是 RI 合約期間所有預期要支付之款項的總和。

**問：逐步解說不預付可轉換 RI 之間的轉換？**
與有預付額的可轉換 RI 之間的轉換不同，由於在無預付額的 RI 之間轉換，因此無須支付校正費用。不過，交換之前依小時支付的金額必須大於或等於交換之後支付的小時數總金額。

不可自訂進行可轉換 RI 交換時收到的執行個體數
可轉換 RI 沒有交換限制，但目前只能交換 AWS 目前提供的可轉換 RI。
降價時，可轉換 RI 可享有降價優惠

----------
# 預留執行個體市場

一個線上商場，可讓 AWS 客戶能夠靈活地向其他企業和組織出售 Amazon Elastic Compute Cloud (Amazon EC2) 預留執行個體。

**問：何時能在預留執行個體市場展售預留執行個體？如何註冊成為預留執行個體市場的賣方？如何展售預留執行個體 ?**
細節參閱AWS EC2 [Q&A](https://aws.amazon.com/tw/ec2/faqs/)

**問：可以展售哪些預留執行個體？**
處於**活動狀態大於 30 天**且**已收到付款**的任何預留執行個體。
只要保留是在**作用中**，就可以展售。
注意，如果需要發票，則預留執行個體將在 AWS **收到付款之前**就已處於**作用中**狀態。在這種情況下，要等AWS收到付款後，才能展示出售該預留執行個體。

**問：是否可以轉售從預留執行個體市場購得的預留執行個體？**
是

**問：銷售預留執行個體時是否有任何限制？**
若要出售預留執行個體，必須擁有美國境內的銀行帳戶。

**問：在預留執行個體市場銷售預留執行個體是否需要支付費用？**
是，每個預留執行個體，AWS 都會收取預付總額 12% 的服務費。

**問：購買第三方預留執行個體時，對客戶是否有任何限制？**
是，不能購買自己的預留執行個體，包括任何連結帳戶 (透過合併帳單)。

----------
# 隨需容量預留

可在 Amazon EC2 上建立和管理預留的容量。
可以選擇可用區域和數量 (執行個體數量)，以及其他執行個體規格 (如執行個體類型和租用) 來建立容量保留。
建立後，即會保留 EC2 容量，而不論是否執行執行個體。**只要容量預留保持作用中**，就要為預留的所有價值付費。

**問：我何時應使用隨需容量預留，何時應使用 RI？**
當您需要獨立於 RI (折扣) 之外管理容量時，使用容量預留。
使用區域 RI 則會自動對區域中的可用區域和執行個體大小套用 RI 執行個體用量折扣。

**問：允許我預留多少個執行個體？**
取決於您帳戶的隨需執行個體限制，需要更高的限制，請聯絡 AWS 。

**問：我可以在何處找到更多有關使用容量預留的資訊？**
請參閱 [Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) 或 [windows](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-capacity-reservations.html) 技術說明文件。

----------
# EC2 叢集

使用 EC2 叢集可透過單一 API 呼叫佈建不同執行個體類型、可用區域和隨需、預留執行個體 (RI) 和 Spot 執行個體等購買模型間的運算容量

**問：如果我目前使用 Amazon EC2 Spot 機群，是否需要遷移到 Amazon EC2 機群？**
如果您透過 Spot 叢集使用 Amazon EC2 Spot 執行個體，可以繼續使用該叢集。Spot 叢集和 EC2 叢集提供相同的功能。

**Amazon EC2 叢集運用的真實世界範例？**
如大數據工作負載、容器化應用程式、網格處理工作負載等。

**不支援多個區域 EC2 叢集請求。**

----------
# 各種執行個體
## Spot 執行個體
## 微型執行個體
## 運算優化執行個體
## 加速運算執行個體
## 叢集執行個體
## 一般用途執行個體
## 儲存優化執行個體
## 記憶體優化執行個體
## 記憶體增強型執行個體
## 上一代執行個體
## 關於執行個體的優化與休眠
----------
## VM Import/Export

透過使用 VM Import/Export 匯入虛擬機器 (VM) 映像來建立 Amazon EC2 執行個體。
此外，還可以透過匯出以前匯入的 EC2 執行個體來建立 VM。也可以使用 VM Import/Export 將 VM 遷移到Amazon EC2，利用以前用於建置 VM 的投資。

如需更多 VM Import 的詳細資訊，包括支援的檔案格式、架構與作業系統組態，請參閱 [Amazon EC2 User Guide](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/VMImportPrerequisites.html) 的 VM Import/Export 章節。

----------
## 服務水準協議 (SLA)

SLA 保證在某一區域內，Amazon EC2 和 Amazon EBS 的每月正常執行時間百分比至少為 99.99%。

----------
## 較長的 EC2、EBS 和 Storage Gateway 資源 ID

**問：哪些項目會有所變更？**
從 2018 年 7 月開始，所有新建立的 EC2 資源都將收到較長的格式 ID。
新格式將只適用於新建立的資源；現有的資源不會受到影響。
執行個體和磁碟區已經使用這種 ID 格式。到 2018 年 6 月底，客戶將有權選擇使用較長的 ID。在這段期間，您可以選擇要指派的 ID 格式資源，並更新管理工具與指令碼以新增較長格式的支援。請瀏覽[這個](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resource-ids.html)文件取得指示。

**問：為何需要這樣做？**
為了能長期不間斷地建立新的資源，需要引入較長的 ID 格式。所有 Amazon EC2 資源 ID 將在 2018 年 7 月變更為較長的格式。

**問：這會對我造成什麼影響？**
若只使用主控台管理 AWS 資源，則可能完全不受影響，但仍應更新設定以盡快使用較長的 ID。
若是透過 API、SDK 或 AWS CLI 與 AWS 資源互動，則可能會受到影響，這視您的軟體是否會在驗證或保留資源 ID 時對 ID 格式做出假設而定。如果是這種情況，您可能需要更新系統才能處理新格式。

