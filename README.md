# django-docker-kubernetes

## Connecting to an EC2 instance

1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, under NETWORK & SECURITY, choose Key Pairs.
3. Choose Create Key Pair.
4. Enter a name for the new key pair in the Key pair name field of the Create Key Pair dialog box, and then choose Create.
5. Update permissions of key
 ```
chmod 400 my-key-pair.pem
```
6. Connect to EC2 instance
```
ssh -i /path/my-key-pair.pem ec2-user@2001:db8:1234:1a00:9691:9503:25ad:1761
```
7. Update and upgrade
```
sudo apt-get update
sudo apt-get upgrade
```
8. Install git
```
sudo apt install and configure git
git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"
```
9. Clone repository
```
git clone https://github.com/vibhash1083/django-docker-kubernetes.git
```
10. Install and set up virtual environment
11. Install nginx
```
sudo apt-get install nginx
sudo service nginx start
sudo service nginx stop
```
```
sudo nano /etc/nginx/nginx.conf
user ubuntu ubuntu;
```
```
sudo nano /etc/nginx/sites-enabled/default
access_log /home/ubuntu/projects/django-docker-kubernetes/pollsapp/nginx-access.log;
error_log /home/ubuntu/projects/django-docker-kubernetes/pollsapp/nginx-error.log info;
```
12. Gunicorn
```
pip install gunicorn
nano start_gunicorn.sh
```
```
APPNAME=pollsapp
APPDIR=/home/ubuntu/projects/django-docker-kubernetes/$APPNAME/

LOGFILE=$APPDIR'gunicorn.log'
ERRORFILE=$APPFIR'gunicorn-error.log'

NUM_WORKERS=3

ADDRESS=0.0.0.0:8000

cd $APPDIR

# source ~/.bashrc
# workon $APPNAME
source ../../denv/bin/activate

exec gunicorn $APPNAME.wsgi:application \
-w $NUM_WORKERS --bind=$ADDRESS \
--log-level=debug \
--log-file=$LOGFILE 2>>$LOGFILE  1>>$ERRORFILE &
```

```
chmod +x start_gunicorn.sh
./start_gunicorn.sh
```


Kill a process at a port
```
fuser -k -n tcp 8000
``


The web server
The web server receives an HTTP request from the client (the browser) and is usually responsible for load balancing, proxying requests to other processes, serving static files, caching and more. The web server usually interprets the request and sends it to the gateway. Common web server and Apache and Nginx. In this tutorial, we will use Nginx (which is also my favorite).

The Gateway
The gateway translates the request received from the web server so the application can handle it. The gateway is often responsible for logging and reporting as well. We will use Gunicorn as our Gateway for this tutorial.

The Application
As you may already guess, the application refers to your Django app. The app takes the interpreted request, process it using the logic you implemented as a developer, and returns a response.

13. Run application with gunicorn
```
gunicorn --bind 0.0.0.0:8000 pollsapp.wsgi:application
```

sudo apt-get install supervisor






[program:gunicorn] 
directory=/home/django/app-django/app command=/root/.virtualenvs/virtual-env-name/bin/gunicorn --workers 3 --bind unix:/home/django/app-django/app/app.sock app.wsgi:application 
autostart=true 
autorestart=true 
stderr_logfile=/var/log/gunicorn/gunicorn.out.log stdout_logfile=/var/log/gunicorn/gunicorn.err.log 
user=ubuntu 
group=w 
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8
[group:guni] 
programs:gunicorn






server {
   listen 80; 
    server_name 13.126.242.241; 
    location = /favicon.ico { access_log off; log_not_found off; } 
    location /static/ { 
        root /home/ubuntu/projects/django-docker-kubernetes/pollsapp/; 
    } 
    location / { 
        include proxy_params; 
        proxy_pass http://unix:/home/ubuntu/projects/django-docker-kubernetes/pollsapp/app.sock; 
    } 
}

    # +-------------------------+
    # |           NGINX         |
    # +-------------------------+
    # +-------------------------+
    # |         Gunicorn        |
    # |          Django         |
    # +-------------------------+
    # +-----------+ +-----------+
    # |  Postgres | |     S3    |
    # +-----------+ +-----------+


