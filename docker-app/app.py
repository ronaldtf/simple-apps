from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!\n"

@app.route('/version')
def version():
    return "Hello World 1.0\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

