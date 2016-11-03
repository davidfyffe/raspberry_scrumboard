import RPi.GPIO as GPIO # Remember to run as superuser (sudo)
import time
from abc import ABCMeta, abstractmethod

class ButtonController(object):
    __metaclass__ = ABCMeta
    
    incrementType = ""
    
    'Common button controller class. takes pin number'
    def __init__(self, gpio_pin):
        self.gpio_pin = gpio_pin
        GPIO.setmode(GPIO.BCM)   # This example uses the BCM pin numbering
        GPIO.setup(self.gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.gpio_pin, GPIO.RISING, callback=self.myCallBack, bouncetime=300)
        
    def setIncrementType(self, increment):
        self.increment = increment
    def getIncrementType(self):
        return self.increment

    def checkForButtonPress(self):
        input_state = GPIO.input(self.gpio_pin)
        if input_state == False:
            print "Button Pressed on ", self.gpio_pin
            time.sleep(0.2)

    #local callback defering logic to main controller
    @abstractmethod 
    def myCallBack(self, channel): pass
        
    
