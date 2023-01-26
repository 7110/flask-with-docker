from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'index'


@app.route('/services', methods=['GET'])
def get_services():
    services = [
        {
            'name': 'Yahoo',
            'url': 'https://www.yahoo.co.jp/'
        },
        {
            'name': 'Google',
            'url': 'https://www.google.com/'
        },
        {
            'name': 'Twitter',
            'url': 'https://twitter.com/'
        }
    ]

    return jsonify(services)


@app.route('/correspondence', methods=['POST'])
def post_correspondence():
    body = request.json
    body['addition_key'] = '8200'

    return body
