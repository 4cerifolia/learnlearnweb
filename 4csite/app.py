import pymysql
from pymysql.cursors import DictCursor
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/phone/list')
def phone_list():
    # 连接数据库
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='x910823y',charset='utf8mb4',db='addressbook')
    cursor = conn.cursor(cursor=DictCursor)

    # 根据sql语句查询数据库中的数据
    cursor.execute('select id,name,tel,short_tel,mobile,email,depart_id from info order by id desc')
    data_list = cursor.fetchall()

    # 关闭连接
    cursor.close()
    conn.close()

    return render_template('phone_list.html',data_list=data_list)




# http://127.0.0.1:5000/add/phone?youname=%E9%9F%A9%E6%99%A8%E9%A3%9E&phonenumber=18768116241
@app.route('/add/phone')
def add_phone():
    # 获取了用户在页面上的数据
    inputName = request.args.get('youname')
    inputNumber=request.args.get('younumber')
    print(inputName,inputNumber)
    return("success!")
    # 保存到数据库
    # 连接数据库
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='x910823y',charset='utf8mb4',db='addressbook')
    cursor = conn.cursor(cursor=DictCursor)

    # 根据sql语句查询数据库中的数据
    cursor.execute('insert into employeelist ')
    data_list = cursor.fetchall()

    # 关闭连接
    cursor.close()
    conn.close()
if __name__ == '__main__':
    app.run()
