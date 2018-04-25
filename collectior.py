import paho.mqtt.publish as publish
import json
import time


while True:
    print('Collecting and sending data...')
    d = {'tem': 25, 'hum': 13, 'ph': 1}
    payload = json.dumps(d)
    publish.single("test", payload, hostname="localhost")
    time.sleep(1)
