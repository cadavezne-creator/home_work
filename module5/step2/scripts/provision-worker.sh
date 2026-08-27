#! /bin/bash

set -e

apt-get update
sudo apt-get install -y openjdk-11-jre-headless curl git
sudo apt install openjdk-17-jre-headless -y
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


if ! id -u jenkins > /dev/null 2>&1; then
        useradd -m -s /bin/bash jenkins
      fi
      # Добавляем пользователей в группу docker
      usermod -aG docker vagrant
      usermod -aG docker jenkins

      # 5. Подготовка рабочей директории Jenkins Agent
      mkdir -p /home/jenkins/agent
      chown -R jenkins:jenkins /home/jenkins/


sudo curl -sO http://192.168.56.10:8080/jnlpJars/agent.jar;
sudo java -jar agent.jar -url http://192.168.56.10:8080/ -secret cf589b1c6fc3fc3211d0f138581e35c0872878e7b0bc28b7f6b27539c35196b4 -name test -webSocket -workDir "/home/jenkins/agent"
sudo chown jenkins:jenkins /home/jenkins/agent.jar



echo " Setup complite"
