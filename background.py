from flask import Flask
from threading import Thread

app = Flask("Simpbot")

@app.route("/")
def home():
    return 'simp'


def run():
  app.run(host='0.0.0.0',port=8080)


def keepAlive():
    t = Thread(target=run)
    t.start()