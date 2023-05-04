from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello to world of flask "

if __name__ == "__main__":
    app.run()