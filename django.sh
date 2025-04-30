#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <refresh_companies_from_tabellone|sync_mlists_to_adhoc|...>"
    exit 100
fi

./manage.sh django $@
