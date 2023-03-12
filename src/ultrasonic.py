from machine import Pin, Timer
import time
# Given ultrasonic is the HC-SR04
# We reference the following datasheet:
# https://www.electroschematics.com/wp-content/uploads/2013/07/HC-SR04-datasheet-version-2.pdf

# Sample period of 50 ms (to give enough time for pulses to be sent and echoed back).
# f = 1 / period = 1 / 50 * 1000 = 20Hz
# Period of 50 ms want 10 \mu s to be on so duty of .01 ms or .01/50 * 1024 = 0.2048

# Unfortunately unable to pulse PWM at that granularity so we will have to use a very small
# delay (small enough that negligible compared to event loop time)

# We need to choose a timer to schedule our pulses with, default to the last of the 4 timers
class Ultrasonic:
    def __init__(self, trig, echo, timer = 6):
        # The maximum distance the sensor can read (value returned on timeout):
        self.MAX_DIST = 197 # In inches
        self.trig = Pin(trig, Pin.OUT)
        self.echo = Pin(echo, Pin.IN)
        self.timer = Timer(timer)
        self.recv_time = 0
        self.end_recv_time = 0
        # Distance is measure in inches
        self.dist = self.MAX_DIST
        self.timer.init(mode = Timer.PERIODIC, freq = 10, callback = self.pulse)
      #  self.echo.irq(trigger = Pin.IRQ_RISING, handler = self.lock_time)
        self.echo.irq(trigger = Pin.IRQ_FALLING|Pin.IRQ_RISING, handler = self.compute_dist)

    # Send out a pulse on the trigger pin to get a measurement for the distance.
    # Schedule this function with a callback to ensure that it gets called repeatedly.
    def pulse(self, e):
        # print('Calling pulse')
        self.trig.value(0)
        time.sleep_us(5)
        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)
        self.recv_time = time.time_ns()

    def compute_dist(self, e):
        self.end_recv_time = time.time_ns()
        self.dist = max(self.MAX_DIST, (self.end_recv_time - self.recv_time) / (1000 * 148))