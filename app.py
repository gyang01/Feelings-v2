from flask import Flask
from flask import render_template, url_for, redirect,request

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def index():
    if request.method=="GET":
        return render_template("main.html",answer=False)

    if request.method=="POST":
        if request.form['emotion']=="emotion":
            emotion=request.form['emotionvalue']
            return render_template("main.html",answer=True)

if __name__=="__main__":
    app.debug=True
    app.run(port=8888)
