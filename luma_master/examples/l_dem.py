import RPi.GPIO as gpio
from time import sleep

class Shifter():

	inputA=5
	inputB=6
	clock=13
	clearPin=26

	def __init__(self):
		self.setupBoard()
		self.pause=0
	def tick(self):
		gpio.output(Shifter.clock,gpio.HIGH)
		sleep(self.pause)
		gpio.output(Shifter.clock,gpio.LOW)
		sleep(self.pause)

	def setValue(self,value):
		for i in range(24):
	            bitwise=0x800000>>i
        	    print(i)
	            bit=bitwise&value
		    if (bit==0):
		        gpio.output(Shifter.inputB,gpio.LOW)
  	            else:
		        gpio.output(Shifter.inputB,gpio.HIGH)
     		    #if i == 6:
		#	gpio.output(Shifter.inputB.gpio.HIGH)
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

def main():
	pause=1
	gpio.setmode(gpio.BCM)
	shifter=Shifter()
	running=True
	while running==True:
        	try:
			#shifter.clear()
			#shifter.setValue(1)
			#sleep(1)
			shifter.clear()
			shifter.setValue(0b000000000011111111111111)
			sleep(pause)
			#shifter.clear()
			#shifter.setValue(0x555555)
			#sleep(pause)
	                print("loop")
	        except KeyboardInterrupt:
        		running=False


if __name__=="__main__":
    main()
