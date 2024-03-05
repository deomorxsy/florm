#!/usr/bin/bash
#
#
#req=$(cat ./register.json)
curl --header "Content-Type: application/json" \
    --request POST \
    --data-binary @register.json \
    http://127.0.0.1:5000/auth/register
