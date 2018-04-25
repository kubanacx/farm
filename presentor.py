import paho.mqtt.client as mqtt
import json
from datetime import datetime

def on_message(mqttc, obj, msg):
    payload = json.loads(msg.payload.decode('utf-8'))
    print(payload, datetime.now().time().replace(microsecond = 0))

# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client()
mqttc.on_message = on_message
# Uncomment to enable debug messages
# mqttc.on_log = on_log
mqttc.connect("localhost", 1883, 60)
mqttc.subscribe("test", 0)

mqttc.loop_forever()
