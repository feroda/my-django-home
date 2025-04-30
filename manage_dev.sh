#!/bin/bash

source ./.env
# grep ^BASE_URL .env > nginx/www/assets/.env

if [ "x$MY_IOT_ENV" != "xdev" ]; then
    echo "Error: MY_IOT_ENV for dev environment MUST be set to 'dev'";
    exit 100;
fi

COMMAND="docker compose -p $MY_IOT_PROJECT -f compose.yaml"
COMMAND="$COMMAND -f compose-dev.yaml"

exec ./managez_final_exec.sh "$COMMAND" $@
