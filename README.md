#### 整体架构

 ![image-20210219235435975](https://twc20201231shenzhen.oss-cn-shenzhen.aliyuncs.com/r53600image-20210219235435975.png)

####  代码结构

```
├─database   //python爬虫
├─email_fun  
├─front     // 前端代码
└─mysite    //后台业务代码

```



#### 前端展示页面

![image-20210220000749154](https://twc20201231shenzhen.oss-cn-shenzhen.aliyuncs.com/r53600image-20210220000749154.png)

![image-20210220000806177](https://twc20201231shenzhen.oss-cn-shenzhen.aliyuncs.com/r53600image-20210220000806177.png)

##### 数据库设计 

```
CREATE TABLE `lagou` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`company` VARCHAR(128) NOT NULL COMMENT '公司名' COLLATE 'utf8_general_ci',
	`job` VARCHAR(128) NULL DEFAULT NULL COMMENT '工作' COLLATE 'utf8_general_ci',
	`city` VARCHAR(128) NULL DEFAULT NULL COMMENT '城市' COLLATE 'utf8_general_ci',
	`site` VARCHAR(128) NULL DEFAULT NULL COMMENT '站点' COLLATE 'utf8_general_ci',
	`salary` VARCHAR(128) NULL DEFAULT NULL COMMENT '薪资' COLLATE 'utf8_general_ci',
	`url` VARCHAR(255) NULL DEFAULT NULL COMMENT '网址' COLLATE 'utf8_general_ci',
	`update_time` VARCHAR(255) NULL DEFAULT NULL COMMENT '更新时间' COLLATE 'utf8_general_ci',
	`job_type` VARCHAR(255) NULL DEFAULT NULL COMMENT '工作类型' COLLATE 'utf8_general_ci',
	PRIMARY KEY (`id`) USING BTREE
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=1546
;

```

![image-20210219234153523](https://twc20201231shenzhen.oss-cn-shenzhen.aliyuncs.com/r53600image-20210219234153523.png)

#### 项目部署

##### 拉勾网、智联招聘、BOSS直聘网爬虫程序

该项目为三大招聘网站的爬虫程序  
通过给定搜索词与城市，即可进行数据爬取  
数据可以通过发送excel到特定邮件。还可以导入数据库中，在email和data_base文件夹中有相关程序


##### 爬取 城市/岗位 信息
bossP/database insert_data.py  

##### mysite 项目部署
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

 

项目在linux中部署 、 开启screen          

 新建窗口
 screen -S 
 恢复窗口
 screen -r  bossP       
 python manage.py runserver 0.0.0.0:8000   
 ctrl a +d   