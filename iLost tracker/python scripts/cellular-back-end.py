#!/usr/bin/env python

from Hologram.HologramCloud import HologramCloud
from time import sleep
import sys
import time
import serial
import pynmea2


RESPOND_WITH = 'e'

# This function will return with the cellular position, received from the Nova
def getCoordinates():
    latitude = hologram.network.location.latitude
    longitude = hologram.network.location.longitude
    return latitude, longitude


def gotSMS():
    global RESPOND_WITH
    sms = hologram.popReceivedSMS()
    if sms is not None:
        RESPOND_WITH = sms.message
        print sms
        return True
    else:
        return False

def main():

    if not hologram.network.is_connected():
            result = hologram.network.connect()
            if result == False:
                print 'Failed to connect to cell network'
            else:
                print 'Connected to cell network'

        elif gotSMS():
          
            latitude, longitude = getCoordinates()
            origin = 'Cellular'
            
            # 's' is indicating that the response needs to be an SMS
            
            if RESPOND_WITH[0] == 's':
                response = origin + ' coordinates of your bike: https://maps.google.com/maps?q=' + str(latitude) + ',' + str(longitude)
                topic = 'sms'
            # Otherwise the response needs to be an SMS.
            # In the future the default behavior might change so
            # let's stick with 'e' means reponse needs to be and e-mail
            # and the default behavior is the same
            else:
                response = '{"latitude":"' + str(latitude) + '","longitude":"' + str(longitude) + '","origin":"'+ origin +'"}'
                topic = 'email'

            print 'Response: ' + response
            # Sending the data to the Hologram Cloud. It will do the
            # necessary routing, data handling
            response_code = hologram.sendMessage(response, topic)
            if 'Message sent successfully' == hologram.getResultString(response_code):
                print 'Message sent successfully'
            else:
                print 'Failed to send message'
   