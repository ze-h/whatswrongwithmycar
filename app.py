import lib.sample as sample
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'Click for details on the X3':
            return "According to NHTSA, a 2011 BMW X3 has a {} cylinder engine.".format(sample.x3())
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html', form=request.form)
    
    return render_template("index.html")