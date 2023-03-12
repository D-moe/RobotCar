# main.py

from button import Button
from servo import Servo
from color import Color
from ultrasonic import Ultrasonic
from motorcontroller import MotorController
from HCSR04 import HCSR04
import config
import time
import neopixel
import machine

led_1 = neopixel.NeoPixel(machine.Pin(config.LED_PIN), 1)
# This non-interrupt implementation seems to work, we'll have
# to investigate why our original implementation was not working properly.
ult_1 = HCSR04(config.TRIG_PIN, config.ECHO_PIN)
motors = MotorController(config.STBY, config.PWM_A,config.A_IN, config.PWM_B, config.B_IN)
motors.set_right(1023)
motors.set_left(-1023)
# ult_1 = Ultrasonic(config.TRIG_PIN, config.ECHO_PIN)
color = Color()
button_1 = Button(config.BUTTON_PIN)
servo_1 = Servo(config.SERVO_PIN)
servo_1.set(-90)
time.sleep(1)
servo_1.set(90)
print(f'The dist is {ult_1.distance_cm()}')

# TODO(morleyd): Multithreading (for use with ultrasonic sensor)
# Web Server: https://github.com/jczic/MicroWebSrv
# -> For controlling over http requests
#  https://bytesnbits.co.uk/multi-thread-coding-on-the-raspberry-pi-pico-in-micropython/
