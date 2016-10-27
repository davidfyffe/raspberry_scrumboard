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



if __name__ == '__main__':
	main()
    
def main():
	pause=0.5
	gpio.setmode(gpio.BOARD)
	shifter=Shifter()
	running=True
	while running==True:
        	try:
			#shifter.clear()
			#shifter.setValue(1)
			#sleep(1)
			shifter.clear()
			shifter.setValue(0x0AAAAAA)
			sleep(pause)
			shifter.clear()
			shifter.setValue(0x0555555)
			sleep(pause)
	        except KeyboardInterrupt:
        		running=False


if __name__=="__main__":
    main()

