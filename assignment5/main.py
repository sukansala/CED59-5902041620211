from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def index():  # โมดูลรับค่าจากไฟล์ index.html โดยการส่งค่าในรูปแบบ POST
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
