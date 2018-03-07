---

title: 在django中使用celery处理任务队列和定时任务
date: 2017/08/10 23:30:21
categories: python
updated: 2017/08/10 23:30:22
comments: true
toc: true

tags:
- celery
- django

---

## 前言:

使用django框架的时候，我需要定时同步数据这样一个功能。我那一丢丢的运维经验让我第一时间想到 脚本 + crontab 这样的组合。曾经用这样的组合定时地在服务器中备份数据和日志。

好了～既然有了方案A，我就可以放心地去折腾其他办法了～

用django + 定时 去搜索，主要找到三个方式：

- django脚本 + crontab
- django-celery
- 第三方插件 django-crontab

考虑到应用场景是公司的项目，公司里面主要是微软系的程序员，用linux的crontab大概是他们最不喜欢看到的样子了～而django-crontab是后来才发现的，而且celery在网上的资源比较多，以后给其他人维护的话难度也不会特别大，所以选择去折腾celery了～

另，感谢 杨仕航的博客, 他的《[Django Celery定时任务和时间设置](http://yshblog.com/blog/164)》这篇文章对我启发比较大。

后面内容分四个部分：
- 简述是我对celery的一些了解
- 环境部署
- 具体实现，里面代码的注释是这个部分的主导
- 参考文献～



## celery简述

根据资料得知，celery 是用python 开发的分布式任务队列处理库。

在我的项目中，分布式没有用到， 而任务队列是我需要的~

文档只有简单的介绍和一个快速开始之类的章节被翻译了，并且中文文档的版本(3.1)也跟不上celery(4.1.0)的节奏。

但是celery的中文教程在网上挺多的～

celery需要一个 中间人(worker) 这样的角色去发送和接受消息。关于 中间人(worker)， celery的[官方文档](http://docs.jinkan.org/docs/celery/getting-started/first-steps-with-celery.html#celerytut-broker) 列出了几个可行的选择～



在django中应用celery
- 异步的思路是： 通过路由异步触发使用celery绑定的函数，把任务交给 worker，返回, worker 在后台执行函数
- 定时任务的思路是:  beat服务检查定时任务， 检查到任务的时候把任务告诉worker服务, worker执行任务



## 环境部署

环境部署需要安装几个东西，清单：
- 中间人(worker)我选择了redis
- celery-with-redis (使用pip安装)
就这么多～

### redis部署

redis 的官方文档写的相当详细了～我简单的记录一下：

```

$ wget http://download.redis.io/releases/redis-4.0.1.tar.gz
$ tar xzf redis-4.0.1.tar.gz
$ cd redis-4.0.1
$ make

```
命令分别是 下载 - 解压 - 进入文件夹 - 编译

要想方便地使用redis命令的话，还需要执行`make install`, 这句需要sudo权限～

### celery-with-redis部署

这个只需要执行
```
pip install celery-with-redis
```
就完事了。。。。

顺便说一下, python项目用virtualenv + pip + requirement.txt 这样的方式去管理开发环境是十分爽的一件事儿～



## 实现

实现主要涉及到三个文件：
- proj/settings.py (django配置文件)
- proj/celery.py (celery配置文件，可以写带settings.py里面，但分离出来让代码块更加清晰)
- app/tasks.py （消息队列配置文件，在各app中新建）

以及 \_\_init__.py的一些简单配置

废话不多说，看代码:

proj/settings.py:
``` python
# celery 中间人
BROKER_URL = 'redis://localhost:6379/0'

# celery 结果返回, 用于追踪结果
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# celery 呢诶用等消息的格式设置
CELERY_APPCEPT_CONTENT = ['application/json',]
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# CELERY 时区设置，使用TIME_ZONE同样的时区
CELERY_TIMEEZONE = TIME_ZONE

```

proj/celery.py:
```python
from __future__ import absolute_import, unicode_literals

from celery import Celery
from django.conf import settings
import os

project_name = os.path.split(os.path.abspath('.'))[-1] # 项目名字

project_settings = "{0}.settings".format(project_name) # 项目配置文件

os.environ.setdefault('DJANGO_SETTINGS_MODULE', project_settings) # 加载django环境

app = Celery(project_name) # 实例化celery

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) # 加载各app的tasks
```

然后在proj/\_\_init__.py中添加`from .celery import app as celery_app` 这一句让django启动时自动加载celery

接着可以定义任务了， app/tasks.py：
``` python

from django.test import TestCase

# Create your tests here.



from celery.decorators import task
from celery.decorators import periodic_task
from celery.task.schedules import crontab

@celery_app.task
def test_async():
    ''' 异步任务
    '''
    pass

@periodic_task(run_every=crontab(minute='0'))
def test_timing():
    ''' 定时任务
    '''
    pass

```

特别说明一下，`crontab(minute='0')`这个参数，就是类是linux 的crontab的用法，用于设置某些时间，当beat监听到对应的时间的时候，就触发函数了～

celery的crontab在源码上是这样的：
```
crontab(minute='*', hour='*', day_of_week='*', day_of_month='*', month_of_year='*')
```
由于我已经困了。。。。这里怎么用请参考 [Django Celery定时任务和时间设置](http://yshblog.com/blog/164) 或者自行搜索。。
也许哪天我会补这个坑。。。。



## 参考文献

*参考文献：*

- [celery文档](http://docs.jinkan.org/docs/celery/)
- [Django Celery定时任务和时间设置](http://yshblog.com/blog/164)
- [redis官方下载链接与安装教程](https://redis.io/download)




