from flask import Flask
from flask import render_template
import requests
import json
app = Flask(__name__)


@app.route('/')
def index():
    request = requests.get(
        'https://www.googleapis.com/books/v1/volumes?q=Hobbit'
    )
    return render_template('books.html', books=json.loads(request.text)['items'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
