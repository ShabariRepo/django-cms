# for heroku or foreman/forego deployments once it gets on the server
release: yes "yes" | python manage.py migrate
web: uwsgi --http-socket=:$PORT --master --workers=2 --threads=8 --die-on-term --wsgi-file=samplecms/wsgi_production.py  --static-map /media/=/app/samplecms/media/ --offload-threads 1