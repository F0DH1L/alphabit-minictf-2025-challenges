#!/bin/bash

# List of paths to Docker Compose files for list 1

compose_paths_1=(
  "./web/forgery/docker-compose.yml"
  "./web/lfi/docker-compose.yml"
  "./web/sequel/docker-compose.yml"
  "./web/injector/docker-compose.yml"
  "./pwn/oops/docker-compose.yml"
  "./pwn/ret2ret/docker-compose.yml"
  "./pwn/ret2exit/docker-compose.yml"
  "./pwn/shellcoder/docker-compose.yml"
)


compose_paths_2=(
  "./misc/LinearReg/docker-compose.yml"
  "./misc/escaper/docker-compose.yml"
  "./misc/runner/docker-compose.yml"
  "./misc/filewhat/docker-compose.yml"

  "./web/Alpha_Member/docker-compose.yml"
  "./web/sequel_revenge/docker-compose.yml"
  "./web/templated/docker-compose.yml"

  "./crypto/ez_crypto/docker-compose.yml"
  "./crypto/rsa1/docker-compose.yml"
  "./crypto/rsa2/docker-compose.yml"

  "./pwn/bank/docker-compose.yml"
  "./pwn/pp/docker-compose.yml"
  "./pwn/ppp/docker-compose.yml"
  "./pwn/shellcoder-revenge/docker-compose.yml"

  "./reverse/patchme/docker-compose.yml"

)

compose_paths_3=(
  "./misc/escaper2/docker-compose.yml"

  "./crypto/rsa3/docker-compose.yml"
  "./crypto/rsa4/docker-compose.yml"
)
# Check if an integer argument was passed
if [[ ! $1 =~ ^[0-9]+$ ]]; then
  echo "Please provide an integer argument."
  exit 1
fi

# Choose the list of paths based on the input integer
if (( $1 == 1 )); then
  compose_paths=("${compose_paths_1[@]}")
elif (( $1 == 2 )); then
  compose_paths=("${compose_paths_2[@]}")
elif (( $1 == 3 )); then
  compose_paths=("${compose_paths_3[@]}")
else
  echo "Invalid integer argument. Please choose 1 or 2."
  exit 1
fi

# Iterate through the list of Docker Compose paths and run docker-compose up
for path in "${compose_paths[@]}"; do
  echo "Running Docker Compose for $path"
  docker-compose -f "$path" up --build -d
done