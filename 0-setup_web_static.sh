#!/usr/bin/env bash
# Creates and configures an nginx server.

# Checks if the package nginx exists
if ! dpkg -l | grep -qw nginx; then
    sudo apt-get update
    sudo apt-get install nginx -y
    sudo ufw allow 'Nginx HTTP'
fi

# Create the following directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "
<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>
" | sudo tee /data/web_static/releases/test/index.html

# Check if the symbolic soft link exists, if it does then delete
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi

# Create a new symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give file ownership of the folder /data to user and group ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration
sudo tee /etc/nginx/sites-available/default > /dev/null << EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$HOSTNAME;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}
EOF

# Restart Nginx
sudo nginx -t && sudo systemctl restart nginx

# Ensure the script exits
exit 0





