
import requests
import json
from flask import Flask
app = Flask(__name__)
token = "EAACNyZBYZAhLMBAIoElPrpGXbfZAMqVjgrxE3ML1WR9rZCCUeKfZB07PkptglfoVq8LGbqXueLenjW1PxHZC67mGZCrdHVH94ZCJZCtlFZAGMleOwC8r4ezjn7nKpkEXdhoWZBAd2DAaKbZABRZCPmwc7JqNYXlbFv6KddtfTIW81tmOzZCwZDZD"

@app.route('/')
def index():
    return "Hi"
    
@app.route('/webhook', methods=['GET'])
def webhook():
    if request.method == 'GET' :
        if request.args.get('hub.verify_token') == 'EAACNyZBYZAhLMBAIoElPrpGXbfZAMqVjgrxE3ML1WR9rZCCUeKfZB07PkptglfoVq8LGbqXueLenjW1PxHZC67mGZCrdHVH94ZCJZCtlFZAGMleOwC8r4ezjn7nKpkEXdhoWZBAd2DAaKbZABRZCPmwc7JqNYXlbFv6KddtfTIW81tmOzZCwZDZD' :
            return request.args.get('hub.challenge')
        return "Wrong Verify Token"
    return 'Hello World!'

if __name__ == '__main__' :
    app.debug = True
    app.run(host='0.0.0.0')





