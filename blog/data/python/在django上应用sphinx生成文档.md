---
title: 在django上应用sphinx生成文档
date: 2017/06/10 14:52:00
categories: python
updated: 2017/06/10 14:52:00
comments: true
toc: true

tags:
- django
- sphinx

---

## quickly start sphinx

### 安装sphinx
就是这么简单：

        (env)$ pip install sphinx

### 添加sphix到项目中
- 执行 `$ sphinx-quickstart`
- 根据提示配置：# 提示后面有输入的是需要配置的，留空的地方用默认 
    
    TODO: 翻译成中文 
    
    >enter values for the following settings (just press Enter to
    accept a default value, if one is given in brackets).
    
    >Enter the root path for documentation.
    >> Root path for the documentation [.]: doc
    
    >You have two options for placing the build directory for Sphinx output.
    Either, you use a directory "_build" within the root path, or you separate
    "source" and "build" directories within the root path.
    >> Separate source and build directories (y/n) [n]: 

    >Inside the root directory, two more directories will be created; "_templates"
    for custom HTML templates and "_static" for custom stylesheets and other static
    files. You can enter another prefix (such as ".") to replace the underscore.
    >> Name prefix for templates and static dir [_]: 

    >The project name will occur in several places in the built documentation.
    >> Project name: django_board
    
    > Author name(s): Vern

    >Sphinx has the notion of a "version" and a "release" for the
    software. Each version can have multiple releases. For example, for
    Python the version is something like 2.5 or 3.0, while the release is
    something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
    just set both to the same value.
    >> Project version []: 0.1
    
    > Project release [0.1]: 

    >If the documents are to be written in a language other than English,
    you can select a language here by its language code. Sphinx will then
    translate text that it generates into that language.
    For a list of supported codes, see http://sphinx-doc.org/config.html#confval-language.
    >> Project language [en]: zh_CN

    >The file name suffix for source files. Commonly, this is either ".txt"
    or ".rst".  Only files with this suffix are considered documents.
    >> Source file suffix [.rst]: 

    >One document is special in that it is considered the top node of the
    "contents tree", that is, it is the root of the hierarchical structure
    of the documents. Normally, this is "index", but if your "index"
    document is a custom template, you can also set this to another filename.
    >> Name of your master document (without suffix) [index]: 

    >Sphinx can also add configuration for epub output:
    >> Do you want to use the epub builder (y/n) [n]: 

    >Please indicate if you want to use one of the following Sphinx extensions:

    > autodoc: automatically insert docstrings from modules (y/n) [n]: y

    > doctest: automatically test code snippets in doctest blocks (y/n) [n]: 

    > intersphinx: link between Sphinx documentation of different projects (y/n) [n]: 

    > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: 

    > coverage: checks for documentation coverage (y/n) [n]: 

    > imgmath: include math, rendered as PNG or SVG images (y/n) [n]: 
    
    > mathjax: include math, rendered in the browser by MathJax (y/n) [n]: 
    
    > ifconfig: conditional inclusion of content based on config values (y/n) [n]: 
    
    > viewcode: include links to the source code of documented Python objects (y/n) [n]: 
    
    > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: 

    >A Makefile and a Windows command file can be generated for you so that you
    only have to run e.g. `make html' instead of invoking sphinx-build
    directly.
    >> Create Makefile? (y/n) [y]: 
    > Create Windows command file? (y/n) [y]: 

### 配置 conf.py : `$ vim doc/conf.py`
``` python
    import os
    import sys
    import django
    sys.path.insert(0, os.path.abspath('.'))
    # 缺少此行会导致在make html时提示 __import__出错，找不到module。 所以必须把上一级目录(即代码所在目录)include进来
    sys.path.insert(0, os.path.abspath('..'))

    # 将settings加载到环境变量里面
    os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings'
    # 加载django模块和上下文
    django.setup()

 ```

### 生成文档（html格式）
#### 生成rst文件命令:
- 执行：

        $ sphinx-apidoc -o doc . 
    'doc' 是sphinx地址，里面有一个conf.py,  '.' 是生成文件存放路径

    注：文档生成的东西受rst文件控制

- 把生成的 doc/modules.rst添加到index.rst


#### 运行构建
- 使用sohinx-build命令

    sourcedir 是指 源目录，builddir 是指你想放置的生成文件的位置。-b 选择了生成器；在本例中Sphinx将会生成HTML格式的文件。

        $ sphinx-build -b html sourcedir builddir

*参考文献：*
- [sphinx文档-初入sphinx](http://www.pythondoc.com/sphinx/tutorial.html)
- [博客园sunada2005-使用sphinx自动提取python中的注释成为接口文档](http://www.cnblogs.com/sunada2005/p/6306677.html)
- [Alfred Huang (黄文超)的个人空间-使用 SPHINX 创建 DJANGO 整体项目文档](https://www.huangwenchao.com.cn/2015/12/djangp-sphinx.html)
## 文档结构
- 通过修改rst文件可以修改生成文档的结构
