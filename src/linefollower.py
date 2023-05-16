from machine import Pin, ADC

class LineFollower():
    def __init__(self, right, mid, left):
        self.right = ADC(Pin(right))
        self.right.atten(ADC.ATTN_11DB)
        self.mid = ADC(Pin(mid))
        self.mid.atten(ADC.ATTN_11DB)
        self.left = ADC(Pin(left))
        self.left.atten(ADC.ATTN_11DB)
        self.vals = []
    def read_pins(self):
        self.vals = [self.right.read(), self.mid.read(), self.left.read()]

