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


RUN set -ex \
    && RUN_DEPS=" \
        libexpat1 \
        libjpeg62-turbo \
        libpcre3 \
        libpq5 \
        mime-support \
        postgresql-client \
        procps \
        zlib1g \
    " \
    && seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
    && apt-get update && apt-get install -y --no-install-recommends $RUN_DEPS \
    && rm -rf /var/lib/apt/lists/*

RUN set -ex \
    && BUILD_DEPS=" \
        build-essential \
        git \
        libexpat1-dev \
        libjpeg62-turbo-dev \
        libpcre3-dev \
        libpq-dev \
        zlib1g-dev \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS \
    # && python3.7 -m venv /venv \
    # && /venv/bin/pip3 install -U pip \
    # && /venv/bin/pip3 install --no-cache-dir -r /requirements/production.txt \
    # && /venv/bin/pip3 install gunicorn \
    && pip3 install -U pip \
    && pip3 install -r /code/requirements.txt \
    && pip3 install gunicorn \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
# RUN pip3 install -r /code/requirements.txt
# RUN pip3 install gunicorn

RUN DATABASE_URL=postgres://none REDIS_URL=none python3 /code/manage.py collectstatic --noinput
# Set the working directory to /code/
WORKDIR /code/

RUN python3 manage.py migrate

# create table for block inventory
RUN python3 manage.py block_inventory
RUN python3 manage.py update_index

RUN useradd wagtail
RUN chown -R wagtail /code
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
