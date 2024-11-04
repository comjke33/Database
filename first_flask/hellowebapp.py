from flask import Flask

# 원래는 웹서버가 실행해야함 -> 프로그램으로써 돌림
app = Flask(__name__) 

# 얘도 함수
# 2개 경로에 대한 request가 왔을 때 둘다 구동함
@app.route('/') # 127.0.0.1:5000
@app.route('/hello/') # 127.0.0.1:5000/hello
@app.route('/hello/<string:name>/')


def hello(name = None):
    mydoc=""
    mydoc+="<h1> Hello, world! </h1>"
    mydoc+="<h2> Welcome to my </h2>"

    if name:
        mydoc += f"<h1>Hello, {name} World!</h1>"
    else:
        mydoc += "<h1>Hello, World!</h1>"
    return mydoc

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
