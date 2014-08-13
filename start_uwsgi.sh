#!/bin/bash
exec /usr/local/bin/uwsgi \
    --http=:8080 \
    --wsgi-file=./src/app.py \
    --callable=app \
    --gevent=$GEVENT_WORKERS \
    --master=$UWSGI_MASTER \
    --die-on-term

