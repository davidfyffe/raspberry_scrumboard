'''
Created on Oct 31, 2016

@author: n0206863
'''
import Switch
import shiftpi

class CathodeController(object):
    '''
    7 segment Common cathode
    '''


    def __init__(self):
        '''
        Constructor
        '''
        shiftpi.shiftRegisters(2)
        self.turnAllOff()
    
    def displayNumber(self, number):
        
        self.turnAllOff()
        
        LEFTCHAR=0
        RIGHTCHAR=8
        
        tens,units = divmod(number, 10)
        
        if number > 9:
            self.chooseDigits(tens, LEFTCHAR)
            self.chooseDigits(units, RIGHTCHAR)
        else:
            self.chooseDigits(units, LEFTCHAR)
            
        
        
    def chooseDigits(self, number, bitAddition):
        for case in Switch.switch(number):
            if case(0):
                self.digitZero(bitAddition)
                break
            if case(1):
                self.digitOne(bitAddition)
                break
            if case(2):
                self.digitTwo(bitAddition)
                break
            if case(3):
                self.digitThree(bitAddition)
                break
            if case(4):
                self.digitFour(bitAddition)
                break
            if case(5):
                self.digitFive(bitAddition)
                break
            if case(6):
                self.digitSix(bitAddition)
                break
            if case(7):
                self.digitSeven(bitAddition)
                break
            if case(8):
                self.digitEight(bitAddition)
                break
            if case(9):
                self.digitNine(bitAddition)
                break
            if case(): # default, could also just omit condition or 'if True'
                print "something else!"
                # No need to break here, it'll stop anyway
    
        
    def turnSegOn(self, pinId):
        #print "Turn on seg {}".format(pinId)
        shiftpi.digitalWrite(pinId, shiftpi.HIGH)

    def turnAllOn(self):
        # turns all shift register pins to HIGH
        shiftpi.digitalWrite(shiftpi.ALL, shiftpi.HIGH)

    def turnAllOff(self):
        # turns all shift register pins to LOW
        shiftpi.digitalWrite(shiftpi.ALL, shiftpi.LOW)
        
    def digitOne(self, shiftregister=0):
        self.turnSegOn(2+shiftregister)
        self.turnSegOn(4+shiftregister)

    def digitTwo(self, shiftregister=0):
        self.turnSegOn(0+shiftregister)
        self.turnSegOn(1+shiftregister)
        self.turnSegOn(3+shiftregister)
        self.turnSegOn(4+shiftregister)
        self.turnSegOn(5+shiftregister)
        
    def digitThree(self, shiftregister=0):
        self.turnSegOn(0+shiftregister)
        self.turnSegOn(1+shiftregister)
        self.turnSegOn(3+shiftregister)
        self.turnSegOn(5+shiftregister)
        self.turnSegOn(6+shiftregister)
        
    def digitFour(self, shiftregister=0):
        self.turnSegOn(0+shiftregister)
        self.turnSegOn(2+shiftregister)
        self.turnSegOn(3+shiftregister)
        self.turnSegOn(6+shiftregister)

    def digitFive(self, shiftregister=0):
        self.turnSegOn(1+shiftregister)
        self.turnSegOn(2+shiftregister)
        self.turnSegOn(3+shiftregister)
        self.turnSegOn(5+shiftregister)
        self.turnSegOn(6+shiftregister)

    def digitSix(self, shiftregister=0):
        self.turnSegOn(2+shiftregister)
        self.turnSegOn(3+shiftregister)
        self.turnSegOn(4+shiftregister)
        self.turnSegOn(5+shiftregister)
        self.turnSegOn(6+shiftregister)
        self.turnSegOn(7+shiftregister)
        
    def digitSeven(self, shiftregister=0):
        self.turnSegOn(0+shiftregister)
        self.turnSegOn(1+shiftregister)
        self.turnSegOn(6+shiftregister)
        
    def digitEight(self, shiftregister=0):
        self.turnSegOn(0+shiftregister)
        self.turnSegOn(1+shiftregister)
        self.turnSegOn(2+shiftregister)
        self.turnSegOn(3+shiftregister)
        self.turnSegOn(4+shiftregister)
        self.turnSegOn(5+shiftregister)
        self.turnSegOn(6+shiftregister)
        self.turnSegOn(7+shiftregister)

    def digitNine(self, shiftregister=0):
        self.turnSegOn(0+shiftregister)
        self.turnSegOn(1+shiftregister)
        self.turnSegOn(2+shiftregister)
        self.turnSegOn(3+shiftregister)
        self.turnSegOn(6+shiftregister)
        
    def digitZero(self, shiftregister=0):
        self.turnSegOn(0+shiftregister)
        self.turnSegOn(1+shiftregister)
        self.turnSegOn(2+shiftregister)
        self.turnSegOn(4+shiftregister)
        self.turnSegOn(5+shiftregister)
        self.turnSegOn(6+shiftregister)
        self.turnSegOn(7+shiftregister)

    def digitTen():
        digitOne(0);
        digitZero(8);
        
    def digitEleven():
        digitOne(0)
        digitOne(8)
        
    def delay(self, delay):
        shiftpi.delay(delay)
'''
new = CathodeController(1)
new.displayNumber(1)
new.displayNumber(3)
new.displayNumber(11)
new.displayNumber(12)
new.displayNumber(22)
new.displayNumber(10)
new.displayNumber(33)
new.displayNumber(03)
new.displayNumber(99)
'''
