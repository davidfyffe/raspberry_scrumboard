from AbstractButtonController import ButtonController
import MainLogicController as mainlogic

class CathodeButton(ButtonController):
    
    def __init__(self, gpio_pin):
        super(CathodeButton, self).__init__(gpio_pin)
    
    def myCallBack(self, channel):
            print "Button Controller: Cathode Button pressed"
            mainlogic.cathodeCallBack(channel, self.increment)
        
'''
a = CathodeButton(15)
a.setIncrementType('up')
a.registerForButtonEvent()
a.myCallBack(15)
a.myCallBack(15)
a.myCallBack(15)
a.myCallBack(15)
a.myCallBack(15)
a.myCallBack(15)

for x in range(0, 99):
    a.myCallBack(15)

b = CathodeButton(14)
b.setIncrementType('down')
b.registerForButtonEvent()
b.myCallBack(14)
b.myCallBack(14)
b.myCallBack(14)
b.myCallBack(14)

for x in range(0, 99):
    b.myCallBack(15)

'''