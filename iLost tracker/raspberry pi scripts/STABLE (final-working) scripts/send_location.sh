#!/bin/sh
while :

do

if grep rl typescript
then
	echo "yup , I got the location request"
	location=$(sudo hologram modem location) && sudo hologram send "$location" -t "LR"
	>typescript
	echo "sent location back to user"
else
	echo "..."
	sleep 10s
fi


done
