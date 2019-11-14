# Use an official Python runtime as a parent image
FROM python:3.7
LABEL maintainer="sshenoy@centrilogic.com"

# Set environment varibles
# comment these out if needed per environment
ENV http_proxy http://10.228.12.41:8888
ENV https_proxy http://10.228.12.41:8888

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

COPY ./requirements.txt /code/requirements.txt

# Copy the current directory contents into the container at /code/
COPY . /code/
WORKDIR /code/

# RUN set -ex \
#     && RUN_DEPS=" \
#         libexpat1 \
#         libjpeg62-turbo \
#         libpcre3 \
#         libpq5 \
#         mime-support \
#         python-dev default-libmysqlclient-dev \
#         python3-pymysql \
#         postgresql-client \
#         procps \
#         zlib1g \
#     " \
#     && seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
#     && apt-get update && apt-get install -y --no-install-recommends $RUN_DEPS \
#     && rm -rf /var/lib/apt/lists/*
# postgresql-client \
# default-libmysqlclient-dev \

# RUN set -ex \
#     && BUILD_DEPS=" \
#         build-essential \
#         git \
#         libexpat1-dev \
#         libjpeg62-turbo-dev \
#         libpcre3-dev \
#         libpq-dev \
#         zlib1g-dev \
#     " \
#     && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS \
    # && python3.7 -m venv /venv \
    # && /venv/bin/pip3 install -U pip \
    # && /venv/bin/pip3 install --no-cache-dir -r /requirements/production.txt \
    # && /venv/bin/pip3 install gunicorn \
RUN pip install --upgrade pip \
    && pip install -r /code/requirements.txt \
    && pip install gunicorn 
    # && pip install mysqlclient \
    # && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    # && rm -rf /var/lib/apt/lists/*
# RUN pip3 install --upgrade pip

# Install any needed packages specified in requirements.txt
# RUN pip3 install -r /code/requirements.txt
# RUN pip3 install gunicorn
# RUN pip install mysql-python

RUN DATABASE_URL=mysql://none REDIS_URL=none python3 /code/manage.py collectstatic --noinput
# RUN python3 /code/manage.py collectstatic --noinput
# Set the working directory to /code/
# WORKDIR /code/

# RUN python3 manage.py migrate

# create table for block inventory
# run these inside the container upon creation
# RUN python3 manage.py block_inventory
# RUN python3 manage.py update_index
# RUN python3 manage.py createsuperuser 

RUN mkdir -p /code/media/images && mkdir -p /code/media/documents && mkdir -p /code/media/original_images
RUN chmod 777 /code/media/original_images && chmod 777 /code/media/images && chmod 777 /code/media/documents

RUN useradd wagtail
RUN chown -R wagtail /code

# RUN chmod 777 /code/docker-entrypoint.sh
# ENTRYPOINT ["/code/docker-entrypoint.sh"]

# mark the destination for images as a volume
VOLUME ["/code/media/images/"]
VOLUME ["/code/media/original_images/"]

USER wagtail
EXPOSE 8000
CMD exec gunicorn samplecms.wsgi:application --bind 0.0.0.0:8000 --workers 3



# Use an official Python runtime as a parent image
# FROM python:3.7
# LABEL maintainer="sshenoy@centrilogic.com"

# # Set environment varibles
# # comment these out if needed per environment
# #ENV http_proxy http://10.228.12.41:8888
# #ENV https_proxy http://10.228.12.41:8888

# ENV PYTHONUNBUFFERED 1
# ENV DJANGO_ENV dev

# COPY ./requirements.txt /code/requirements.txt
# RUN pip3 install --upgrade pip


# # Copy the current directory contents into the container at /code/
# COPY . /code/

# # Install any needed packages specified in requirements.txt
# RUN pip3 install -r /code/requirements.txt
# RUN pip3 install gunicorn

# # Set the working directory to /code/
# WORKDIR /code/

# RUN python3 manage.py migrate

# RUN useradd wagtail
# RUN chown -R wagtail /code
# USER wagtail

# EXPOSE 8090
# CMD exec gunicorn samplecms.wsgi:application --bind 0.0.0.0:8090 --workers 3
