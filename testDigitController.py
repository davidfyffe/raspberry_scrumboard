import digitController
from digitController import Shifter

shifter = Shifter()
shifter.clear()
shifter.setValue(0x0AAAAAA)
sleep(pause)
shifter.clear()
shifter.setValue(0x0555555)
sleep(pause)
