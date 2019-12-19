from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/hi')
def hi():
    name = "김태완"
    return render_template('hi.html', html_name = name)

@app.route('/greeting/<string:name>')
def greeting(name):
    def_name = name
    return render_template("greeting.html", html_name = def_name)

@app.route('/cube/<int:num>')
def cube(num):
    return render_template("cube.html", html_name = num**3)

@app.route('/dinner')
def dinner():
    menu = ['스테이크', '마라탕', '초밥', '라멘', '그리들']
    dinnerMenu = random.choice(menu)
    menu_img = { 
        '스테이크' : 'https://tse3.mm.bing.net/th?id=OIP.wUCbaBDt3XDt7aH7AS4QZgHaE8&pid=Api&P=0&w=230&h=154',
        '마라탕' : 'http://newsteacher.chosun.com/site/data/img_dir/2019/05/28/2019052800090_0.jpg',
        '초밥' : 'http://postfiles10.naver.net/MjAxODAyMDhfMjEg/MDAxNTE4MDU2NTgxNTI5.3lrCqtydNBicoCyk5EZLel1DtQ0jpoZS-o-9NCYxbLcg.oXCEs8-DmjWzkEBJWIpvKGejJC2Dpm-Poj5fw-VqcsAg.JPEG.cafefrance/IMG_2568.jpg?type=w966',
        '라멘' : 'http://news.pulmuone.kr/webfile/webedit/20180312/20180312110147_%EC%9D%BC%EB%B3%B8%EB%8F%88%EC%BD%94%EC%B8%A0.jpg',
        '그리들' : 'http://thumbnail.egloos.net/600x0/http://pds25.egloos.com/pds/201704/12/89/c0222089_58ed916fd7906.jpg'
        }
    return render_template("dinner.html", dinnerMenu = dinnerMenu, dinner_img = menu_img[dinnerMenu])

@app.route('/movies')
def movies():
    movies = ['조커', '겨울왕국2', '터미네이터', '어벤져스']
    return render_template('movies.html', movies = movies)

if __name__ == "__main__":
    app.run(debug = True)