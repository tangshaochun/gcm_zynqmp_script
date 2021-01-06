#!/usr/bin/env python
from __future__ import print_function

from periphery import I2C
from constants import *
from configurations import board

def tca6424_reg_wr(i2c_bus_addr,dev_addr,reg_addr,reg):
  i2c = I2C("/dev/i2c-0")
  i2c.transfer(TCA9548_U165_ADDR, [I2C.Message([i2c_bus_addr])])   # select i2c bus
  i2c.transfer(dev_addr, [I2C.Message([reg_addr,reg])]) # write the value to the 3 configuration registers
  i2c.close()

def tca6424_reg_rd(i2c_bus_addr,dev_addr,reg_addr):
  i2c = I2C("/dev/i2c-0")
  i2c.transfer(TCA9548_U165_ADDR, [I2C.Message([i2c_bus_addr])]) # select i2c bus

  read = I2C.Message([0x0]*1, read=True)
  i2c.transfer(dev_addr, [I2C.Message([reg_addr])])      # set reg_addr
  i2c.transfer(dev_addr, [read])
  i2c.close()
  
  print('read back is 0x{0:x}' .format(read.data[0]))
  return read.data[0]
 
def firefly_reset_release(i2c_bus_addr,device_addr):
	#Release the Reset and deselect the firefly
	tca6424_reg_wr(i2c_bus_addr,device_addr,0x04,0xFF)
	tca6424_reg_wr(i2c_bus_addr,device_addr,0x05,0xFF)
	tca6424_reg_wr(i2c_bus_addr,device_addr,0x06,0xFF)
	tca6424_reg_rd(i2c_bus_addr,device_addr,0x04)
	tca6424_reg_rd(i2c_bus_addr,device_addr,0x05)
	tca6424_reg_rd(i2c_bus_addr,device_addr,0x06)
  
