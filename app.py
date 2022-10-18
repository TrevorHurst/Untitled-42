from flask import Flask
from flask import request
from flask import redirect
from flask import render_template

messages = []

app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def hello_world():
    global messages
    if request.method == "POST":
        ip = request.remote_addr
        messages.insert(0, f"{ip}> {request.form['message']}")
        messages = messages[:10]
        return redirect('/')
    else:
        return render_template('main.html',messagey = messages[::-1])


if __name__ == "__main__":
    import os
    os.system("sh run.sh")