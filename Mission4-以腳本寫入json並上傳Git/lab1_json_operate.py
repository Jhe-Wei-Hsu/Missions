
# coding: utf-8

# In[2]:


'''創建一個檔案，裡面塞入一個json object， object裡面需要有四個欄位，分別對應到 string, number, object, array。
讀取該檔案做操作，將四個欄位進行內容修改，存回原檔案
流程:
1.建立檔案jsontest.txt
2.讀取檔案
3.寫入檔案
4.存檔
5.關閉檔案

'''
#調用操作系統命令，來建立文件，刪除文件，查詢文件
import os
#調用json函數
import json
#讀取檔案
open1=open('jsontest.txt','w')
#寫入檔案，先寫一個json object， object裡面需要有四個欄位，分別對應到 string, number, object, array。
jsondata={
    'jsonString': 'haha binghon is good',
    'jsonNumber': 9487,
    'jsonObject': {'iii': "verygood", 'cc104': '03'},
    'jsonArray': ['a',5,4, 'd'] 
        }
open1.write(json.dumps(jsondata))
open1.close()

