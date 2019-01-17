#Mission7-FlaskServer入門2-QueryString
'''
流程
1. 安裝flask套件(若已安裝可省略)
2. 引用flask套件
3. 增加flask這個app的啟動點
4. 給一個可被訪問的路徑/
5. 針對get的反應

    flask get結合query string
    使用時，查詢http://192.168.114.10:5000?hello=iii
    """
6. 啟用Flask Server
'''
#實作
#install flask
!pip install flask

#引用套件
from flask import Flask, request, abort, jsonify
'''
jsonify不仅会将内容转换为json，而且也会修改Content-Type为application/json。
使用者端會提出一個請求稱為request, 在flask處理這些資訊的就是request，這是flask的自帶函數
Flask 自带了很顺手的 abort() 函数用于以一个 HTTP 失败代码中断一个请求，他也会提供一个非常简单的错误页面，用于提供一些基础的描述。
'''

#增加flask這個app的啟動點
app = Flask(__name__,static_url_path = "/images" , static_folder = "./images/" )
#給一個可被訪問的路徑/
@app.route('/',methods=['GET'])

def hello_world():
#取用用戶的querystring
#192.168.50.195:5000?id=123
#遇到get使用id存取時的值=t
    t = request.args.get('id')
    #轉成Dict
    jsonDict = {'id':t}
    #轉成json並回傳在網頁上
    return jsonify(jsonDict)
#啟用伺服器
if __name__ == "__main__":
    app.run(host='0.0.0.0')