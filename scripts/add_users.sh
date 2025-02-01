#!/bin/bash

# Define the file name
file="users.csv"

# Read the file line by line
while IFS=, read -r timestamp email full_name
do
    # Skip the header line
    if [[ "$timestamp" == "Timestamp" ]]; then
        continue
    fi
    password=$(head -c 20 /dev/urandom | base64 | xxd -p)
    echo "$email, $full_name, $password"
    curl -X POST https://mini-ctf.alphabit.club/api/v1/users \
    --header "Authorization: Token ctfd_ed228addf20da759c22a4c91460730a98f0bc46ae1a26b0552371e2445927f95" \
    --header "Content-Type: application/json" \
    -d "{\"name\":\"$full_name\",\"email\":\"$email\",\"password\":\"$passwprd\",\"type\":\"user\",\"verified\":false,\"hidden\":false,\"banned\":false,\"fields\":[]}"
done < "$file"


