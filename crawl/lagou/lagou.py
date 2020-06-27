# @Author  : Czq
# @Time    : 2019/3/16 14:33
# @File    : lagou.py
import requests
import json
import pandas as pd
import time
import schedule


def get_params(city, kw, x):
    '''
    :return:网页参数，将传入的参数做成参数字典
    '''
    params = {
        'city': city,
        'kd': kw,
        'pn': str(x),
        'first': 'true'
    }
    return params


def get_cookie(url_start, headers):
    '''
    :param url_start: 可以获取cookie的初始页面
    :param headers: 网页头信息
    :return: cookie
    '''
    s = requests.Session()
    s.get(url_start, headers=headers, timeout=3)
    cookie = s.cookies
    return cookie


def get_text(url, headers, params, cookie):
    '''
    :return: 爬取的内容
    '''
    r = requests.post(url, headers=headers, params=params, cookies=cookie)
    r.encoding = r.apparent_encoding
    text = json.loads(r.text)

    return text


def extract_data(text, df,jobType,updateDate):
    '''
    :param text: 爬取到的内容
    :param df: 标准输出的格式
    :return: dataframe格式数据
    '''
    if text != None:
        try:
            data = text.get('content').get('positionResult').get('result')

            for d in data:
                job = {}
                job['公司'] = d['companyShortName']
                job['职位'] = d['positionName']
                job['城市'] = d['city']
                job['位置'] = d['district']
                job['工资'] = d['salary']
                job['具体链接'] = 'https://www.lagou.com/jobs/' + str(d['positionId']) + '.html'
                job['职位类型'] = jobType
                job['更新时间'] = updateDate

                df = df.append(job, ignore_index=True)
        except:
            pass

    return df


def lagou_main(city, jobType):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=',
    }
    url_start = 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput='
    url = 'https://www.lagou.com/jobs/positionAjax.json'

    columns = ['公司', '职位', '城市', '位置', '工资', '具体链接']
    df = pd.DataFrame(columns=columns)
    nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(nowtime)
    # 修改爬取量
    for i in range(1, 100):
        params = get_params(city, jobType, i)
        cookie = get_cookie(url_start, headers)
        text = get_text(url, headers, params, cookie)
        df = extract_data(text, df, jobType,nowtime )
        # time.sleep(3)

    return df

#创建一个按照秒数执行的任务
# schedule.every(3).seconds.do(test)
def job(t):
    print ("I'm working...", t)
    return
# 每秒执行任务
# schedule.every().second.do(job,'It is 01:00')
# 每天执行任务
# schedule.every().day.at("01:00").do(job,'It is 01:00')
#执行定时任务
# while True:
#     schedule.run_pending()
#     time.sleep(1)



if __name__ == '__main__':
     nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
     print(nowtime)
     # test()
     city = '深圳'
     kw = 'java'
     df = lagou_main(city, kw)
     print(df)
