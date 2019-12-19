from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

if __name__ == "__main__":
    app.run(debug = True)