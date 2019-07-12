import RPi.GPIO as gpio
from time import sleep

class Shifter():

    inputA=4
    inputB=17
    clock=27
    clearPin=22
    outputA = 
    outputB = 
    s_clock = 
    s_clear = 
    s_check = 
    bitarray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    bitnum = 0

    def __init__(self):
	self.setupBoard()
	self.pause=0

    def tick(self):
	gpio.output(Shifter.clock,gpio.HIGH)
	sleep(self.pause)
	gpio.output(Shifter.clock,gpio.LOW)
	sleep(self.pause)

    def conv_array(self):
        Shifter.bit_num = 0
        num = 0
        for b in range(24):
            num = (Shifter.bitarray[b]*10*(b+1)) + num
        Shifter.bit_num = int(num,2)
        return bit_num
    
    def clear_switch(self):
        Shifter.bitarray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        return Shifter.bitarray
    
    def check_switch(self):
        for s in range(24):
            Shifter.clear_switch(self)
            Shifter.bitarray[s] = 1
            Shifter.conv_array(self)
            if Shifter.s_check == gpio.HIGH:
                return Shifter.bitarray
            
    def setValue(self,value):
	for i in range(24):
            bitwise=0x800000>>i
       	    print(i)
            bit=bitwise&value
	    if (bit==0):
	        gpio.output(Shifter.inputB,gpio.LOW)
            else:
	        gpio.output(Shifter.inputB,gpio.HIGH)
	    Shifter.tick(self)

    def clear(self):
	gpio.output(Shifter.clearPin,gpio.LOW)
	Shifter.tick(self)
	gpio.output(Shifter.clearPin,gpio.HIGH)

    def setupBoard(self):
	gpio.setup(Shifter.inputA,gpio.OUT)
	gpio.output(Shifter.inputA,gpio.HIGH)
	gpio.setup(Shifter.inputB,gpio.OUT)
	gpio.output(Shifter.inputB,gpio.LOW)
	gpio.setup(Shifter.clock,gpio.OUT)
	gpio.output(Shifter.clock,gpio.LOW)
	gpio.setup(Shifter.clearPin,gpio.OUT)
	gpio.output(Shifter.clearPin,gpio.HIGH)
        gpio.setup(Shifter.outputA,gpio.OUT)
	gpio.output(Shifter.outputA,gpio.HIGH)
	gpio.setup(Shifter.outputB,gpio.OUT)
	gpio.output(Shifter.outputB,gpio.LOW)
	gpio.setup(Shifter.s_clock,gpio.OUT)
	gpio.output(Shifter.s_clock,gpio.LOW)
	gpio.setup(Shifter.s_clear,gpio.OUT)
	gpio.output(Shifter.clear,gpio.HIGH)
        gpio.setup(Shifter.s_check,gpio.IN)
        
    def snake(self,size)
        Shifter.clear_switch(self)
        for s in range(24+int(size):
            if s < 24:
                Shifter.bitarray(s) = 1
            if s >= size:
                Shifter.bitarray(s-size) = 0
            Shifter.conv_array()
            Shifter.setValue(self,shifter.bit_num)
            sleep(1)
def main():
    pause=1
    gpio.setmode(gpio.BCM)
    shifter=Shifter()
    running=True
    while running==True:
       	try:
            shifter.check_switch()
            shifter.conv_array()
            shifter.setValue(shifter.bit_num)
            sleep(2)
            shifter.clear()
	    #shifter.clear()
    	    #shifter.setValue(1)
	    #sleep(1)
	    #shifter.clear()
	    #shifter.setValue(0b000000000011111111111111)
	    #sleep(pause)
            #shifter.clear()
	    #shifter.setValue(0x555555)
	    #sleep(pause)
            print("loop")
	except KeyboardInterrupt:
	    running=False


if __name__=="__main__":
    main()
