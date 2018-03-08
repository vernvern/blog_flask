---

title: python3实现微信接入小冰~
date: 2017/06/12 21:30:12
categories: python
updated: 2017/06/12 21:30:12
comments: true
toc: true

tags:
- itchat


---

## 导读:

本教程分三部分， 其中
- 搭建环境是必须的～
- 快速开始
- 给开发者的～

另重点感谢github的[yanwii](https://github.com/yanwii/), 实现这个功能其中一个关键点是使用了他github库的[微软小冰微博api](https://github.com/yanwii/msxiaoiceapi)

[TOC]

## 搭建运行环境
1. 以下二选一：
    - linux请自行命令安装python3 以及 对应pip
    - windows 请自尽，目前我使用的yanwii的api在windows下报错。。

1. 有了python 以及pip 之后，就可以开始安装一些依赖的库啦～
    ```
    pip install flask
    pip install itchat
    pip install bs4
    ```



## 快速开始
下载源码包, 请移步到[我的百度云](http://pan.baidu.com/s/1qYa2iM4)下载源码

然后直接执行，扫码登录，之后就可以了，撒花～

*注: 如果这样直接运行，跑的是我微博的小冰。。。。请温柔对待～

## 实现过程

1. 从 [yanwii的微软小冰微薄api](https://github.com/yanwii/msxiaoiceapi) 下载一份代码
2. 请按照yanwii的github上的说明重新设置小冰的接口（图文并茂），具体步骤包括:
    - 打开微博小冰私信
    - 开调试模式并且向小冰发送私信
    - 将调试（Chrome里面的Network）获得的`getbyid?@#$%^&`中的Request Headers的所有信息复制到headers.txt中
1. 写主函数(根目录下)

    `$ vim main.py`

    ```python

    import itchat
    import xiaoiceapi as xb

    xiaobing = xb.xiaoiceApi()


    @itchat.msg_register(itchat.content.TEXT)
    def print(msg):
        string = msg['Text'] # 获得对方发过来的消息
            ret = xiaobing.chat(string) # 往小冰api发送消息
                return ret['text'] # 返回小冰的回复给对方


    itchat.auto_login(hotReload=True) # 登录微信
    itchat.run() # 运行服务
    ```


2. 然后就`python main.py`运行就阔以了～


## 参考文献：
*参考文献：*
- [yanwii的微软小冰微薄api](https://github.com/yanwii/msxiaoiceapi)
- [itchat官方文档](http://itchat.readthedocs.io/zh/latest/)





