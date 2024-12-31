#!/bin/sh

docker build -t ez_crypto .

docker run -p 1337:1337 ez_crypto