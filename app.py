#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
    return 'How are you?'

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    app.run(debug=True)
