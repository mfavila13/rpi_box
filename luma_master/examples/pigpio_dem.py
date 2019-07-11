import pigpio
from shiftregister import ShiftRegister

pi = pigpio.pi()

a_pin = 19
b_pin = 26
clr_pin = 20
clk_pin = 21

sr = ShiftRegister(pi, a_pin, b_pin, clr_pin, clk_pin)

sr.update(0b10101010) # Register outputs 10101010

sr.clear() # Register outputs 00000000

sr.toggle(0) # Register outputs 00000001

sr.toggle(7) # Register outputs 10000001

sr.write(7, 0) # Register outputs 00000001

sr.write(4, 1) # Register outputs 00010001