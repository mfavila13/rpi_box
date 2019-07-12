import RPi.GPIO as gpio
from time import sleep
class Shifter():
    outputA=4
    outputB=17
    s_clock=27
    s_clearPin=22
    clockmon = 5
    def __init__(self):
        self.setupBoard()
        self.pause=0
    def tick(self):
	gpio.output(Shifter.s_clock,gpio.HIGH)
	sleep(self.pause)
	gpio.output(Shifter.s_clock,gpio.LOW)
	sleep(self.pause)
    def checkValue(self):
        for j in range(24):
            #output to output B
            #read data lines when clock is high
	    bitwise = 0x800000>>j
	    bitVal = bitwise
	    if (bitVal ==0):
	        gpio.output(Shifter.outputB,gpio.LOW)
	    else:
		gpio.output(Shifter.outputB,gpio.HIGH)
	Shifter.tick(self)
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
        gpio.setup(Shifter.s_clock,gpio.OUT)
        gpio.output(Shifter.s_clock,gpio.LOW)
        gpio.setup(Shifter.s_clearPin,gpio.OUT)
        gpio.output(Shifter.s_clearPin,gpio.HIGH)
        gpio.setup(Shifter.clockmon,gpio.IN)
def main():
    pause=0.5
    gpio.setmode(gpio.BCM)
    shifter=Shifter()
    running=True
    while running==True:
        try:
            shifter.checkValue()
            check = gpio.input(5)
	    print(check)
        except KeyboardInterrupt:
            running=False


if __name__=="__main__":
    main()
