#!/bin/bash

source ./.env
# grep ^BASE_URL .env > nginx/www/assets/.env

case $MY_IOT_ENV in 
    "dev")
        exec ./manage_dev.sh $@;
        ;;
    "prod")
        exec ./manage_prod.sh $@;
        ;;
    *)
        echo "Error: MY_IOT_ENV MUST be defined and set to 'dev' or 'prod'";
        exit 100;
esac
