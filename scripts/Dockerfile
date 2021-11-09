FROM ubuntu:latest

# Add cron_update file in the cron directory
ADD cron_test /etc/cron.h/cron_test

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.h/cron_test

RUN touch ./cron-output.txt

#Install Cron
RUN apt-get update
RUN apt-get -y install cron

# Run the command on container startup
CMD ["cron", "-f"]