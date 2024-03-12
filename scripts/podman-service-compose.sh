#!/usr/bin/bash
#
#####
# source this file before running docker compose
####

# systemd creates the podman UNIX socket under /run/user/1000/podman/
# that have a File Descriptor
systemctl --user start podman.socket

# replace the DOCKER_HOST environment variable for the podman UNIXsocket
export DOCKER_HOST="unix://$XDG_RUNTIME_DIR/podman/podman.sock"

# curl acts as a client making a request to the systemd's socket unit file (Podman API Socket),
# which triggers the podman service unit file. podman.service inherits the socket File Descriptor
# and accept connection; this is an instance of a podman process in running state.
curl -H "Content-Type: application/json" --unix-socket "$XDG_RUNTIME_DIR/podman/podman.sock" http://127.0.0.1/_ping

# source this file before running docker compose
####

docker compose -f ./oci/container-compose.yml build