def firefly_select (refdes):
	firefly_reset_release(Z_IIC_BUS6,TCA6424_U16_ADDR)
	firefly_reset_release(Z_IIC_BUS6,TCA6424_U17_ADDR)
	firefly_reset_release(Z_IIC_BUS7,TCA6424_U13_ADDR)
	firefly_reset_release(Z_IIC_BUS7,TCA6424_U14_ADDR)
	firefly_reset_release(Z_IIC_BUS8,TCA6424_U15_ADDR)
	print ('Deselect all the FireFlys')
	if refdes=="U51" or refdes=="U52":
		#Select the FireFly A RX/TX 1 (U51/U52)		
		tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U17_ADDR,0x04,0xED) #1110_1101
		print ('FireFly A RX/TX 1 (U51/U52) are selected')
	elif refdes=="U50" or refdes=="U49":	
		#Select the FireFly A RX/TX 2 (U50/U49)
		tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U17_ADDR,0x04,0x7F) #0111_1111
		tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U17_ADDR,0x05,0xFB) #1111_1011
	elif refdes=="U53" or refdes=="U54":	
		#Select the FireFly A RX/TX 3 (U53/U54)
		tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U17_ADDR,0x05,0xDF) #1101_1111
		tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U17_ADDR,0x06,0xFE) #1111_1110	
	elif refdes=="U56" or refdes=="U55":	
		#Select the FireFly A RX/TX 4 (U56/U55)
		tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U16_ADDR,0x06,0xB7) #1011_0111			
	elif refdes=="U57" or refdes=="U58":	
		#Select the FireFly A RX/TX 5 (U57/U58)
		tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U16_ADDR,0x05,0xDF) #1101_1111
		tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U16_ADDR,0x06,0xFE) #1111_1110			
	elif refdes=="U60" or refdes=="U59":	
		#Select the FireFly A RX/TX 6 (U60/U59)
		tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U16_ADDR,0x04,0x7F) #0111_0111
		tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U16_ADDR,0x05,0xFB) #1111_1011		
	elif refdes=="U61" or refdes=="U62":	
		#Select the FireFly A RX/TX 7 (U61/U62)
		tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U16_ADDR,0x04,0xED) #1110_1101
	elif refdes=="U64" or refdes=="U63":	
		#Select the FireFly A RX/TX 8 (U64/U63)
		tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U17_ADDR,0x06,0xB7) #1011_0111	
			
	elif refdes=="U65" or refdes=="U66":	
		#Select the FireFly B RX/TX 1 (U65/U66)
		tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U14_ADDR,0x04,0xED) #1110_1101	
	elif refdes=="U68" or refdes=="U67":	
		#Select the FireFly B RX/TX 2 (U68/U67)
		tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U14_ADDR,0x04,0x7F) #0111_1111
		tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U14_ADDR,0x05,0xFB) #1111_1011		
	elif refdes=="U69" or refdes=="U70":	
		#Select the FireFly B RX/TX 3 (U69/U70)
		tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U14_ADDR,0x05,0xDF) #1101_1111
		tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U14_ADDR,0x06,0xFE) #1111_1110				
	elif refdes=="U72" or refdes=="U71":	
		#Select the FireFly B RX/TX 4 (U72/U71)
		tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U14_ADDR,0x06,0xB7) #1011_0111		
	elif refdes=="U73" or refdes=="U74":	
		#Select the FireFly B RX/TX 5 (U73/U74)
		tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U13_ADDR,0x06,0xB7) #1011_0111		
	elif refdes=="U76" or refdes=="U75":	
		#Select the FireFly B RX/TX 6 (U76/U75)
		tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U13_ADDR,0x05,0xDF) #1101_1111
		tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U13_ADDR,0x06,0xFE) #1111_1110		
	elif refdes=="U77" or refdes=="U78":	
		#Select the FireFly B RX/TX 7 (U77/U78)
		tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U13_ADDR,0x04,0x7F) #0111_1111
		tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U13_ADDR,0x05,0xFB) #1111_1011	
	elif refdes=="U80" or refdes=="U79":	
		#Select the FireFly B RX/TX 8 (U80/U79)
		tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U13_ADDR,0x04,0xED) #1110_1101	

	elif refdes=="U81" or refdes=="U84":	
		#Select the FireFly Z RX/TX 1 (U81/U84)
		tca6424_reg_wr(Z_IIC_BUS8,TCA6424_U13_ADDR,0x06,0xB7) #1011_0111	
	elif refdes=="U82" or refdes=="U83":	
		#Select the FireFly GRM RX/TX 1 (U82/U83)
		tca6424_reg_wr(Z_IIC_BUS8,TCA6424_U13_ADDR,0x04,0xED) #1110_1101
	else:
		print ('Invalid Firefly REFDES, Please refer to the schematics for the details.')
		return False
		
def firefly_reg_wr(i2c_bus_addr,firefly_refdes,dev_addr,reg_page,reg_addr,reg_value):
	firefly_select(firefly_refdes)
  i2c = I2C("/dev/i2c-0")
  i2c.transfer(TCA9548_U165_ADDR, [I2C.Message([i2c_bus_addr])])   # select i2c bus
  
  i2c.transfer(dev_addr, [I2C.Message([127,reg_page])]) # select the register page
  i2c.transfer(dev_addr, [I2C.Message([reg_addr,reg_value])]) # write the value to registers
  i2c.close()		
  
def firefly_reg_rd(i2c_bus_addr,firefly_refdes,dev_addr,reg_page,reg_addr):
	firefly_select(firefly_refdes)
  i2c = I2C("/dev/i2c-0")
  i2c.transfer(TCA9548_U165_ADDR, [I2C.Message([i2c_bus_addr])])   # select i2c bus

  read = I2C.Message([0x0]*1, read=True)
  i2c.transfer(dev_addr, [I2C.Message([127,reg_page])]) # select the register page
  i2c.transfer(dev_addr, [I2C.Message([reg_addr])])      # set reg_addr
  i2c.transfer(dev_addr, [read])
  i2c.close()
  
  print('read back is 0x{0:x}' .format(read.data[0]))
  return read.data[0]
  
  
						
