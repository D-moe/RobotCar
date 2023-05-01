import machine, time
from machine import Pin, PWM

def abs(val):
    if val < 0:
        return -val
    else:
        return val

class MotorController:
    def __init__(self, standby, pwm_a, a_in, pwm_b, b_in):
        self.standby = Pin(standby, mode=Pin.OUT, pull = None)
        self.pwm_a = PWM(Pin(pwm_a))
        self.pwm_a.duty(0)
        self.a_in = Pin(a_in, mode=Pin.OUT, pull = None)
        self.pwm_b = PWM(Pin(pwm_b))
        self.pwm_b.duty(0)
        self.b_in = Pin(b_in, mode=Pin.OUT, pull = None)
        # Start in standby so no movement
        self.standby.value(0)
    # val range from -1023 to 1023x
    def set(self, val, control, pwm):
          # Change the motor out of standby
        self.standby.value(1)

        reverse = val < 0
        mag = abs(val)
        if reverse:
            control.value(0)
        else:
            control.value(1)

        pwm.duty(mag)
# Set left and set right seems to be controlling direction instead
    def set_right(self, val):
        # Change the motor out of standby
        self.set(val, self.b_in, self.pwm_b)

    def set_left(self, val):
        # Change the motor out of standby
        self.set(val, self.a_in, self.pwm_a)