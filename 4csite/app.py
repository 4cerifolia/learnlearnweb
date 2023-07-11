import pymysql
from pymysql.cursors import DictCursor
from flask import Flask, render_template, request,redirect


app = Flask(__name__)

# 新建、删除、更新使用，不能用于查询
def db_execute(sql,arg_list):
    # 连接数据库
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='x910823y',charset='utf8mb4',db='addressbook')
    cursor = conn.cursor(cursor=DictCursor)

    # 根据sql语句查询数据库中的数据 修改、新增、删除 --》    conn.commit()
    cursor.execute(sql,arg_list)
    conn.commit()

    # 关闭连接
    cursor.close()
    conn.close()


    


@app.route('/phone/list')
def phone_list():
    # 连接数据库
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='x910823y',charset='utf8mb4',db='addressbook')
    cursor = conn.cursor(cursor=DictCursor)

    # 根据sql语句查询数据库中的数据
    cursor.execute('select id,name,tel,short_tel,mobile,email,depart_id from employeelist order by id desc')
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
    inputMobile = request.args.get('mobilenumber')
    inputTel = request.args.get('telnumber')
    inputShorttel= request.args.get('shorttel')
    inputEmail= request.args.get('email')
    inputdepartid= request.args.get('departid')
    # 保存到数据库
    # 连接数据库
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='x910823y',charset='utf8mb4',db='addressbook')
    cursor = conn.cursor(cursor=DictCursor)

    # 根据sql语句查询数据库中的数据 修改、新增、删除 --》    conn.commit()
    cursor.execute('insert into employeelist(name,tel,short_tel,mobile,email,depart_id)values(%s,%s,%s,%s,%s,%s)',[inputName,inputTel,inputShorttel,inputMobile,inputEmail,inputdepartid])
    conn.commit()

    # 关闭连接
    cursor.close()
    conn.close()


    #成功后重定向至phone_list.html
    return redirect('/phone/list')

# 删除一条信息
@app.route('/del/phone')
def del_phone():
    delKey = request.args.get('del_key')
    #根据key值删除数据库中内容
    #delete from *table name* where id=1

    # 连接数据库
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='x910823y',charset='utf8mb4',db='addressbook')
    cursor = conn.cursor(cursor=DictCursor)

    # 根据sql语句查询数据库中的数据 修改、新增、删除 --》    conn.commit()
    cursor.execute('delete from employeelist where id=%s',[delKey,])
    conn.commit()

    # 关闭连接
    cursor.close()
    conn.close()

    #成功后重定向至phone_list.html
    return redirect('/phone/list')


if __name__ == '__main__':
    app.run()
