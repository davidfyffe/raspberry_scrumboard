#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2016  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#
import time

from CathodeButton import CathodeButton
from ServoButton import ServoButton

import MainLogicController as mainController




def main():
    
    YELLOWUP=18
    YELLOWDOWN=23
    BLUELED = 22
    BLUESWITCH = 27
    REDLED = 23
    REDSWITCH = 25
    GREENLED = 24
    GREENSWITCH = 6
    
    yellowUpButton = CathodeButton(YELLOWUP)
    yellowUpButton.setIncrementType('up')
    yellowDownButton = CathodeButton(YELLOWDOWN)
    yellowDownButton.setIncrementType('down')
    #blueButton = ServoButton(BLUESWITCH)
    #greenButton = ServoButton(GREENSWITCH)
    #redButton = ServoButton(REDSWITCH)
    
    
    running=True
    while running==True:
            try:
                '''
                '''
                #print "running"
            
            except KeyboardInterrupt:
                running=False
                
    return 0

if __name__ == '__main__':
    main()

