from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    name = request.args.get('keyword')
    return render_template('pong.html', data = name)

@app.route('/youtube')
def youtube():
    return render_template('youtube.html')

if __name__ == "__main__":
    app.run(debug=True)