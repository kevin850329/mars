from flask import Flask, request, redirect

import logic

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


uri = 'https://s.megawingame.com/'


@app.route('/add/', methods=['POST'])
def add_full_url():
    if request.method == 'POST':
        tmp_full_url = request.json.get('url')
        short_url = logic.add_full_url(tmp_full_url)
        return uri + 'g/' + short_url
    elif request.method == 'GET':
        return ''


@app.route('/add_with_name/', methods=['POST'])
def add_full_url_with_name():
    if request.method == 'POST':
        tmp_full_url = request.json.get('url')
        name = request.json.get('name')
        short_url = logic.add_full_url_with_name(tmp_full_url, name)
        if short_url == 'DuplicateName':
            return 'DuplicateName'
        return uri + 'g/' + short_url
    elif request.method == 'GET':
        return ''


@app.route('/g/<short_url>')
def redirect_to_full_url(short_url: str):
    full_url = logic.get_full_url(short_url)
    if full_url:
        return redirect(full_url)
    return ''


@app.route('/gs/<full_url>', methods=['GET', 'POST', 'DELETE'])
def get_short_url(full_url: str):
    if request.method == 'POST':
        tmp_full_url = request.json.get('url')
        short_url = logic.get_short_url(tmp_full_url)
        return uri + 'g/' + short_url
    else:
        return ''


if __name__ == '__main__':
    app.run()
