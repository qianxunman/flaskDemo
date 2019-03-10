from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world, this is runing in port 5000!</br><h1>不用看了，你就是一个大傻子！哈哈哈哈</h1>'

if __name__ == '__main__':
    app.run(debug=True)