#configure the TCA6424 IO ports as inputor output
#tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U16_ADDR,0x8C,0x49,0x92,0x24) #P07-P00 01001001; P17-P10 10010010; P27-P20 00100100 (0 is output; 1 is input)
tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U16_ADDR,0x0C,0x49) #P07-P00 01001001;
tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U16_ADDR,0x0D,0x92) #P17-P10 10010010 (0 is output; 1 is input)
tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U16_ADDR,0x0E,0x24) #P27-P20 00100100 (0 is output; 1 is input)
tca6424_reg_rd(Z_IIC_BUS6,TCA6424_U16_ADDR,0x0C)
tca6424_reg_rd(Z_IIC_BUS6,TCA6424_U16_ADDR,0x0D)
tca6424_reg_rd(Z_IIC_BUS6,TCA6424_U16_ADDR,0x0E)

tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U17_ADDR,0x0C,0x49) #P07-P00 01001001;
tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U17_ADDR,0x0D,0x92) #P17-P10 10010010 (0 is output; 1 is input)
tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U17_ADDR,0x0E,0x24) #P27-P20 00100100 (0 is output; 1 is input)
tca6424_reg_rd(Z_IIC_BUS6,TCA6424_U17_ADDR,0x0C)
tca6424_reg_rd(Z_IIC_BUS6,TCA6424_U17_ADDR,0x0D)
tca6424_reg_rd(Z_IIC_BUS6,TCA6424_U17_ADDR,0x0E)

tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U13_ADDR,0x0C,0x24) #P07-P00 00100100;
tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U13_ADDR,0x0D,0x49) #P17-P10 01001001 (0 is output; 1 is input)
tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U13_ADDR,0x0E,0x92) #P27-P20 10010010 (0 is output; 1 is input)
tca6424_reg_rd(Z_IIC_BUS7,TCA6424_U13_ADDR,0x0C)
tca6424_reg_rd(Z_IIC_BUS7,TCA6424_U13_ADDR,0x0D)
tca6424_reg_rd(Z_IIC_BUS7,TCA6424_U13_ADDR,0x0E)

tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U14_ADDR,0x0C,0x49) #P07-P00 01001001;
tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U14_ADDR,0x0D,0x92) #P17-P10 10010010 (0 is output; 1 is input)
tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U14_ADDR,0x0E,0x24) #P27-P20 00100100 (0 is output; 1 is input)
tca6424_reg_rd(Z_IIC_BUS7,TCA6424_U14_ADDR,0x0C)
tca6424_reg_rd(Z_IIC_BUS7,TCA6424_U14_ADDR,0x0D)
tca6424_reg_rd(Z_IIC_BUS7,TCA6424_U14_ADDR,0x0E)

tca6424_reg_wr(Z_IIC_BUS8,TCA6424_U15_ADDR,0x0C,0xC9) #P07-P00 01001001;
tca6424_reg_wr(Z_IIC_BUS8,TCA6424_U15_ADDR,0x0D,0xFF) #P17-P10 10010010 (0 is output; 1 is input)
tca6424_reg_wr(Z_IIC_BUS8,TCA6424_U15_ADDR,0x0E,0x27) #P27-P20 00100100 (0 is output; 1 is input)
tca6424_reg_rd(Z_IIC_BUS8,TCA6424_U15_ADDR,0x0C)
tca6424_reg_rd(Z_IIC_BUS8,TCA6424_U15_ADDR,0x0D)
tca6424_reg_rd(Z_IIC_BUS8,TCA6424_U15_ADDR,0x0E)

#Release the Reset and deselect all the firefly
firefly_reset_release(Z_IIC_BUS6,TCA6424_U16_ADDR)
firefly_reset_release(Z_IIC_BUS6,TCA6424_U17_ADDR)
firefly_reset_release(Z_IIC_BUS7,TCA6424_U13_ADDR)
firefly_reset_release(Z_IIC_BUS7,TCA6424_U14_ADDR)
firefly_reset_release(Z_IIC_BUS8,TCA6424_U15_ADDR)

#Select the FireFly A TX/RX 8 (U92/U38)
firefly_reg_rd(Z_IIC_BUS6,"U51",FIREFLY_RX_ADDR,0,62)



