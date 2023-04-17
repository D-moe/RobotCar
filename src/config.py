# All global vars, etc go here
BUTTON_PIN = 2
# TODO(morleyd): standardize this pin.
SERVO_PIN = 17 # Maps to 10? Double check pin 10
LED_PIN = 4
MAX_STATE = 5


TRIG_PIN = 13

ECHO_PIN = 12

PWM_A = 5
PWM_B = 18 # Maps to 6
A_IN = 32 # Maps to 8
B_IN = 33 # Maps to 7
STBY = 25 # Maps to 3

# Line Sensor
# Relevant Datasheet:
# https://cdn-shop.adafruit.com/product-files/3930/ITR20001-T.pdf
LINE_A = 26 # Maps to A0
LINE_B = 14 # Maps to A1
LINE_C = 27 # Maps to A2

IR_PIN = 22 # Maps to 9
SDA = 21 # Maps to Arduino SDA pin
SCL = 22 # Maps to Arduino SCL pin

# The amount of
# 00
current_state = 0 # Default state
last_press = 0 # Store the time of the last_pressx
# The value currently being measured by the ultrasonic, updated in a separate thread.x
current_dist = 0.0
target_dist = 25.0