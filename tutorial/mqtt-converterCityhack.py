import paho.mqtt.client as mqtt
import json
from random import randint
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.output(3,GPIO.HIGH)
GPIO.output(4,GPIO.HIGH)
GPIO.output(17,GPIO.HIGH)
time.sleep(1)
GPIO.output(3,GPIO.LOW)
GPIO.output(4,GPIO.LOW)
GPIO.output(17,GPIO.LOW)
time.sleep(1)
#brokers IPS
MQTT_URL         = "fd00::1"

MQTT_TOPIC_EVENT = "zolertia/evt/status"

# The callback upon connecting successfully
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC_EVENT)
    print("Subscribed to " + MQTT_TOPIC_EVENT )

# The callback when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if msg.topic== MQTT_TOPIC_EVENT:
        print("new reading")
        GPIO.output(3,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(3,GPIO.LOW)
        GPIO.output(4,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(4,GPIO.LOW)
        #client2.publish(MQTT_TOPIC_CLOUDSENDER,str(msg.payload)[2:-1])
        y = json.loads(str(msg.payload)[2:-1])
        if int(y['SeqNo'])==1:
            GPIO.output(17,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(17,GPIO.LOW)
            print("new Node")
            print("new treshold request "+"zolertia/"+y['mac'])
            
            client.publish("zolertia/"+y['mac'],str(randint(1,2)))
    
###################################################################################
###################################################################################


###################################################################################
###################################################################################

# Create the MQTT connection object
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect and loop forever
print("connecting to " + MQTT_URL)
client.connect(MQTT_URL, 1883, 60)
client.loop_forever()


GPIO.clean()
