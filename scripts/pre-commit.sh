#! /bin/bash
flake8 --ignore=E402,F841 --exclude=__init__.py
if [ $? == '0' ]; then
    figlet 'c o m m i t !'
fi
