

FROM centos


RUN yum install wget -y
RUN wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
RUN rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
RUN yum install java -y
RUN yum install jenkins -y
ENTRYPOINT systemctl start jenkins
CMD 'ls -l /var/lib/jenkins'
CMD 'ls -l /var/jenkins_home'
CMD 'cat /var/jenkins_home/secrets/initialAdminPassword'





