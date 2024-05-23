from flask import Flask
from src.logger import logging

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    logging.info("We are testing second method of logging")
    return "Welocome to Vardhan Hegde's ML pipeline Project session"

if __name__ == "__main__":
    app.run(debug = True)
