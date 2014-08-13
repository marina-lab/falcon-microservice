#!/bin/bash
exec /usr/local/bin/uwsgi \
    --http-socket=:8080 \
    --wsgi-file=./src/app.py \
    --callable=app
