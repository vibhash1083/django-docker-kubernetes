# Docker with flask
## List of all active docker images
docker ps

## List of all docker images
docker ps -a

## Remove all docker images
docker rm $(docker ps -aq)

## Run hello world
docker run hello-world

## Run docker ubuntu container
docker run -it ubuntu bash

## Run existing ubuntu container
docker exec -it [container-id] bash

## Start/Stop container
docker start id
docker stop id
docker attach id

docker run -it --name ubuntu1 ubuntu /bin/bash
-d detached
--rm - removes when stopped (testing)
-v docker volume

## Ubuntu basic setup
apt-get update -y && \
    apt-get install -y python3 python3-pip
    
apt-get install -y virtualenv
virtualenv foo-env -p python3
pip install django

## Build docker image
docker build -t flask-tutorial:latest .
docker run -d -p 5000:5000 flask-tutorial

## Docker Volumne
docker run -it -v /Users/vibhashchandra/projects:/dockervol ubuntu bash

https://runnable.com/docker/python/dockerize-your-flask-application