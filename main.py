import sys
import math
import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep
from hx711 import HX711
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo = Servo(12, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)


def dump_food():
    print("dumping food")
    servo.mid()
    sleep(2)
    servo.min()
    sleep(2)
    servo.max()
    print("that now it should stop")
    #this should sweep back and forth. Not tested on the servo
    while True:
    for i in range(0, 360):
        servo.value = math.sin(math.radians(i))
        sleep(0.01)

def cleanAndExit():
    print("Cleaning...")
        
    print("Bye!")
    sys.exit()

hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")

food_bar = 5

referenceUnit = 407
hx.set_reference_unit(referenceUnit)

hx.reset()
hx.tare()
print("Tare done! Add weight now...")

while True:
    try:
        val = hx.get_weight(5)
        print(val)

        hx.power_down()
        hx.power_up()
        sleep(0.1)
        if val < food_bar:
            sleep(5)
            val = hx.get_weight(5)
            if val < food_bar:
                dump_food()


    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
