# Set up Jenkins

1. Add repository key and to sources list
```
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
```
2. Ubuntu 18.04 comes with Java 9, install java 8 and jenkins
```
sudo add-apt-repository ppa:webupd8team/java
sudo apt install oracle-java8-installer
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo apt-add-repository "deb https://pkg.jenkins.io/debian-stable binary/"
sudo apt install jenkins
```
3. Start jenkins
```
sudo systemctl start jenkins
sudo systemctl status jenkins
```
4. Open jenkins at http://your_server_ip_or_domain:8080
