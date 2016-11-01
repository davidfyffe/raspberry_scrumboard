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
    
def digitOne():
    shiftpi.digitalWrite(2, shiftpi.HIGH)
    shiftpi.digitalWrite(4, shiftpi.HIGH)

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
    shiftpi.digitalWrite(shiftpi.ALL, shiftpi.HIGH)

def digitNine():
    shiftpi.digitalWrite(0, shiftpi.HIGH)
    shiftpi.digitalWrite(1, shiftpi.HIGH)
    shiftpi.digitalWrite(2, shiftpi.HIGH)
    shiftpi.digitalWrite(3, shiftpi.HIGH)
    shiftpi.digitalWrite(6, shiftpi.HIGH)
    
def digitZero():
    shiftpi.digitalWrite(0, shiftpi.HIGH)
    shiftpi.digitalWrite(1, shiftpi.HIGH)
    shiftpi.digitalWrite(2, shiftpi.HIGH)
    shiftpi.digitalWrite(4, shiftpi.HIGH)
    shiftpi.digitalWrite(5, shiftpi.HIGH)
    shiftpi.digitalWrite(6, shiftpi.HIGH)
    shiftpi.digitalWrite(7, shiftpi.HIGH)
    
#shiftpi.pinsSetup({"ser": SER_PIN, "rclk": RCLK_PIN, "srclk": SRCLK_PIN}) # that's it

#turnSegOn(0)
#turnSegOn(1)
#turnSegOn(2)
#turnSegOn(3)
#turnSegOn(4)
#turnSegOn(5)
#turnSegOn(6)

#turnAllOn()
#turnAllOff()
#turnAllOn()
turnAllOff()

#digitOne()
#shiftpi.delay(1000)
#turnAllOff()
#digitTwo()
#shiftpi.delay(1000)
#turnAllOff()
#digitThree()
#shiftpi.delay(1000)
#turnAllOff()
#digitFour()
#shiftpi.delay(1000)
#turnAllOff()
digitFive()
shiftpi.delay(1000)
turnAllOff()
digitSix()
shiftpi.delay(1000)
turnAllOff()
digitSeven()
shiftpi.delay(1000)
turnAllOff()
digitEight()
shiftpi.delay(1000)
turnAllOff()
digitNine()
shiftpi.delay(1000)
turnAllOff()
digitZero()


shiftpi.delay(1000)
turnAllOff()


