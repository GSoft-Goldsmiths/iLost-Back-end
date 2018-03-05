#!/bin/sh
while :


if grep off typescript
then
	echo "switching off the tracker"
	sudo hologram modem disconnect
	>typescript
	echo "tracker is off"
else
	echo "..."
	sleep 10s
fi

done