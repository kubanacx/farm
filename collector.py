import paho.mqtt.publish as publish
import json
import time


while True:
    print('Collecting and sending data...')

    d = {'tem': 25, 'hum': 13, 'ph': 6.0, 'ovf': False, 'dyl': True, 'prx': False}
    payload = json.dumps(d)
    publish.single("test", payload, hostname="localhost")
    time.sleep(0.1)
