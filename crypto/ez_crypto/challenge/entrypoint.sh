#!/bin/sh

EXEC="./chall.py"
PORT=#port

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive, exec:"$EXEC",stderr