############################################################
# Dockefile for the soat insurance calculator
############################################################

FROM jaconsta/python:3.5
# FROM ubuntu:16.04

MAINTAINER  Javier Constain

# Environmental variables.
# Local directory with project source
ENV DOCKYARD_SRC=api
# Directory in container for all project files
ENV DOCKYARD_SRVHOME=/srv
# Directory in container for project source files
ENV DOCKYARD_SRVPROJ=/srv/api

# Update sources packages
# run apt-get update && apt-get upgrade -y
# run apt-get install -y python3.5 python3-pip

# Create application subdirectories
WORKDIR $DOCKYARD_SRVHOME
RUN mkdir media static logs
VOLUME ["$DOCKYARD_Sdd_SRVHOME/logs/"]

# Copy application source code to SRCDIR
COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ

# Install Python dependencies
RUN pip3 install -r $DOCKYARD_SRVPROJ/requirements.txt

# Port to expose
EXPOSE 8000

# Copy entrypoint script into the image
WORKDIR $DOCKYARD_SRVPROJ
COPY ./entrypoint.sh /
run sh /entrypoint.sh
ENTRYPOINT exec gunicorn api.wsgi:application --name api --bind 0.0.0.0:8000 --workers 3
