import RPi.GPIO as gpio
from time import sleep

class Shifter():

    #inputA=15
    SHCPclock=6 #SHCP 8-stage shift register pin 11 clockpin
    DSinput=26  #DS Serial Data input.
    STCP=19 #STCP 8-bit storage register pin 12  register clock = latch
    #clearPin=6 #latch MR pin 10

    MR=5 #master reset  SRCLR


    def __init__(self):
        self.setupBoard()
        self.pause=0

    def tick(self):
        gpio.output(Shifter.SHCPclock,gpio.HIGH)
        sleep(self.pause)
        gpio.output(Shifter.SHCPclock,gpio.LOW)
        sleep(self.pause)

    def setValue(self,value):
        print "Setting value", value
        for i in range(24):
            bitwise=0x800000>>i
            bit=bitwise&value
            if (bit==0):
                gpio.output(Shifter.DSinput,gpio.LOW)
            else:
                gpio.output(Shifter.DSinput,gpio.HIGH)
            Shifter.tick(self)
        gpio.output(Shifter.STCP, gpio.HIGH)

    def clear(self):
        gpio.output(Shifter.MR,gpio.LOW)
        Shifter.tick(self)
        gpio.output(Shifter.MR,gpio.HIGH)

    def setupBoard(self):

        gpio.setmode(gpio.BCM)

        #gpio.setup(Shifter.inputA,gpio.OUT)
        #gpio.output(Shifter.inputA,gpio.HIGH)

        gpio.setup(Shifter.DSinput,gpio.OUT)
        gpio.output(Shifter.DSinput,gpio.LOW)

        gpio.setup(Shifter.SHCPclock,gpio.OUT)
        gpio.output(Shifter.SHCPclock,gpio.LOW)

        gpio.setup(Shifter.STCP,gpio.OUT)
        gpio.output(Shifter.STCP,gpio.LOW)
        
        gpio.setup(Shifter.MR,gpio.OUT)
        gpio.output(Shifter.MR,gpio.HIGH)


# def main():
#     pause=0.5
#     #gpio.setmode(gpio.BOARD)
#     shifter=Shifter()
#     running=True
#     while running==True:
#         try:
#         #shifter.clear()
#         #shifter.setValue(1)
#         #sleep(1)
#             shifter.clear()
#             #shifter.setValue(0x0AAAAAA)
#             sleep(pause)
#             #shifter.clear()
#             shifter.setValue(0x0555555)
#             sleep(pause)
#         except KeyboardInterrupt:
#             running=False
#
# if __name__ == '__main__':
# 	main()
