#! /bin/bash

set -e 

## Развертываем сервер для прирлоения приложения
echo "#################################################"
echo "устанавливаем докер и дженкинс"
echo "#################################################"



## Установка необходимых пакетов т добавление репозитория докера
apt-get update
sudo apt install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF
# install docker
apt-get update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
systemctl status docker


echo "#################################################"
echo "докер работает"
echo "#################################################"

# start jenkins container
sudo docker volume create jenkins_home

sudo docker run -d --restart=always --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk17

#  test

echo " Setup complite"