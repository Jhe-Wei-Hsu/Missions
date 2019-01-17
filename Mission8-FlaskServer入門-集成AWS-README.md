# Mission8 - FlaskServer入門 - 集成AWS


## 描述

撰寫一個Flask Server， 設計一個端口為user，用戶能對此端口用POST方法訪問，挾帶任意json body。 將此body轉存成檔案，存在伺服器上，並將此檔案上傳至 iii-tutorial-v2桶內的student{座號}資料夾下。

s3實作流程
**1.創建bucket**
**2.瀏覽bucket**
**3.上傳物件至s3**
**4.下載物件from s3**
**5.刪除物件in s3**

## 實作範例
    #安裝boto3及awscli
    !pip install boto3 awscli
    
    
    #需先給jupyter notebook aws cli的認證權限
    #用jupyter notebook開專屬的cmd
    jovyan@b2cc00a4f7ba:~$ aws configure
    AWS Access Key ID [None]: 秘
    AWS Secret Access Key [None]:秘 
    Default region name [None]: ap-northeast-1
    Default output format [None]: tesxt
## 
    #注意時間問題，可用ntpdate指令處理
    #時間差過大會報錯
    """
    瀏覽有哪一些桶子
    
    """
    
    import boto3
    from pprint import pprint
    
    client = boto3.client(
        's3'
    )
    
    pprint(client.list_buckets())
## 
## 
## 註：boto3是Client-Server架構，在python使用套件功能都是client，遠端(s3)為Server端
## 
## 
    """
    瀏覽桶子內的物件
    
    """
    #引用套件
    import boto3
    from pprint import pprint
    #啟用客戶端
    client = boto3.client(
        's3'
    )
    #瀏覽桶子
    pprint(client.list_objects_v2(Bucket='iii-tutorial-v2'))
## 
## 
## 
    """
    
    上傳物件至桶子中
    
    """
    
    import boto3
    from pprint import pprint
    
    s3resource = boto3.resource('s3')
    uploadObject = s3resource.Object('iii-tutorial-v2', 'student4/step1-s3-demo.txt').put(Body=open('./step1-s3-demo.txt', 'rb'))
    pprint(uploadObject)

