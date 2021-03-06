 # -*- coding: utf-8 -*-
import os
from flask import Flask

app = Flask(__name__)

#app.config.from_object(os.environ['APP_SETTINGS'])
cfg = os.environ['APP_SETTINGS'].replace('"','')
print(cfg)
app.config.from_object(cfg)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return f"Hello {name}!"

if __name__ == '__main__':
    app.run()