from machine import Pin
import time
import config

class Button:
    def __init__(self, pin, tol = 500):
        self.DEBOUNCE_TOL = 500
        self.current_state = 0
        self.last_press = 0
        self.button = Pin(config.BUTTON_PIN, Pin.IN)
        print("Loading button")
        self.button.irq(trigger=Pin.IRQ_FALLING, handler = self.update_state)

# Call this function on any button press
    def update_state(self, p):
        # The current time in nanoseconds
        current_time = time.time_ns()/(10**6)
        if (current_time - self.last_press <= self.DEBOUNCE_TOL):
            return
        self.current_state = self.current_state + 1
        if self.current_state > config.MAX_STATE:
            self.current_state = 0
        # Add debug print
        print(f'The current state is {self.current_state}')
        self.last_press =  time.time_ns()/(10**6)

