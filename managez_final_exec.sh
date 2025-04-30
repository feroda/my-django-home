#!/bin/bash

COMMAND=$1
shift

if [ $1 == "django" ]; then
	shift
	COMMAND="$COMMAND exec web python ./manage.py"
fi

echo "Doing $COMMAND $@";

exec $COMMAND $@
