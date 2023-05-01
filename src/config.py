# All global vars, etc go here
BUTTON_PIN = 35 # Maps to 2
SERVO_PIN =  12 # Maps to 10
LED_PIN = 32 # Maps to 4
MAX_STATE = 5
# 39, 32, 33, 34, 35, 36 are pins that can be used for ADC
# and are on ADC1

#  ADC1 for 36, 39, 34
TRIG_PIN = 18 # Maps to 13

ECHO_PIN = 13 # Maps to 12

PWM_A = 33 # Maps to 5
PWM_B = 25 # Maps to 6
B_IN = 27 # Maps to 8
A_IN = 26 # Maps to 7
# TODO(morleyd): Add in the standby pin.
STBY = 17 # Maps to 3

# Line Sensor
# Relevant Datasheet:
# https://cdn-shop.adafruit.com/product-files/3930/ITR20001-T.pdf
LINE_A = 36 # Maps to A0x
LINE_B = 39 # Maps to A1
LINE_C = 34 # Maps to A2

IR_PIN = 14 # Maps to 9

# Serial pin for communicating with ESP-CAM
TX = 16
RX = 17


current_state = 0 # Default state
last_press = 0 # Store the time of the last_pressx
# The value currently being measured by the ultrasonic, updated in a separate thread.x
current_dist = 0.0
target_dist = 25.0