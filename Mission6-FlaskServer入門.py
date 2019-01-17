
#install flask
!pip install flask

#引用套件
from flask import Flask, request, abort, jsonify
'''jsonify不仅会将内容转换为json，而且也会修改Content-Type为application/json。
使用者端會提出一個請求稱為request, 在flask處理這些資訊的就是request，這是flask的自帶函數
Flask 自带了很顺手的 abort() 函数用于以一个 HTTP 失败代码中断一个请求，他也会提供一个非常简单的错误页面，用于提供一些基础的描述。
'''    
#增加flask這個app的啟動點
app = Flask(__name__,static_url_path = "/images" , static_folder = "./images/" )
#給一個可被訪問的路徑/
@app.route('/',methods=['GET'])
#要show出來的內容--以json格式
def hello_world():
  t = {'a':1,'b':'Chicken leg'}
  return jsonify(t)
#啟動程式
if __name__ == "__main__":
  app.run(host='0.0.0.0')