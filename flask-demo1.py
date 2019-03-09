from flask import Flask


app = Flask(__name__)

app.route('/')
def index():
    return 'hello,this is from the port of 5001'

if __name__ = '__main__':
    app.run()
