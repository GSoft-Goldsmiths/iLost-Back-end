#!/bin/bash

#location=$(sudo hologram modem location) && sudo hologram send "$location"

while true;

	sudo hologram recieve >> log.txt
	sleep 5s;

done 




PATTERN=$1
FILE=$2

if grep -q $PATTERN $FILE;
 then
     echo "Here are the Strings with the Pattern '$PATTERN':"
     echo -e "$(grep $PATTERN $FILE)\n"
 else
     echo "Error: The Pattern '$PATTERN' was NOT Found in '$FILE'"
     echo "Exiting..."
     exit 0
fi