import config
import time
class BangBangController:
    def __init__(self, motors):
        self.motors = motors
    def set_target(self, dist):
        speed = 1023/2
        if (dist > config.current_dist):
            self.motors.set_right(-speed)
            self.motors.set_left(-speed)
        else:
            self.motors.set_right(speed)
            self.motors.set_left(speed)

class PIDController:
    def __init__(self, motors, p, i, d):
        # max error is 200, go full speed when 50cm from target
        # p = .25
        self.motors = motors
        self.p = p
        self.i = i
        self.d = d
        self.sum_e = 0
        # In seconds
        self.last_sample = time.time()
        self.last_error = 0
        self.gain = 0
        self.error = 0
        self.curr_dist = 0

    def reset(self):
        self.sum_e = 0
        self.last_sample = time.time()
    def set_p(self, p):
        self.reset()
        self.p = p
    def set_i(self, i):
        self.reset()
        self.i = i
    def set_d(self, d):
        self.reset()
        self.d = d
    def bound_gain(self, gain):
        if gain> 1023:
            gain = 1023
        elif gain < -1023:
            gain = -1023
        gain = int(gain)
        return gain
    def set_target(self, target_dist, current_dist):
        self.error = target_dist - current_dist
        self.curr_dist = current_dist
        curr_sample = time.time()

        self.gain = self.p * self.error + self.i * self.sum_e + self.d * (self.error - self.last_error)/max(curr_sample - self.last_sample, 0.000001)
        self.gain = self.bound_gain(self.gain)
        self.motors.set_right(self.gain)
        self.motors.set_left(self.gain)

        # Update state for next iteration
        self.sum_e += self.error
        self.last_sample = curr_sample
        self.last_error = self.error

