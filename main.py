from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return (
        "<h1>Hello, World!</h1>"
        "<p>"
        '<a href="/howdy">If that isnt effusive enough, click here</a>'
        "<br>"
        '<a href="/basic_input">Enter your input</a>'
        "</p>"
    )

    # Enter input does nothing, just links to "basic input" route/page


@app.route("/howdy")
def howdy():
    return "<h1>Howdy!</h1>"


@app.route("/basic_input")
def basic_input():
    return (
        '<form action="/output" method="post">'
        '<input type="text" name="input">'
        '<input type="submit" value="Submit"></form>'
    )


# action="/output" - where form data sent
# method="post", how form data sent

# on submit, 'input: {text}' is passed to request.form on the server as: <class 'werkzeug.datastructures.ImmutableMultiDict'>


@app.route("/output", methods=["POST"])
def output():
    user_input = request.form["input"]
    return f"You entered: {user_input}"


# if methods not specified ['GET'] is the default
# HTTP terminology client-server request methods (GET, POST, etc.) perspective of the client
# hence POST because the client is "posting" information to the server


app.run()
