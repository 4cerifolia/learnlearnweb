from flask import Flask, render_template


app = Flask(__name__)

@app.route('/phone/list')
def phone_list():
    return render_template('phone_list.html')


if __name__=='__main__':
    app.run()


