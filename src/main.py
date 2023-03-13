# main.py

from button import Button
from servo import Servo
from color import Color
from ultrasonic import Ultrasonic
from motorcontroller import MotorController
from HCSR04 import HCSR04
from Controllers import BangBangController, PIDController
import config
import time
import neopixel
import machine
import _thread

def test_run(motors, servo):
    motors.set_right(500)
    motors.set_left(500)
    servo.set(-90)
    time.sleep(1)
    servo.set(90)
    motors.set_right(-500)
    motors.set_left(-500)
    time.sleep(1)
    motors.set_right(0)
    motors.set_left(0)

# sampling_rate: the rate to sample in Hz (s^-1)
def ultrasonic_thread(ult, sampling_rate = 10):
    while(True):
        config.current_dist = ult.distance_cm()
        time.sleep_ms(int(1000/sampling_rate))

def controller_thread(controller, sampling_rate = 10):
    while(True):
        controller.set_target(config.target_dist, config.current_dist)
        time.sleep_ms(int(1000/sampling_rate))


led_1 = neopixel.NeoPixel(machine.Pin(config.LED_PIN), 1)
ult_1 = HCSR04(config.TRIG_PIN, config.ECHO_PIN)
motors = MotorController(config.STBY, config.PWM_A,config.A_IN, config.PWM_B, config.B_IN)
button_1 = Button(config.BUTTON_PIN)
servo_1 = Servo(config.SERVO_PIN)
pid_controller = PIDController(motors, 1023/4, 0, 0)

# Setup threading for the ultrasonic sensor to consistently update the distance over time
ult_thread = _thread.start_new_thread(ultrasonic_thread, (ult_1, 10))
controller_thread = _thread.start_new_thread(controller_thread, (pid_controller, 10))

# test_run(motors, servo_1)
# TODO(morleyd): Multithreading (for use with ultrasonic sensor)
# Web Server: https://github.com/jczic/MicroWebSrv
# -> For controlling over http requests
#  https://bytesnbits.co.uk/multi-thread-coding-on-the-raspberry-pi-pico-in-micropython/
