FROM ubuntu:latest

#Install Cron
RUN apt-get update
RUN apt-get -y install cron
RUN apt-get -y install python

# Add cron_update file in the cron directory
COPY cron-test /etc/cron.h/cron-test

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.h/cron-test

RUN touch /var/log/cron.log

# Apply cron job
RUN crontab /etc/cron.h/cron-test

#Start cron
CMD ["cron", "f"]