#Mission5-基礎資料處理
#1. 引用套件+2.使用request模組
import requests
RESPONSE = requests.get('https://jsonplaceholder.typicode.com/users')

#3. 使用get方法取得2,3,4,5筆資料
TRYGET = RESPONSE.json()
TRYGET2=TRYGET[2:5]

# 4.載入DATETIME套件並將UTC時間變為變數
import datetime
nowUtcUnixTime = datetime.datetime.utcnow().timestamp()
UTCTIME=int(nowUtcUnixTime)
UTCSTR=str(UTCTIME)


#5.創造檔案，刪除檔案與資料夾，創建資料夾，寫入資料，關閉檔案

import os
import shutil

if os.path.exists('TESTDIR') :
    # 刪除資料夾與檔案
    shutil.rmtree('./TESTDIR')
    # 創造資料夾
else:
    # 創造資料夾
    os.mkdir('TESTDIR')
    # 開起一個檔案
    openStep2File = open('TESTDIR/'+UTCSTR+'.txt','w')
    # 將資料寫入檔案
    openStep2File.write(str(TRYGET2))
    # 將檔案關閉
    openStep2File.close()

print('完成了,請至根目錄下檢查')