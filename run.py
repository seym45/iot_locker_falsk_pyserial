from flask import Flask, render_template,request
import serial
import time
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


import test
@app.route("/query")
def query():
    arg = request.args.get('q', default='None', type=str)
    arg = '?' if arg == 'query' else arg
    ret = test.get_value(arg)
    try:
        ret = ret.decode()
    except:
        pass
    print('debug: ' + str(ret))
    return ret

if __name__ == '__main__':
    app.run(debug=True)
