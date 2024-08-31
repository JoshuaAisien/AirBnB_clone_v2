#!/usr/bin/env bash
# install Nginx if it not already installed
if ! dpkg -l | grep -sw nginx > dev/null  2>&1;then
  sudo apt update
  sudo apt install -y nginx
else:
  echo "Nginx is already installed"
fi
# create a folder if it doesn't  exit
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
# create a fake HTML file

echo " <!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<p> hello_world </p>
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# create a symbolic link to be deleted and recreated every-time the script is ran
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# ownership of /data/ folder
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/server_name _;/a\
      location /hbnb_static {\
          alias /data/web_static/current/;\
          }' /etc/nginx/sites-availble/default

echo "complete"
