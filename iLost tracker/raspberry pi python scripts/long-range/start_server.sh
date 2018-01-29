#!/bin/bash

#location=$(sudo hologram modem location) && sudo hologram send "$location"

while true;

	sudo hologram recieve >> log.txt
	sleep 60s;

done 