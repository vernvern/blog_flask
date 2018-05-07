#! /bin/bash
flake8 --ignore=E402,F841,E402,F811 --exclude=__init__.py
ret_code=$?
if [ $ret_code == '0' ]; then
    figlet 'c o m m i t !'
else
    figlet 'W a r n i n g !'
fi
exit $ret_code
