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
8. Install and configure git
```
sudo apt-get install git
git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"
```
9. Clone repository
```
git clone https://github.com/vibhash1083/django-docker-kubernetes.git
```
10. Install and set up virtual environment
```
sudo apt install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
```
11. Install requirements and Run server
```
cd django-docker-kubernetes/
pip install -r requirements.txt
python pollsapp/manage.py migrate
python pollsapp/manage.py runserver 0.0.0.0:8000
```
We can start server in background by using &
```
python pollsapp/manage.py runserver 0.0.0.0:8000 &
```
12. Why not Django in production environment?
Django server is lightweight and designed for development environment only.
Till 1.7 it was single threaded
No security and performance audit
Lesser configuration option

12. Architecture
>    # +-------------------------+
>    # |           NGINX         |
>    # +-------------------------+
>    # +-------------------------+
>    # |         Gunicorn        |
>    # |          Django         |
>    # +-------------------------+
>    # +-----------+ +-----------+
>    # |  Postgres | |     S3    |
>    # +-----------+ +-----------+

13. Set up nginx
High performance web server, load balancer and reverse proxy
Set up static files folder and run manage.py collectstatic
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

```
sudo apt-get install nginx
sudo service nginx start
sudo service nginx stop
sudo service nginx restart
```
Access server at http://<ip-address>
```

14 Set up gunicorn
Gunicorn is python WSGI(Web server gateway interface) HTTP server for Unix. WSGI is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request.
```
pip install gunicorn
```
15. Start WSGI server using gunicorn
```
gunicorn pollsapp.wsgi:application --bind 0.0.0.0:8000
or
gunicorn pollsapp.wsgi:application --bind 0.0.0.0:8000 &
```
16. Configure nginx with gunicorn
Add configuration to the file 
```
sudo nano /etc/nginx/sites-enabled/pollsapp
```

```
server {
    server_name 13.127.254.61;

    access_log off;

    location /static/ {
        alias /home/ubuntu/projects/django-docker-kubernetes/pollsapp/static/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header X-Forwarded-Host $server_name;
        proxy_set_header X-Real-IP $remote_addr;
        add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
    }
}
```

or 

Add config to /etc/nginx/sites-available/pollsapp and create a symlink
```
sudo ln -s /etc/nginx/sites-available/pollsapp /etc/nginx/sites-enabled/pollsapp
```

Whenever config has to be disabled, remove symlink.
17. Script to start gunicorn
Create and edit start_gunicorn.sh file
```
APPNAME=pollsapp
APPDIR=/home/ubuntu/projects/django-docker-kubernetes/$APPNAME/

LOGFILE=$APPDIR'gunicorn.log'
ERRORFILE=$APPFIR'gunicorn-error.log'

NUM_WORKERS=3

ADDRESS=0.0.0.0:8000

cd $APPDIR

source /home/ubuntu/projects/venv/bin/activate

exec gunicorn $APPNAME.wsgi:application \
-w $NUM_WORKERS --bind=$ADDRESS \
--log-level=debug \
--log-file=$LOGFILE 2>>$LOGFILE  1>>$ERRORFILE &
```
Make it executable and run it
```
chmod +x start_gunicorn.sh
./start_gunicorn.sh
```
18. Set up runit


### Notes
Kill a process at a port
```
fuser -k -n tcp 8000
``


The web server
The web server receives an HTTP request from the client (the browser) and is usually responsible for load balancing, proxying requests to other processes, serving static files, caching and more. The web server usually interprets the request and sends it to the gateway. Common web server and Apache and Nginx. 

The Gateway
The gateway translates the request received from the web server so the application can handle it. The gateway is often responsible for logging and reporting as well. We will use Gunicorn as our Gateway for this tutorial.

The Application
As you may already guess, the application refers to your Django app. The app takes the interpreted request, process it using the logic you implemented as a developer, and returns a response.

