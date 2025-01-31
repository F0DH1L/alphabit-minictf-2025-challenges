FROM ubuntu:22.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat 

RUN useradd ctf 

WORKDIR /challenge

COPY challenge .

RUN chown -R root:root .
RUN chmod +x chall entrypoint.sh ./glibc/libc.so.6 ./glibc/ld-linux-x86-64.so.2

EXPOSE 1341

USER ctf

ENTRYPOINT [ "./entrypoint.sh" ]
