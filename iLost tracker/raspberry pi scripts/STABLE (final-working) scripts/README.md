# Raspberry pi scripts - LONG-RANGE-CAPABILITY

# INSTALLATION INSTRUCTIONS

### update the raspberry pi

* turn on the raspberry pi  

* connect the raspberry pi to the internet

* type & enter: sudo apt-get update

* type & enter: sudo apt-get upgrade

* type & enter: curl -L hologram.io/python-install | bash

* type & enter: curl -L hologram.io/python-update | bash       


### upload the ilost scripts onto the raspberry pi

* go to ilost tracker\raspberry pi scripts\STABLE (final-working) scripts\ on the back-end github repo

* download the scripts: send_location.sh, ilost-start-server.sh & hologram_receive_1

* place these three scripts in the /home/pi  directory in the raspberry pi

* make sure to chmod u+x in terminal for each script (give permission for it to run properly)


### get everything running & automatic

* open terminal & type & enter: crontab -e

* choose nano (its very simple)

* get rid of any scripts that are already there, otherwise ignore this step

* type: @reboot /home/pi/ilost-start-server.sh &
		@reboot /home/pi/send_location.sh &

* press: ctrl-x, press: y, press: enter

* now reboot or shutdown the raspberry pi. it should now work.

### any issues please contact marian or hussein


