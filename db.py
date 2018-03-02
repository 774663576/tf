# jdbc:mysql://127.0.0.1:3306/biyanzhi

import pymysql
db = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='koolearn',
    charset='utf8'
)
cursor = db.cursor()

def queryInfo(user_id):
    sql = "select * from user WHERE  user_number='%s'"
    data = (user_id)
    cursor.execute(sql % data)
    result = cursor.fetchone()
    return result[1]

#   # 关闭数据库连接
# db.close()