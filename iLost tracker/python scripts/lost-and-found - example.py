#!/usr/bin/env python

# https://www.hackster.io/Abysmal/find-my-bike-082ebb

from Hologram.HologramCloud import HologramCloud
from time import sleep
import sys
import time
import serial
import pynmea2

__author__ = "Balazs Simon"
__license__ = "GPL"
__version__ = "1.0.0"
__details__ = "https://www.hackster.io/Abysmal/lost-and-found-082ebb"

RESPOND_WITH = 'e'

# This function will return with the cellular position, received from the Nova
def getCoordinates():
    latitude = hologram.network.location.latitude
    longitude = hologram.network.location.longitude
    return latitude, longitude

# This function will return True is the Nova is received and SMS and
# it will also print it to the console. Otherwise it will return False
# RESPOND_WITH will contain the message of the SMS to determine whether
# it should answer with in SMS or e-mail and with cellular or GPS position
def gotSMS():
    global RESPOND_WITH
    sms = hologram.popReceivedSMS()
    if sms is not None:
        RESPOND_WITH = sms.message
        print sms
        return True
    else:
        return False

if __name__ == '__main__':
    hologram = HologramCloud(dict(), network='cellular')
    # The default baudrate of the Ublox Neo 7M GPS module is 9600
    # You have to enable UART to use serial. My project contains 
    # information about it
    ser = serial.Serial(
        port='/dev/serial0',
        baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
    # These variables are used to store the last valid GPS position.
    # They can be used when the GPS can't get a fix but you have 
    # cellular connection
    gpsLatitude = 0.0
    gpsLongitude = 0.0
    while True:
        x=ser.readline()
        # GPGGA sentences contain the position data. The other 
        # sentences are irrelevant
        if x[:6] == "$GPGGA":
            position = pynmea2.parse(x)
            print position
            # If the GPS can't get a fix then the parsing's result 
            # is 0.0 for both longitude and latitude. This is how
            # the program knows that it lost the GPS signal and it
            # should use the stored last known position
            if position.longitude != 0.0 and position.latitude != 0.0:
                gpsLatitude = position.latitude
                gpsLongitude = position.longitude
        if not hologram.network.is_connected():
            result = hologram.network.connect()
            if result == False:
                print 'Failed to connect to cell network'
            else:
                print 'Connected to cell network'
        elif gotSMS():
            # 'g' is indicating that the requested data is the GPS 
            # position. If no GPS position is found at all then we
            # respond with the cellular position
            if RESPOND_WITH[1] == 'g' and gpsLatitude != 0.0:
                latitude, longitude = gpsLatitude, gpsLongitude
                origin = 'GPS'
            # Otherwise the requested data is the cellular position. 
            # In the future the default behavior might change so
            # let's stick with 'c' means cellular position here and
            # the default is the same
            else:
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
