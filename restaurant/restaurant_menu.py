from flask import Flask, render_template, request, redirect
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
    items = cursor.execute('SELECT id, name FROM restaurant').fetchall()
    db.close()

    return render_template('restaurants.html', restaurants=items)

    # 스파게티 코드
    # mydoc="<h1>All Restaurants</h1>"
    # mydoc += "<ul>"
    # for item in items:
    #     mydoc += f"<li>{item[0]}</li>"
    # mydoc +="</ul>"
    # return mydoc

# string으로 하면 레스토랑 이름으로도 인식됨
@app.route('/restaurant/<int:restaurant_id>/')
def showMenu(restaurant_id):
    return f"All menu items for restaurant {restaurant_id}"

# methods default는 GET만 받기 때문에 따로 설정해야함
@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        db = sqlite3.connect('./restaurant/restaurant_menu.db')
        cursor = db.cursor()
        cursor.execute('INSERT INTO restaurant (name) VALUES (?)', (request.form['name'],))
        db.commit()
        db.close()

        # 추가 페이지말고 목록 페이지로 이동
        return redirect('/restaurants/')
    return render_template('restaurants_new.html')

@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return f"This page will be for deleting a {restaurant_id} restaurants"

def hello(name = None):
    return render_template('home.html', name = name)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
