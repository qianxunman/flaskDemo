from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world, this is runing in port 5001!'

if __name__ == '__main__':
    app.run(debug=True)