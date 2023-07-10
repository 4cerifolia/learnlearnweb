from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/phone/list')
def phone_list():
    return render_template('phone_list.html')
# http://127.0.0.1:5000/add/phone?youname=%E9%9F%A9%E6%99%A8%E9%A3%9E&phonenumber=18768116241
@app.route('/add/phone')
def add_phone():


username = request.args.get('youname')
usernumber = request.args.get('younumber')

return "xxx"


if __name__ == '__main__':
    app.run()
