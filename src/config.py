# All global vars, etc go here
BUTTON_PIN = 2
# TODO(morleyd): standardize this pin.
SERVO_PIN = 17 # Maps to 1
LED_PIN = 4
MAX_STATE = 5


TRIG_PIN = 13

ECHO_PIN = 12

PWM_A = 5
PWM_B = 18 # Maps to 6
A_IN = 32 # Maps to 8
B_IN = 33 # Maps to 7
STBY = 25 # Maps to 3

# The amount of
# 00
current_state = 0 # Default state
last_press = 0 # Store the time of the last_pressx
# The value currently being measured by the ultrasonic, updated in a separate thread.x
current_dist = 0.0
target_dist = 25.0