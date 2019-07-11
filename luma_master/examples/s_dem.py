import RPi.GPIO as gpio
from time import sleep
import wiringpi
class Shifter():
    outputA=4
    outputB=17
    s_clock=27
    s_clearPin=22
    def __init__(self):
        self.setupBoard()
        self.pause=0
    def checkValue(self):
        for j in range(24):
            #output to output B
            #read data lines when clock is high
            bitVal = wiringpi.shiftIn(s_clock,0)
            print(bitVal)
        #Shifter.tick(self)
    def clear(self):
        gpio.output(Shifter.s_clearPin,gpio.LOW)
        Shifter.tick(self)
        gpio.output(Shifter.s_clearPin,gpio.HIGH)
    def setupBoard(self):
        gpio.setup(Shifter.outputA,gpio.OUT)
        gpio.output(Shifter.outputA,gpio.HIGH)
        gpio.setup(Shifter.outputB,gpio.OUT)
        gpio.output(Shifter.outputB,gpio.LOW)
        gpio.setup(Shifter.s_clock,gpio.IN)
        gpio.output(Shifter.s_clock,gpio.LOW)
        gpio.setup(Shifter.s_clearPin,gpio.IN)
        gpio.output(Shifter.s_clearPin,gpio.HIGH)

    def main():
        pause=0.5
        gpio.setmode(gpio.BCM)
        shifter=Shifter()
        running=True
        while running==True:
            try:
                checkValue()
            except KeyboardInterrupt:
                running=False


if __name__=="__main__":
    main()
