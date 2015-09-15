import os
from flask import Flask
import redis

app = Flask(__name__)
r = redis.StrictRedis(host='db', port=6379, db=0)

@app.route("/")
def consume():
    num = r.get('num')
    if num == None:
        num = 0
    else:
        num = int(num)
        num -= 1

    r.set('num', str(num))
    return str(num)

if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
