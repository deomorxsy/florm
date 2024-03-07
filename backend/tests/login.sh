#!/usr/bin/bash
#
#
#req=$(cat ./register.json)
req=$( cat << 'EOF'
{
    "username": "johndoe123",
    "password": "pdfsadfdsafdsafda"
}
EOF
)
curl --header "Content-Type: application/json" \
    --request POST \
    --data "$req" \
    http://127.0.0.1:5000/auth/login
