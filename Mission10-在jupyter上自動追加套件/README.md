# Mission10 - 在jupyter上自動追加套件

https://github.com/Jhe-Wei-Hsu/Missions/tree/Mission10

## 描述

jupyter 開啟時，已經自動安裝PyMySQL套件

開啟一個rds-example.ipynb，並嘗試使用PyMySQL套件連結至mysql進行 創建資料庫，資料表，插入資料，查詢資料

並將檔案上傳至github


## 相關技術

docker 

docker-compose

github

python

參考文件
創建連結https://hk.saowen.com/a/1c2fa8c1eaf78defd154bfd50fd74a3688fa8fa1ca14af497ad99afd54693688


http://www.codedata.com.tw/database/mysql-tutorial-9-table-index/


創建表單

----------
# 流程
1. 建立docker-compose環境
2. 撰寫 docker-compose.yml 描述檔
3. 檢查 docker-compose.yml 描述檔   `**docker-compose  config**`
4. 執行 docker-compose    `docker-compose up -d`
----------
# 實作
## 1.建立mission10資料夾
    git branch Mission10 ; git checkout Mission10 ; mkdir Mission10 ; cd Mission10/


## 2.建立docker-compose環境

建立docker-compose.yml 、dockerfile、work 資料夾、mysql/data以供 container 使用。

    mkdir work;mkdir -p mysql/data;vim dockefile
    --------dockerfile---------
    FROM jupyter/base-notebook
    RUN pip install PyMySQL
    --------dockerfile----------
    
    --------docker-compose.yml---------
    version: '3'
    services:
      jupyter:
        build: 
          context: .
          dockerfile: Dockerfile
        container_name: jupyter_test_compoese
        user: root
        environment:
          - GRANT_SUDO=yes
        ports:
          - "8888:8888"
        command: start-notebook.sh --NotebookApp.token=''
        volumes:
          - ./work:/home/jovyan/work/
      
      mariaDB:
        image: mariadb
        container_name: cc104.rds.local
        restart: always
        environment:
          MYSQL_ROOT_PASSWORD: cc10403
        ports:
          - "3306:3306"
        volumes:
          - ./mysql/data:/var/lib/mysql
    -----------docker-compose.yml-----------


## 3.執行docker-compose  以及查看container狀況
    #執行docker-compose 在背景
    docker-compose up -d
    #查看container狀況
    docker-compose ps
![](https://d2mxuefqeaa7sj.cloudfront.net/s_C939571687622E9E18A4E9A8254D99EDFECCDD4A6A74A9B5D8E368EF72262A19_1548145842575_image.png)

## 4.使用jupyter-notebook，rds-example.py，並嘗試使用PyMySQL套件連結至mysql進行 創建資料庫，資料表，插入資料，查詢資料

**4-1. 確認PyMysql已正確安裝**

![](https://d2mxuefqeaa7sj.cloudfront.net/s_C939571687622E9E18A4E9A8254D99EDFECCDD4A6A74A9B5D8E368EF72262A19_1548145989306_image.png)


4-2. 確認cc104.rds.local container 運行狀況並進入查詢(以root登入，密碼cc10403)

    #進入container
    docker container exec -it cc104.rds.local /bin/bash
    #登入進入 mysql
    mysql -u root -p
    密碼 ： cc10403
    
    #查詢現有的資料庫
    mysql> show databases;
![](https://d2mxuefqeaa7sj.cloudfront.net/s_C939571687622E9E18A4E9A8254D99EDFECCDD4A6A74A9B5D8E368EF72262A19_1548146253999_image.png)

    #選用mysql資料庫
    mysql> use mysql
![](https://d2mxuefqeaa7sj.cloudfront.net/s_C939571687622E9E18A4E9A8254D99EDFECCDD4A6A74A9B5D8E368EF72262A19_1548146283216_image.png)


**4-3.python****資料庫****應用**
創建資料庫，資料表，插入資料，查詢資料

    #導入pymysql套件
    import pymysql
    # 連接database
    #host可以是container name或其ip，意思相同
    conn = pymysql.connect(host="cc104.rds.local", user="root",password="cc10403",database="mysql",charset="utf8")
    # 得到一個可以執行SQL語句的光標對象
    cursor = conn.cursor()
    # 定義要執行的SQL語句
    #創建TABLE 名為USER
    #TABLE內容有id欄(自行產生)，name欄(長度限制為10字元，不可空),
    #age欄(从 0 到 255 的整型数据。存储大小为 1 字节，不可空<人應該不會超過255歲吧 ?)。
    sql = """
    CREATE TABLE USER (
    id INT auto_increment PRIMARY KEY ,
    name CHAR(10) NOT NULL UNIQUE,
    age TINYINT NOT NULL
    )ENGINE=innodb DEFAULT CHARSET=utf8;
    """
    #ENGINE=innodb DEFAULT CHARSET=utf8
    #查詢mysql支援的儲存引擎用 InnoDB 其支援transactions 
    # 執行SQL語句
    cursor.execute(sql)
    # 關閉對象
    cursor.close()
    # 關閉資料庫連接
    conn.close()

插入資料

    #插入資料
    # 引入pymysql套件
    import pymysql
    # 連接database
    conn = pymysql.connect(host="cc104.rds.local", user="root",password="cc10403",database="mysql",charset="utf8")
    # 得到一個可以執行SQL語句的對象
    cursor = conn.cursor()
    sql = "INSERT INTO USER(name, age) VALUES (%s, %s);"
    name = "Wei-Hsu"
    age = 29
    # 執行SQL語句
    cursor.execute(sql, [name, age])
    # 提交事務
    conn.commit()


![](https://d2mxuefqeaa7sj.cloudfront.net/s_C939571687622E9E18A4E9A8254D99EDFECCDD4A6A74A9B5D8E368EF72262A19_1548147373856_image.png)


查詢資料

    #查詢資料
    # 引入pymysql套件
    import pymysql
    # 連接database
    conn = pymysql.connect(host="cc104.rds.local", user="root",password="cc10403",database="mysql",charset="utf8")
    # 得到一個可以執行SQL語句的對象
    cur = conn.cursor()
    #1.查詢操作  
    # 編寫sql 查詢語句  user 對應我的TABLE名  
    sql = "SELECT * FROM USER"
    try:  
        cur.execute(sql)    #執行sql語句  
      
        results = cur.fetchall()    #獲取查詢的所有記錄  
        print("id","name","age")  
        #遍歷結果  
        for row in results :  
            id = row[0]  
            name = row[1]  
            age = row[2]  
            print(id,name,age)  
    except Exception as e:  
        raise e  
    finally:  
        conn.close()  #關閉連接 
![](https://d2mxuefqeaa7sj.cloudfront.net/s_C939571687622E9E18A4E9A8254D99EDFECCDD4A6A74A9B5D8E368EF72262A19_1548147505730_image.png)

## 5.Github
https://github.com/Jhe-Wei-Hsu/Missions/tree/master/Mission10-%E5%9C%A8jupyter%E4%B8%8A%E8%87%AA%E5%8B%95%E8%BF%BD%E5%8A%A0%E5%A5%97%E4%BB%B6

----------
# 備註：相關資料來源
## 1.mariadb預設資料庫位址

根據https://hub.docker.com/_/mariadb 提供：
/var/lib/mysql

![](https://d2mxuefqeaa7sj.cloudfront.net/s_C939571687622E9E18A4E9A8254D99EDFECCDD4A6A74A9B5D8E368EF72262A19_1547720146467_image.png)


@Li B 雖然我對coding沒興趣，但我也在努力
