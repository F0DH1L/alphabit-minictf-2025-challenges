#!/bin/bash

DEPTH="3"

for c in $(find -mindepth "${DEPTH}" -maxdepth "${DEPTH}" -name challenge.yml); do
    c="${c%/challenge.yml}"
    echo "${c#./}"
done
