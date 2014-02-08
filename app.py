from flask import Flask
from flask import render_template, url_for, redirect,request
import api
app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def index():
    if request.method=="GET":
        return render_template("main.html",answer=False)

    if request.method=="POST":
        if request.form['emotion']=="emotion":
            emotion=request.form['emotionvalue']
            dic=api.getSenAuth(emotion)
            name=dic['author']
            origin=dic['origin']
            sentence=dic['sentence']
            return render_template("main.html",answer=True,name=name,origin=origin,sentence=sentence)

if __name__=="__main__":
    app.debug=True
    app.run(port=8888)
