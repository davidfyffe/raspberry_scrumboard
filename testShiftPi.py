import shiftpi

SER_PIN=26
RCLK_PIN=6
SRCLK_PIN=5

def turnSegOn(pinid):
    shiftpi.digitalWrite(pinid, shiftpi.HIGH)
    shiftpi.delay(500)
    shiftpi.digitalWrite(pinid, shiftpi.LOW)
    shiftpi.delay(500)

def turnAllOn():
    # turns all shift register pins to HIGH
    shiftpi.digitalWrite(shiftpi.ALL, shiftpi.HIGH)
    shiftpi.delay(1000)

def turnAllOff():
    # turns all shift register pins to LOW
    shiftpi.digitalWrite(shiftpi.ALL, shiftpi.LOW)
    #shiftpi.delay(1000)
    
def digitOne(shiftregister=0):
    print shiftregister
    shiftpi.digitalWrite(2+shiftregister, shiftpi.HIGH)
    shiftpi.digitalWrite(4+shiftregister, shiftpi.HIGH)

def digitTwo():
    shiftpi.digitalWrite(0, shiftpi.HIGH)
    shiftpi.digitalWrite(1, shiftpi.HIGH)
    shiftpi.digitalWrite(3, shiftpi.HIGH)
    shiftpi.digitalWrite(4, shiftpi.HIGH)
    shiftpi.digitalWrite(5, shiftpi.HIGH)
    
def digitThree():
    shiftpi.digitalWrite(0, shiftpi.HIGH)
    shiftpi.digitalWrite(1, shiftpi.HIGH)
    shiftpi.digitalWrite(3, shiftpi.HIGH)
    shiftpi.digitalWrite(5, shiftpi.HIGH)
    shiftpi.digitalWrite(6, shiftpi.HIGH)
    
def digitFour():
    shiftpi.digitalWrite(0, shiftpi.HIGH)
    shiftpi.digitalWrite(2, shiftpi.HIGH)
    shiftpi.digitalWrite(3, shiftpi.HIGH)
    shiftpi.digitalWrite(6, shiftpi.HIGH)

def digitFive():
    shiftpi.digitalWrite(1, shiftpi.HIGH)
    shiftpi.digitalWrite(2, shiftpi.HIGH)
    shiftpi.digitalWrite(3, shiftpi.HIGH)
    shiftpi.digitalWrite(5, shiftpi.HIGH)
    shiftpi.digitalWrite(6, shiftpi.HIGH)

def digitSix():
    shiftpi.digitalWrite(2, shiftpi.HIGH)
    shiftpi.digitalWrite(3, shiftpi.HIGH)
    shiftpi.digitalWrite(4, shiftpi.HIGH)
    shiftpi.digitalWrite(5, shiftpi.HIGH)
    shiftpi.digitalWrite(6, shiftpi.HIGH)
    shiftpi.digitalWrite(7, shiftpi.HIGH)
    
def digitSeven():
    shiftpi.digitalWrite(0, shiftpi.HIGH)
    shiftpi.digitalWrite(1, shiftpi.HIGH)
    shiftpi.digitalWrite(6, shiftpi.HIGH)
    
def digitEight():
    shiftpi.digitalWrite(0, shiftpi.HIGH)
    shiftpi.digitalWrite(1, shiftpi.HIGH)
    shiftpi.digitalWrite(2, shiftpi.HIGH)
    shiftpi.digitalWrite(3, shiftpi.HIGH)
    shiftpi.digitalWrite(4, shiftpi.HIGH)
    shiftpi.digitalWrite(5, shiftpi.HIGH)
    shiftpi.digitalWrite(6, shiftpi.HIGH)
    shiftpi.digitalWrite(7, shiftpi.HIGH)

def digitNine():
    shiftpi.digitalWrite(0, shiftpi.HIGH)
    shiftpi.digitalWrite(1, shiftpi.HIGH)
    shiftpi.digitalWrite(2, shiftpi.HIGH)
    shiftpi.digitalWrite(3, shiftpi.HIGH)
    shiftpi.digitalWrite(6, shiftpi.HIGH)
    
def digitZero(shiftregister=0):
    shiftpi.digitalWrite(0+shiftregister, shiftpi.HIGH)
    shiftpi.digitalWrite(1+shiftregister, shiftpi.HIGH)
    shiftpi.digitalWrite(2+shiftregister, shiftpi.HIGH)
    shiftpi.digitalWrite(4+shiftregister, shiftpi.HIGH)
    shiftpi.digitalWrite(5+shiftregister, shiftpi.HIGH)
    shiftpi.digitalWrite(6+shiftregister, shiftpi.HIGH)
    shiftpi.digitalWrite(7+shiftregister, shiftpi.HIGH)

def digitTen():
    digitOne(0);
    digitZero(8);
    
def digitEleven():
    digitOne(0)
    digitOne(8)
    '''shiftpi.digitalWrite(2, shiftpi.HIGH)
    shiftpi.digitalWrite(4, shiftpi.HIGH)
    shiftpi.digitalWrite(10, shiftpi.HIGH)
    shiftpi.digitalWrite(12, shiftpi.HIGH)'''
    #shiftpi.digitalWrite(12, shiftpi.HIGH)
    #shiftpi.digitalWrite(6, shiftpi.HIGH)
    #shiftpi.digitalWrite(7, shiftpi.HIGH)

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
        
shiftpi.shiftRegisters(2)
DELAY=500
turnAllOn()
#shiftpi.pinsSetup({"ser": SER_PIN, "rclk": RCLK_PIN, "srclk": SRCLK_PIN}) # that's itturnSegOn(0)
#turnSegOn(1)
#shiftpi.delay(2000)
#turnSegOn(2)
#turnSegOn(3)
#turnSegOn(4)
#turnSegOn(5)
#turnSegOn(6)

#turnAllOn()
#turnAllOff()
#turnAllOn()
turnAllOff()
digitZero()
shiftpi.delay(DELAY)
turnAllOff()
digitOne()
shiftpi.delay(DELAY)
turnAllOff()
digitTwo()
shiftpi.delay(DELAY)
turnAllOff()
digitThree()
shiftpi.delay(DELAY)
turnAllOff()
digitFour()
shiftpi.delay(DELAY)
turnAllOff()
digitFive()
shiftpi.delay(DELAY)
turnAllOff()
digitSix()
shiftpi.delay(DELAY)
turnAllOff()
digitSeven()
shiftpi.delay(DELAY)
turnAllOff()
digitEight()
shiftpi.delay(DELAY)
turnAllOff()
digitNine()
shiftpi.delay(DELAY)
turnAllOff()
digitTen()
shiftpi.delay(DELAY)
turnAllOff()
digitEleven()


shiftpi.delay(DELAY)
turnAllOff()


