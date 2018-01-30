#!/bin/sh


if grep rl typescript
then
	echo "yup , I got the loccation request"
	location=$(sudo hologram modem location) && sudo hologram send "$location" -t "LR"
	echo "sent location back to user"
else
	echo "nope"
fi
