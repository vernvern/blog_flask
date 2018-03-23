[![Build Status](https://travis-ci.org/vernvern/blog.svg?branch=master)](https://travis-ci.org/vernvern/blog)
[![Coverage Status](https://coveralls.io/repos/github/vernvern/blog/badge.svg?branch=master)](https://coveralls.io/github/vernvern/blog?branch=master)
# blog

## 项目结构

```
.
├── .coveralls.yml
├── .travis.yml
├── blog
│   ├── __init__.py
│   ├── api/
│   ├── config.py
│   ├── data/
│   ├── models/
│   ├── modules/
│   ├── settings.py
│   ├── static/
│   ├── templates/
│   └── toolkit/
├── deploy
│   ├── Dockerfiles
│   │   ├── nginx
│   │   │   ├── Dockerfile
│   │   │   └── nginx.conf
│   │   ├── python
│   │   │   ├── Dockerfile
│   │   │   ├── requirements.txt
│   │   │   └── sources.list
│   │   └── redis
│   │       └── Dockerfile
│   └── docker_test_run.sh
├── docs/
├── manage.py
├── tests/

```
