import time
from CathodeController import CathodeController

dutyCycleFullRight = 3
dutyCycleFullLeft = 15
dutyCycleTDC = 8
currentServoPositionValue = 0.0
currentCathodeValue = 0
    
def incrementServoAmount():
    global currentServoPositionValue
    if currentServoPositionValue < dutyCycleFullLeft:
        currentServoPositionValue += 1
        
def resetServoAmount():
    return dutyCycleTDC
    
def decrementServoAmount():
    global currentServoPositionValue
    if currentServoPositionValue > dutyCycleFullRight:
        currentServoPositionValue -= 1
        
def incrementCathode():
    global currentCathodeValue
    if currentCathodeValue < 99:
        currentCathodeValue += 1

def decrementCathode():
    global currentCathodeValue
    if currentCathodeValue > 0:
        currentCathodeValue -= 1
        
def servoCallBack(channel, increment):
    global currentServoPositionValue
    print "Edge detected on channel ", channel
    if increment == 'up':
        incrementServoAmount()
        print "Incremented to {}".format(currentServoPositionValue)
        #updateServoPosition(value)
    elif increment == 'down':
        decrementServoAmount()
        print "Decremented to {}".format(currentServoPositionValue)
        #updateServoPosition(value)
    else:
        print "reset servo"
        currentServoPositionValue = resetServoAmount()
        #updateServoPosition(value)

def updateServoPosition(currentValue):
    #currentValue = dbController.selectValue()
    #servoController.setServoToPosition(currentValue)
    print "update servo position here"
    

def cathodeCallBack(channel, increment):
    global currentCathodeValue
    print "Edge detected on channel ", channel
    if increment == 'up':
        incrementCathode()
        print "Incremented to {}".format(currentCathodeValue)
    elif increment == 'down':
        decrementCathode()
        print "Decremented to {}".format(currentCathodeValue)
    else:
        print "reset counter"
        currentCathodeValue = 0
     CathodeController.displayNumber(currentCathodeValue)   

        
