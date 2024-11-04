from flask import Flask, render_template
import sqlite3

# 원래는 웹서버가 실행해야함 -> 프로그램으로써 돌림
app = Flask(__name__) 

# 얘도 함수
# 2개 경로에 대한 request가 왔을 때 둘다 구동함
@app.route('/') # 127.0.0.1:5000
@app.route('/restaurants/') # 127.0.0.1:5000/hello
def showRestaurants():
    db = sqlite3.connect('./restaurant/restaurant_menu.db')
    cursor = db.cursor() # tuple 하나씩 가져오기 때문에
    items = cursor.execute('SELECT name FROM restaurant').fetchall()
    db.close()
    mydoc="<h1>All Restaurants</h1>"
    mydoc += "<ul>"
    for item in items:
        mydoc += f"<li>{item[0]}</li>"
    mydoc +="</ul>"
    return mydoc

@app.route('/restaurant/new/')
def newRestaurants():
    return "This page will be for making a new restaurants"

@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return f"This page will be for deleting a {restaurant_id} restaurants"

def hello(name = None):
    return render_template('home.html', name = name)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
