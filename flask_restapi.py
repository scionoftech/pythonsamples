from flask import Flask
from flask import json
from flask import request

app = Flask(__name__)


@app.route('/test_post', methods=['POST'])
def post_api():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"


# /test_get?language=Python
@app.route('/test_get', methods=['GET'])
def get_api():
    return "Get is " + request.args.get('language')


@app.route("/")
def index():
    return "hello world man"


if __name__ == "__main__":
    app.run()
    # app.run(debug=False, host="0.0.0.0", port=3001)
