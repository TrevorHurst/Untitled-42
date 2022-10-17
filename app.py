from flask import Flask
from flask import request
from flask import render_template

messages = []

app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def hello_world():
    if request.method == "POST":
        messages.append(request.form['message'])
        return render_template('main.html',messagey = messages)
    else:
        return render_template('main.html',messagey = messages)


if __name__ == "__main__":
    import os
    os.system("sh run.sh")