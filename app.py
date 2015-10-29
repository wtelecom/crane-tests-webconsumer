import os
from flask import Flask, jsonify, render_template
import redis

app = Flask(__name__, template_folder='templates')
r = redis.StrictRedis(host='db', port=6379, db=0)

@app.route("/")
def consume():
    data = r.get('data')
    info = None
    if not data:
        data = ''
    if data is 'allo':
        info = render_template('./hello0.html')
    elif data is 'estoestodo':
        info = render_template('./hello.html')
    elif data is 'test':
        info = render_template('./hello2.html')
    elif data is 'test2':
        info = render_template('./hello1.html')

    result = {'data':data, 'action':'get'}
    if info:
        return info
    return jsonify(result)

if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
