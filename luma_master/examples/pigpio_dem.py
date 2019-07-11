import pigpio
from explorehat import plugins
#from shiftregister import ShiftRegister

pi = pigpio.pi()

a_pin = 5
b_pin = 6
clr_pin = 13
clk_pin = 26

sr = plugins.ShiftRegister(pi, a_pin, b_pin, clr_pin, clk_pin)

#sr.update(0b10101010) # Register outputs 10101010

#sr.clear() # Register outputs 00000000

sr.toggle_pin(0) # Register outputs 00000001

#sr.toggle(7) # Register outputs 10000001

#sr.write(7, 0) # Register outputs 00000001

#sr.write(4, 1) # Register outputs 00010001