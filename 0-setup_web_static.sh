#!/usr/bin/env bash
<<<<<<< HEAD
# 0. Prepare your web servers
apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
=======
#script that sets up your web servers for the deployment
sudo su
apt-get update -y
apt-get install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
printf %s "<html>
>>>>>>> cd4c93e33e47d8d47247bb74daae22eff0d3b36b
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
<<<<<<< HEAD
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart
exit 0
=======
ln -sf /data/web_static/releases/test/ /data/web_static/current/
chown -R ubuntu /data/
chgrp -R ubuntu /data
sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" \etc/nginx/sites-available/default
service nginx start
>>>>>>> cd4c93e33e47d8d47247bb74daae22eff0d3b36b
