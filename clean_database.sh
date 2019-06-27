#!/usr/bin/env bash

rm -r shadow/migrations
rm db.sqlite3

python manage.py makemigrations shadow
python manage.py migrate

python populate_shadow.py

python manage.py runserver
