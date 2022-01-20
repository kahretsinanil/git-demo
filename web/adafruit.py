import sys
from Adafruit_IO import *
from Adafruit_IO import MQTTClient

from flask import Flask

from threading import Timer
import time




FEED_ID = 'foo11'

print("PYTHON CODE")

def func1(input_loc):
    print("latval:"+input_loc)


def connected(client):
    client.subscribe(FEED_ID)

def subscribe(client, userdata, mid, granted_qos):
    print('Subscribed to {0} with QoS {1}'.format(FEED_ID, granted_qos[0]))

def disconnected(client):
    sys.exit(1)


def message(client, feed_id, payload):
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    sep_payload=payload.split(",")
    print(sep_payload)
    print(type(sep_payload))
    global lat
    lat=sep_payload[0]
    print(lat)
    print(type(lat))
    long=sep_payload[1]
    print(long)
    print(type(long))
    func1(lat)



client = MQTTClient('kahretsinanil', 'aio_bWGC18fdnPysgYDnoxFDHjpLHNoj', secure=False)


client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.on_subscribe  = subscribe

client.connect()

client.loop_blocking()
