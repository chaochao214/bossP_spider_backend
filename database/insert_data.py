# @Author  : Czq
# @Time    : 2019/3/17 14:45
# @File    : insert_data.py

from database.build_database import build_table, connect_db
from crawl.lagou.lagou import lagou_main
from crawl.zhilian.zhilian import zhilian_main


# from crawl.zhipin.zhipin import zhipin_main


def data_extract(kw, city):
    '''
    :return: 爬取数据并将数据处理成可以批量导入数据库的格式
    '''
    lagou_tuple = []

     # 定义一个python空列表
    # zhilian_tuple = []
    zhipin_tuple = []
    df_lagou = lagou_main(city, kw)
    for i in range(len(df_lagou)):
        lagou_tuple.append(tuple(df_lagou.iloc[i, :].values))

    # 智联招聘的数据
    # df_zhilian = zhilian_main(city, kw)
    # for i in range(len(df_zhilian)):
    #     zhilian_tuple.append(tuple(df_zhilian.iloc[i, :].values))

    # boss直聘的数据
    # df_zhipin = zhipin_main(city, kw)
    # for i in range(len(df_zhipin)):
    #     zhipin_tuple.append(tuple(df_zhipin.iloc[i, :].values))

    # data = [lagou_tuple, zhilian_tuple]
    # data = [lagou_tuple, zhilian_tuple, zhipin_tuple]


    data =[lagou_tuple]
    return data


def batch_insert(data):
    '''
    :return:将数据批量导入数据库
    '''
    db = connect_db()
    cursor = db.cursor()
    try:
        for i, x in enumerate(data):
            if i == 2:
                print("2")
                sql = 'insert into zhipin(company,job,city,salary,url) values (%s,%s,%s,%s,%s)'
                cursor.executemany(sql, x)
                db.commit()
            elif i == 1:
                print("1")
                sql = 'insert into zhilian(company,job,city,site,salary,url) values (%s,%s,%s,%s,%s,%s)'
                cursor.executemany(sql, x)
                db.commit()
            else:
                print("3")
                sql = 'insert into lagou(company,job,city,site,salary,url) values (%s,%s,%s,%s,%s,%s)'
                cursor.executemany(sql, x)
                db.commit()
        print('数据导入成功')
    except:
        db.rollback()
    db.close()


def sql_main(kw, city):
    # 创建数据库的表，这里省略
    # build_table()
    data = data_extract(kw, city)
    print(data)
    batch_insert(data)


if __name__ == '__main__':
    sql_main('java', '深圳')
