# Docker with flask
## List of all active docker containers and images
docker ps

docker images

## List of all docker containers and images
docker ps -a

## Remove all docker containers and iamges
docker rm $(docker ps -aq)

docker rmi -f $(docker images -a -q)

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
```
docker run -it --name ubuntu1 ubuntu /bin/bash
-d detached
--rm - removes when stopped (testing)
-v docker volume
```

## Ubuntu basic setup
apt-get update -y && \
    apt-get install -y python3 python3-pip
    
apt-get install -y virtualenv

virtualenv foo-env -p python3

pip install django

## Build docker image
docker build -t docker-flask-url-shortener:latest .

docker run -d -p 5000:5000 docker-flask-url-shortener

## Tag docker image
docker tag docker-flask-url-shortener:latest vibhashchandra/docker-flask-url-shortener:latest

## Push image to docker hub
docker push vibhashchandra/docker-flask-url-shortener:latest

## Docker Volumne
docker run -it -v /Users/vibhashchandra/projects:/dockervol ubuntu bash

## Install docker compose
sudo apt  install docker-compose

## Docker installation on ubuntu
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04

https://runnable.com/docker/python/dockerize-your-flask-application

## Docker <none><none> and dangling images
https://www.projectatomic.io/blog/2015/07/what-are-docker-none-none-images/
