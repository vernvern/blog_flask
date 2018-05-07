
application_run () {
    while [ 1 ]
        do
            line = ps aux | grep 'gunicorn' | wc -l
            if [[ $line -lt 1 ]];then
                gunicorn -w 4 -b 127.0.0.1:8000 wsgi:app
            else
                sleep 2
            fi
        done
}


main () {
    application_run
}


main >> /opt/log/stdout.log 2>> /opt/log/stderr.log
