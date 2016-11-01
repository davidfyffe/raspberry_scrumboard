'''
Created on Oct 31, 2016

@author: n0206863
'''
import Switch

class CathodeController(object):
    '''
    7 segment Common cathode
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    
    def displayNumber(self, number):
        
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
                self.printDigitZero(bitAddition)
                break
            if case(1):
                self.printDigitOne(bitAddition)
                break
            if case(2):
                self.printDigitTwo(bitAddition)
                break
            if case(3):
                self.printDigitThree(bitAddition)
                break
            if case(): # default, could also just omit condition or 'if True'
                print "something else!"
                # No need to break here, it'll stop anyway
        
       
    def testStuff(self, displayDigit):
        
        value = 'b'
        x = 1
        
        result= {
                 'a':lambda x:x * 5,
                 'b':lambda x: x+7 
                 }[value](x)
         
        print value
        print x     
        print result   
                 
    def printDigitZero(self, bits=0):
        digit = 0+bits
        print "digit {} {}".format(0, digit)    
    def printDigitOne(self, bits=0):
        digit = 1+bits
        print "digit {} {}".format(1, digit)
    def printDigitTwo(self, bits=0):
        digit = 2+bits
        print "digit {} {}".format(2, digit)
    def printDigitThree(self, bits=0):
        digit = 3+bits
        print "digit {} {}".format(3, digit)

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