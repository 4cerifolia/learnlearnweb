from flask import Flask, render_template


app = Flask(__name__)

@app.route('/phone/list')
def phone_list():
    return render_template('phone_list.html')

@app.route('/')
def homepage():
    return render_template('homepage')


if __name__=='__main__':
    app.run()


