import CathodeController

DELAY=2000

new = CathodeController.CathodeController()
'''
#new.turnSegOn(12)
#new.delay(DELAY)
new.displayNumber(1)
new.delay(DELAY)

new.displayNumber(3)
new.delay(DELAY)

new.displayNumber(11)
new.delay(DELAY)
new.displayNumber(12)
new.delay(DELAY)
new.displayNumber(22)
new.delay(DELAY)
new.displayNumber(10)
new.delay(DELAY)
new.displayNumber(33)
new.delay(DELAY)
new.displayNumber(03)
new.delay(DELAY)
new.displayNumber(99)
new.delay(DELAY)
'''
new.turnAllOff()


x=1
while x<10:
    for y in xrange(1,100
    ):
        #new.turnAllOff()
        new.displayNumber(y)
        new.delay(100)
        
    x += 1
