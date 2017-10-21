import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
        input_state = GPIO.input(18)
        if input_state == False:
                print('Button Pressed')
                broadcastEvent("buttonPressed")
                time.sleep(1) # wait a second before we listen for more button presses





def broadcastEvent(eventName):
    mqttc = mqtt.Client("buttonMachine")
    #mqttc.connect("10.0.0.1", 1883)
    mqttc.connect("localhost", 1883)
    # don't retain messages, this needs to be more real -time
    mqttc.publish("events/button", payload=str(eventName),qos=0,retain=False) 
    mqttc.loop(2) #timeout = 2s

