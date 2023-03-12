from machine import PWM, Pin
import math

# Simple servo class, a pwm pulse controls what position the servo moves to.
# The servo we are using is the SG90 Servo Motor which has 0-180 rotation
# For this servo the duty cycle can be anywhere from 1-2 ms with a PWM
# period of 20 ms, 50 Hz
# The duty cycle ranges from 0 - 1023 or 0 - 100%, so [1/20, 1/10] * 1023 = [51.15, 102.30]

# In practice a duty cycle of [25, 127] seems to get the full range
class Servo:
    def __init__(self, pin, freq = 50, min_duty = 25, max_duty = 127):
        self.freq = freq
        self.min_duty = min_duty
        self.max_duty = max_duty
        self.pwm = PWM(Pin(pin), freq, duty = 0)
    # The angle (in degrees) to set the servo to.
    # We offset our range of angles so 0 degrees is forward, so our range is [-90, 90]
    def set(self, angle):
        angle = angle + 90
        # We now linearly interpolate between our range of duty cycles
        duty = self.min_duty + angle*(self.max_duty - self.min_duty)/180
        self.pwm.duty(int(duty))