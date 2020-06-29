from flask import Flask,request,render_template

app = Flask(__name__)



@app.route('/receiveObstacles',methods=["POST"])
def index():
    if request.method == "POST':
        return "kakkar bsdka"


if __name__ = '__main__':
   app.run()

