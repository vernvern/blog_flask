#!/usr/bin/env python
# -*- coding=utf-8 -*-

import sys


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


def show_result(status):
        print(GOOD_RESULT if status == 0 else BAD_RESULT)


def main():
    show_result(True)
    sys.exit(True)


main()
