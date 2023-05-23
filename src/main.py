# main.py

import network
from button import Button
from servo import Servo
from color import Color
from ultrasonic import Ultrasonic
from motorcontroller import MotorController
from HCSR04 import HCSR04
from Controllers import BangBangController, PIDController
from linefollower import LineFollower
from week5 import Week5
import config
import time
import neopixel
import machine
import _thread

def controller_thread(controller, sampling_rate=10):
    while (True):
        controller.set_target(config.target_dist, config.current_dist)
        time.sleep_ms(int(1000/sampling_rate))


def load_wifi():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('network-name')


print('this ran')
button_1 = Button(config.BUTTON_PIN)
# Emergency abort to prevent loop on issue.
# if not button_1.button.value():
#    print("Main skip button activated")

led_1 = neopixel.NeoPixel(machine.Pin(config.LED_PIN), 1)
ult_1 = HCSR04(config.TRIG_PIN, config.ECHO_PIN)
motors_1 = MotorController(config.STBY, config.PWM_B,
                         config.B_IN, config.PWM_A, config.A_IN)
servo_1 = Servo(config.SERVO_PIN)
line_follow_1 = LineFollower(config.LINE_A, config.LINE_B, config.LINE_C)
pid_controller = PIDController(motors_1, 1023/4, 0, 0)
# Set the motors to off to start
motors_1.set_right(0)
motors_1.set_left(0)

def test_run():
    motors = motors_1
    servo = servo_1
    ult = ult_1
    lf = line_follow_1
    led = led_1
    led[0] = (255, 0, 0)
    led.write()
    motors.set_right(300)
    motors.set_left(300)
    servo.set(-45)
    time.sleep(1)
    led[0] = (0, 255, 0)
    led.write()
    servo.set(45)
    motors.set_right(-300)
    motors.set_left(-300)
    time.sleep(1)
    led[0] = (0, 0, 255)
    led.write()
    motors.set_right(0)
    motors.set_left(0)
    time.sleep(1)
    led[0] = (0, 0, 0)
    led.write()
    current_dist = ult.distance_cm()
    print(f'The measured dist is {current_dist}.')
    lf.read_pins()
    print(f'The current line follow values are {lf.vals}')

# Setup threading for the ultrasonic sensor to consistently update the distance over time
print("just booted")

week5= Week5(led_1, ult_1, motors_1, servo_1)

# Can change this to a while, to make your code run continously!
while (config.current_state == 0):
    week5.run()

# ult_thread = _thread.start_new_thread(ultrasonic_thread, (ult_1, 10))
# controller_thread = _thread.start_new_thread(controller_thread, (pid_controller, 10))
# test_run(motors, servo_1)
# TODO(morleyd): Multithreading (for use with ultrasonic sensor)
# Web Server: https://github.com/jczic/MicroWebSrv
# -> For controlling over http requests
#  https://bytesnbits.co.uk/multi-thread-coding-on-the-raspberry-pi-pico-in-micropython/
