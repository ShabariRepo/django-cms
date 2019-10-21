#!/bin/sh
set -e

until mysql $DATABASE_URL -c '\l'; do
  >&2 echo "Mysql is unavailable - sleeping"
  sleep 1
done

>&2 echo "Mysql is up - continuing"

if [ "$1" = '/venv/bin/uwsgi' ]; then
    /venv/bin/python manage.py migrate --noinput
fi

if [ "x$DJANGO_LOAD_INITIAL_DATA" = 'xon' ]; then
	/venv/bin/python manage.py load_initial_data
fi

exec "$@"

# RET=1
# echo "Waiting for database"
# while [[ RET -ne 0 ]]; do
#     sleep 1;
#     if [ -z "${MYSQL_PASSWORD}" ]; then
#         mysql -h $mysql -u $MYSQL_USER -e "select 1" > /dev/null 2>&1; RET=$?
#     else
#         mysql -h $mysql -u $MYSQL_USER -p$MYSQL_PASSWORD -e "select 1" > /dev/null 2>&1; RET=$?
#     fi
# done
# echo "DB reached, continuing"