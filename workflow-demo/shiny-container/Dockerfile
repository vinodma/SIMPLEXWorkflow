FROM vinodmang/baylor_app

#Vinod's shiny server container uses :  https://github.com/rocker-org/shiny/blob/master/Dockerfile

# Python/Flask
RUN apt-get update -y
RUN apt-get install -y python python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt


#COPY ./shiny /srv/shiny-server/BaylorInteractiveViewer
COPY ./shiny /opt/shiny-server/samples/sample-apps/BaylorInteractiveViewer

RUN chmod 777 -R /opt/shiny-server/samples/sample-apps/BaylorInteractiveViewer

# Setup and run multiple processes with supervisor
# see: https://docs.docker.com/engine/admin/using_supervisord/
RUN apt-get update && apt-get install -y openssh-server apache2 supervisor
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd /var/log/supervisor
COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]
