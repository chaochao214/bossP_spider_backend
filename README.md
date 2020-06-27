## 拉勾网、智联招聘、BOSS直聘网爬虫程序
该项目为三大招聘网站的爬虫程序  
通过给定搜索词与城市，即可进行数据爬取  
数据可以通过发送excel到特定邮件。还可以导入数据库中，在email和data_base文件夹中有相关程序


# 爬取 城市/岗位 信息
bossP/database insert_data.py  

# mysite 项目部署
django 命令

1.
cd到bossP/mysite目录下
1. 
git clone /git pull 更新代码
2. migrate
bossP\mysite> python  manage.py migrate
3.安装mysqlclient
bossP\mysite>pip install mysqlclient
4.启动
bossP\mysite> django-admin startproject mysite
5.启动
bossP\mysite>python manage.py runserver

 
 
 #项目在linux中部署 、 开启screen
 screen -r  bossP
 python manage.py runserver 0.0.0.0:8000
 ctrl a +d 