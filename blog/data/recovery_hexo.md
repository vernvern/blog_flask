---

title: 恢复hexo环境
date_created: 2017/08/02 23:17:12
categories: hexo
comments: true

---



## 导读
前段时间重装了系统，但是忘记了怎么部署hexo了。。。。
随手记录如何恢复案发现场～

[TOC]

## 经过


首先～安装hexo环境：

    #   sudo apt install npm
    #   npm install -g hexo-cli 

*注：貌似依赖着nodejs，但我的ubuntu自带了*

 之后我从github把我之前的hexo项目相关文件clone下来
cd 到 hexo_blog/code之后，用 `npm install `然后华丽丽的报错了 

orz

```
              npm WARN optional Skipping failed optional dependency /chokidar/fsevents:
              npm WARN notsup Not compatible with your operating system or architecture: fsevents@1.1.2
              npm ERR! Linux 4.4.0-87-generic
              npm ERR! argv "/usr/bin/nodejs" "/usr/bin/npm" "install"
              npm ERR! node v4.2.6
              npm ERR! npm  v3.5.2
              npm ERR! code ELIFECYCLE

              npm ERR! node-sass@4.5.3 postinstall: `node scripts/build.js`
              npm ERR! Exit status 1
              npm ERR! 
              npm ERR! Failed at the node-sass@4.5.3 postinstall script 'node scripts/build.js'.
              npm ERR! Make sure you have the latest version of node.js and npm installed.
              npm ERR! If you do, this is most likely a problem with the node-sass package,
              npm ERR! not with npm itself.
              npm ERR! Tell the author that this fails on your system:
              npm ERR!     node scripts/build.js
              npm ERR! You can get information on how to open an issue for this project with:
              npm ERR!     npm bugs node-sass
              npm ERR! Or if that isn't available, you can get their info via:
              npm ERR!     npm owner ls node-sass
              npm ERR! There is likely additional logging output above.

              npm ERR! Please include the following file with any support request:
              npm ERR!     /home/vern/hexo_blog/code/npm-debug.log



```

报错后同事让我改代码。。。随便点了一下再执行`npm install`然后用另一台电脑改代码。。。
回来一看卧槽成功了。。。 ？？？？
不熟悉npm。。。挖个坑，就先这样吧～

接着我尝试用 `hexo g`生成静态页面发现报了一些warm：



    WARN  No layout: about.html
    .....
    .....



毫无期望地执行`hexo s` 开本地服务器，果然显示空白了
搜了下，发现问题大概是_config.yml里面的`theme`参数和theme文件夹里面的主题不匹配
看了一眼我的文件夹名我参数没有问题，于是ls一下主题文件夹，卧槽怎么是空的
orz 
去主题的的github clone回来

```
$ git clone https://github.com/tufu9441/maupassant-hexo.git themes/maupassant
$ npm install hexo-renderer-jade@0.3.0 --save
$ npm install hexo-renderer-sass --save
```

然后执行`hexo g`看到都成功了～于是`hexo s`开本地服务器成功了～

撒花～

本来以为到这里就完了，结果发现执行`hexo g`的时候才发现
我github的ssh-key在新电脑上没有
想偷懒从旧的粘过来发现并不行。。。

楼下链接十分详细～我就直接过程放下面，不唠叨了


## 整理



### github ssh-key
- 检查自己的 `~/.ssh`文件，有东西的话备份一下
- 生成新key： `$ ssh-keygen -t rsa -C "your_email@youremail.com"`
- 把公钥的内容复制出来
- 放到github的公钥配置上

### 恢复hexo环境
- 装环境
    ```
    # sudo apt install npm
    # npm install -g hexo-cli   
    ```
    由于我的主题不见了所以要clone下来，，另外不同主题这里需要装依赖有可能不一样
    ```
    $ git clone https://github.com/tufu9441/maupassant-hexo.git themes/maupassant   
    $ npm install hexo-renderer-jade@0.3.0 --save
    $ npm install hexo-renderer-sass --save

    ```
    迷之第一次运行报错，第二次成功
    ```
    npm install 
    ```
    由于恢复过程中曾中断，所以记录下来的有可能并不完整，请见谅

- hexo测试
    ```
    hexo g   // 生成静态文件
    hexo s   // 本地运行
    hexo d   // 部署到github，由于之前已经配置好了这里就直接用了～
    ```

- 遗留问题：

    - `npm install`命令执行第一次失败，第二次成功是什么鬼。。
    - clone 下来的主题不能直接`git add .` `git commit`到自己的github,这里需要弄明白为什么 
    - 在`hexo d`之后，貌似githubpage会有一小段时间不能访问，也不能提交(解决：并没有，是公司12点固定断网一次造成的orz)



## 参考文献

*参考文献:*

- [hexo官方文档](https://hexo.io/zh-cn/docs/)
- [主题maupassant的github](https://github.com/tufu9441/maupassant-hexo.git)
- [如何创建github公钥](https://gist.github.com/yisibl/8019693)





