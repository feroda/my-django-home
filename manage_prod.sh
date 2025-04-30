#!/bin/bash

source ./.env
# grep ^BASE_URL .env > nginx/www/assets/.env

if [ "x$MY_IOT_ENV" != "xprod" ]; then
    echo "Error: MY_IOT_ENV for prod environment MUST be set to 'prod'";
    exit 100;
fi

# docker-compose >= 1.29
COMMAND="docker compose -p $MY_IOT_PROJECT --profile=chat -f compose.yaml"
# else docker-compose < 1.29
# COMMAND="docker compose -p $MY_IOT_PROJECT -f compose.yaml"
COMMAND="$COMMAND -f compose-prod.yaml"

./managez_final_exec.sh "$COMMAND" $@
