# MindMapper Server

> The Server that MindMapper Runs On

## Description:
The Server that MindMapper runs on is Ubuntu 22.04 LTS. It allows for our server to be run on anything, including things as small as USB's to as big as Enterprice-Grade Servers.

We hold data and use industry standard databasing and server systems. Linode as our backend Server and PostgreSQL as our backend database allows us to stay safe, secure, and scalable for the future.

# Build Instructions

# Dependencies
> Ubuntu 22.04 LTS [Click Here for Download Options](https://ubuntu.com/download/server)

## Installing and Running The Database Server
1. Install Ubuntu Server 22.04 LTS on a Virtual/Barebones Machine.

2. SSH and Configure the Server for installation of dependencies, required libraries, updates and upgrades, firewall, and reboot.
```
ssh root@xxx.xxx.xxx.xxx
sudo apt-get update -y && sudo apt-get full-upgrade -y
sudo apt-get install gnupg2 zip unzip libpq-dev nano dos2unix -y
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget -qO- https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo tee /etc/apt/trusted.gpg.d/pgdg.asc &>/dev/null
sudo apt-get update -y && sudo apt-get full-upgrade -y
sudo apt install postgresql postgresql-client -y
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow 5432
sudo ufw allow enable
echo -e "host all all 0.0.0.0/0 md5\nhost all all ::0/0 md5" >> /etc/postgresql/15/main/pg_hba.conf
sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" /etc/postgresql/15/main/postgresql.conf
sudo reboot
```
