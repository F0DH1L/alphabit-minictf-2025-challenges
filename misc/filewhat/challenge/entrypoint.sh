#!/bin/sh
EXEC="./chall"
PORT=#port

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive EXEC:"$EXEC",stderr
