FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y openssh-server cron

RUN useradd -m -s /bin/bash ctf && \
    echo 'ctf:ctf' | chpasswd

WORKDIR /home/ctf

RUN chown -R root:root . && \
    chmod o+rx .

COPY challenge/flag.txt .
COPY challenge/chall .

RUN chown root:root chall & chmod 775 chall & chmod u+s chall

RUN chown root:root flag.txt && chmod 440 flag.txt
RUN ln -s /dev/null /home/ctf/.bash_history 
RUN echo "*/5 * * * * root	rm -rf /tmp/*" >> /etc/crontab 
RUN chmod -r /tmp /var/tmp /run/lock
RUN chmod go-rx /usr/bin/passwd
EXPOSE 22

ENTRYPOINT service ssh start \
    && tail -f /dev/null
