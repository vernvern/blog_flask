#!/usr/bin/env python
# -*- coding=utf-8 -*-

import sys
import glob
import itertools
import subprocess
from functools import wraps
import xml.etree.ElementTree as ET


# config

COVERAGE_RATE = 0.9

GOOD_RESULT = " \
                       _       _ \n \
 _ __    _   _   ___  | |__   | |\n \
| '_ \  | | | | / __| | '_ \  | |\n \
| |_) | | |_| | \__ \ | | | | |_|\n \
| .__/   \__,_| |___/ |_| |_| (_)\n \
|_|\n \
"

BAD_RESULT = " \
  __           _   _   _ \n \
 / _|   __ _  (_) | | | |\n \
| |_   / _` | | | | | | |\n \
|  _| | (_| | | | | | |_|\n \
|_|    \__,_| |_| |_| (_)\n \
"


def __process(cmd):
    proc = subprocess.Popen(cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    return proc.communicate()


def _coverage():
    ''' 检查代码覆盖率

    这个函数依赖着nosetest(), nosetest会生成xml文件
    这里会解析xml文件，然后做一些判断
    '''
    files = glob.glob('**/*coverage.xml', recursive=True)
    status = True
    msg = []
    if files:
        tree = ET.ElementTree(file=files[0])
        packages = tree.getroot()[1]
        for package in packages:
            if package.attrib['name'] == 'modules':
                for classes in package:
                    for tmp_class in classes:
                        data = tmp_class.attrib
                        rate = float(data['line-rate'])
                        if rate < COVERAGE_RATE:
                            status = False
                            name = data['filename']
                            msg.append("%s's coverage rate is too low \
                                        to pass(%s(now) -> %s(expect))"
                                       % (name, rate, COVERAGE_RATE))
    else:
        status = False
        msg.append('coverage.xml is not found,please run coverage before this')

    return {'status': status, 'msg': msg}


def format_print(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print('=' * 70)
        print('%s start\n' % func.__name__)
        ret = func(*args, **kw)
        print('\n%s end' % func.__name__)
        print('=' * 70)
        print('\n\n')
        return ret
    return wrapper


@format_print
def nosetest():
    ''' 单元测试

    - 单元测试
    - 代码覆盖率检查
    '''
    output = __process('nosetests --with-coverage --cover-erase \
                        --cover-package=blog --cover-xml')
    output = output[1].decode('utf-8').split('\n')
    for line in output:
        print(line)
        if line.startswith('FAILED'):
            status = False
            msg = 'unittests %s' % line
            break
    else:
        status = True
        msg = ''
    coverage = _coverage()
    status = coverage['status'] if status else False
    msg = coverage['msg'].insert(0, msg)
    return {'status': status, 'msg': msg}


@format_print
def total(msg):
    ''' 总结

    打印错误信息
    '''
    return [print(x) for x in itertools.chain(*msg)]


def show_result(status):
        print(GOOD_RESULT if status == 0  else BAD_RESULT)


def main():
    status = 0
    msg = []
    func_list = [nosetest]
    for func in func_list:
        check = func()
        if check['status'] is False:
            status = 1
            msg.append(check['msg'])

    total(msg)
    show_result(status)
    sys.exit(status)


main()
