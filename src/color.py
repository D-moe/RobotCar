# We want our state machine to show states with visually
# distinct colors, so we generate them here:
# https://mokole.com/palette.html
# teal: 0, 128, 128
# orange: 255, 165, 0
# lime: 0, 255, 0
# blue: 0, 0, 255
# deep pink: 255, 20, 147

class Color:
    def __init__(self, start=0):
        self.start = start
        self.state = self.start
        self.colors = {
            "teal": (0, 128, 128),
            "orange": (255, 165, 0),
            "lime": (0, 255, 0),
            "blue": (0, 0, 255),
            "pink": (255, 20, 147)
            }
        self.order = ["teal", "orange", "lime", "blue", "pink"]
        self.color = self.colors["blue"]

    def set_color(self, color):
        # If invalid color is given default to off
        color = self.colors.get(color, (0,0,0))
        self.color = color
    def set_state(self, state):
        # If invalid state, set back to default
        if (state > len(self.order) - 1):
            state = self.start
        self.color = self.colors[self.order[state]]
import machine
echo = machine.Pin(12)
echo.irq(handler = None)