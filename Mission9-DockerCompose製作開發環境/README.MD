# Mission9 - DockerCompose製作開發環境

## 描述

使用DockerCompose，製作一個具有jupyter 與 mariaDB 兩個Container的環境，
並指定 jupyter的源碼資料夾保存位置 與 mariaDB的資料保存位置 回本地端

jupyter環境需奠基在dockerfile之上

使用gitignore技術，將mariaDB的資料忽略

其餘的上傳至github 


# 流程
1. 建立docker-compose環境
2. 撰寫 docker-compose.yml 描述檔
3. 檢查 docker-compose.yml 描述檔   `**docker-compose  config**`
4. 執行 docker-compose    `docker-compose up -d`



    #建立docker-compose環境
    mkdir -p ~/AWS/Missions/Mission9/ ; cd ~/AWS/Missions/Mission9/ ; mkdir work/ ;mkdir -p ./mariadb/data ; vim  docker-compose.yml
    
    #撰寫docker-compose.yml
    ---docker-compose.yml內容---
    version: '3.1'
    services:
    
      jupyter-notebook:
        image: jupyter/base-notebook
        container_name: jupyter.local
        ports:
          - "8888:8888"
        volumes:
          - ./work:/home/jovyan/work/
        command: start-notebook.sh --NotebookApp.token=''
    #jupyter/datascience-notebook 為image name，重要的是後面的start-notebook.sh — NotebookApp.token=’’，這邊複寫了原有的command，用意是設定不需要帳密就可登入jupyter，此設定在https://goo.gl/kVyiV4 有其他用法。
    
      db:
        image: mariadb
        restart: always
        container_name: mariadb
        volumes:
          - ./mariadb/data:/data/db/
        ports:
          - "9487:9487"
        environment:
          MYSQL_ROOT_PASSWORD: example
    
      adminer:
        image: adminer
        restart: always
        ports:
          - 8080:8080
    ----↑docker file內容---
    
    ------
    #檢查docker-compose.yml
    cd ~/AWS/Missions/Mission9 ; docker-compose  config
    
    -----------
    #.gitignore內容
    mariadb/data

試用體驗
`docker-compose up -d`

![](https://d2mxuefqeaa7sj.cloudfront.net/s_DDD3AC9AD6E7FFAB6113DC7C7E83B7C0866058261FCE885019686148348745CD_1546691432042_image.png)
![](https://d2mxuefqeaa7sj.cloudfront.net/s_DDD3AC9AD6E7FFAB6113DC7C7E83B7C0866058261FCE885019686148348745CD_1546691454376_image.png)

    #關閉測試環境
    docker-compose down    

上傳Github

    git add -A                                       
    git commit -m "Mission9" 
    git push
https://github.com/Jhe-Wei-Hsu/Missions/tree/master/Mission9


@Li B 
