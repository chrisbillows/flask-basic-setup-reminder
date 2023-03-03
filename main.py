from flask import Flask

app = Flask('bob')

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1><p><a href="/howdy">If that isnt effusive enough, click here</a></p>'

@app.route('/howdy')
def howdy():
    return '<h1>Howdy!</h1>'

app.run()

