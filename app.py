import lib.sample as sample
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    f = open("./pages/index.html", "r")
    return "<h1>According to NHTSA, a 2011 BMW X3 has a {} cylinder engine.</h1>\n".format(sample.x3()),f.read()