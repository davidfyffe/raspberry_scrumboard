from AbstractButtonController import ButtonController
import MainLogicController as mainlogic

class ServoButton(ButtonController):
    
    def __init__(self, gpio_pin):
        super(ServoButton, self).__init__(gpio_pin)
    
    def myCallBack(self, channel):
            print "Button Controller: Servo Button pressed"
            mainlogic.servoCallBack(channel, self.increment)
        
'''
a = ServoButton(15)
a.setIncrementType('up')
a.registerForButtonEvent()
a.myCallBack(15)
a.myCallBack(15)
a.myCallBack(15)
a.myCallBack(15)
a.myCallBack(15)
a.myCallBack(15)

b = ServoButton(14)
b.setIncrementType('down')
b.registerForButtonEvent()
b.myCallBack(14)
b.myCallBack(14)
b.myCallBack(14)
b.myCallBack(14)

a.myCallBack(15)
a.myCallBack(15)
a.myCallBack(15)
a.myCallBack(15)
a.myCallBack(15)
a.myCallBack(15)
'''