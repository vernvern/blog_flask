---

date_created: '2018-03-22T11:53:48.982744+08:00'
date_modified: '2018-03-22T11:53:48.982936+08:00'
hash: 3ab4736f6a92f08f70317c40666cdaa8
id: a81d9010-9a9e-4778-83d8-a7c6fca9309e
sort: "\u672A\u5206\u7C7B"
tags: []
title: "hexo\u5728github\u4E0A\u642D\u5EFA\u535A\u5BA2"

---

## 初始化

[TOC]

### github准备工作
- 安装git
- 添加代码仓
    1. 注册github
    2. github添加name.github.io仓库 （name是github 账号名）
    1. name.github.io完成初次提交

-  ssh key

    1. 生成ssh-key(linux下)：
        ```
        $ cd ~/.ssh   
    
        $ ssh-keygen -t rsa -C "your_email@example.com"
        ```
    1. 复制公钥`id_rsa.pub`的内容
    2. github --> settings --> SSH keys and GPG keys --> new ssh key --> 粘贴公钥`id_rsa.pub`的内容 --> save

    另测试ssh-key：
        
            $ ssh -T git@github.com     

    choose yes:
        
                Hi humingx! You've successfully authenticated, but GitHub does not provide shell access.

###  install hexo
- install node.js
- install hexo
        
        npm install -g hexo

### run hexo
-  初始化一个hexo项目

        $ hexo init

-  生成部署，第一次执行会添加一个public 文件夹，里面是博客的静态页面
  
        $ hexo g
-  生成预览
   
        $ hexo s

### hexo --> github page

- 配置_config.xml 文件：

    ```
    deploy:
        type: git
        repo: git@github.com:name/name.github.io.git
    ```
- push 

        $ hexo d



## 切换主题
- 寻找主题
- 在项目根目录下git clone 到 themes/name  (name随意)
- 安装依赖 if 有必要
- 修改hexo的_config.yml

    ```
    theme: name # 和上面的name 对应
    ```
- 加载主题：

        $ hexo g && hexo s
