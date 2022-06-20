from flask import Flask
from housing.logger import logging

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    logging.info("we are testing logger")
    return "this is machine learning project 2"

if __name__=="__main__":
    app.run(debug=True)
