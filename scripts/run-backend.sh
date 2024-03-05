#!/bin/bash
#
#

export DB_URL="postgresql://admin:Passw0rd@localhost:5432/"
export FLASK_APP="./app/app.py"
source ../venv/bin/activate
pip3 install --upgrade pip
pip3 install -r ./backend/requirements.txt
cd ./backend/ || exit
#flask --app app run --debug
flask --debug run
