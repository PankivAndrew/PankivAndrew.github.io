from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/save_token', methods=['POST'])
def save_token():
    print(request.data)
    return 'OK!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5050')
