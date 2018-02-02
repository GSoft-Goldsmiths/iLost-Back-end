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

else if grep off typescript
then
	echo "switching off the tracker"
	sudo hologram modem disconnect
	>typescript
	echo "tracker is off"
else
	echo "..."
	sleep 10s
fi

else if grep on typescript
then
	echo "switching on the tracker"
	sudo hologram modem connect
	>typescript
	echo "tracker is on"
else
	echo "..."
	sleep 10s
fi

done
