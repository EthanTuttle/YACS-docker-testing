FROM ubuntu:latest

#Install Cron
RUN apt-get update
RUN apt-get -y install cron

# Add cron_update file in the cron directory
COPY cron-test /etc/cron.h/cron-test

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.h/cron-test

# Apply cron job
RUN crontab /etc/cron.h/cron-test

RUN touch /var/log/cron.log

#Start cron
CMD ["cron", "-f"]