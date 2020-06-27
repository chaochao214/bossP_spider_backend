# @Author  : Czq
# @Time    : 2019/3/17 10:32
# @File    : build_database.py

from sshtunnel import SSHTunnelForwarder
import pymysql


# 通过SSH连接云服务器
# server = SSHTunnelForwarder(
#     ssh_address_or_host=("47.105.86.106", port),  # 云服务器地址IP和端口port
#     ssh_username=admin,  # 云服务器登录账号admin
#     ssh_password=password,  # 云服务器登录密码password
#     remote_bind_address=('localhost', 33306)  # 数据库服务地址ip,一般为localhost和端口port，一般为3306
# )

# 云服务器开启
# server.start()


# 云服务器上mysql数据库连接
def connect_db():
    """
    :return: 自动连接数据库
    """
    host = 'localhost'
    # host = '47.105.86.106'
    # port = 33306
    user = 'root'
    password = 'root'
    # password = '123456'
    db = 'bossP'
    # db = pymysql.connect(host, user, password, db)
    db = pymysql.connect("47.105.86.106", "root", "123456", "bossP", port=33306, charset='utf8')
    return db


def build_table():
    """
    :return:查看数据库中是否存在三个表，若没有则新建表
    """
    db = connect_db()
    cursor = db.cursor()
    for table in ['lagou', 'zhilian', 'zhipin']:
        if table == 'zhipin':
            sql = """CREATE TABLE if not exists %s (
                     id int(11) AUTO_INCREMENT,
                     company  VARCHAR(128) NOT NULL,
                     job  VARCHAR(128),
                     city VARCHAR(128),  
                     salary VARCHAR(128),
                     url VARCHAR(255),
                     PRIMARY KEY (`id`))""" % table

            cursor.execute(sql)
        else:
            sql = """create table if not exists %s (
                     id int(11) AUTO_INCREMENT,
                     company VARCHAR(128) NOT NULL,
                     job VARCHAR(128),
                     city VARCHAR(128),
                     site VARCHAR(128),
                     salary VARCHAR(128),
                     url VARCHAR(255),
                     PRIMARY KEY (`id`))""" % table

            cursor.execute(sql)

    db.close()


if __name__ == '__main__':
    build_table()
