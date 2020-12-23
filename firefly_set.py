#!/usr/bin/env python
from __future__ import print_function

from periphery import I2C
from constants import *
from configurations import board

def tca6424_reg_wr(i2c_bus_addr,dev_addr,reg_addr,reg0,reg1,reg2):
  i2c = I2C("/dev/i2c-0")
  i2c.transfer(TCA9548_U165_ADDR, [I2C.Message([i2c_bus_addr])])   # select i2c bus
  i2c.transfer(dev_addr, [I2C.Message([reg_addr,reg0,reg1,reg2])]) # write the value to the 3 configuration registers
  i2c.close()

def tca6424_reg_rd(i2c_bus_addr,dev_addr,reg_addr):
  i2c = I2C("/dev/i2c-0")
  i2c.transfer(TCA9548_U165_ADDR, [I2C.Message([i2c_bus_addr])]) # select i2c bus

  read = I2C.Message([0x0]*3, read=True)
  i2c.transfer(dev_addr, [I2C.Message([reg_addr])])      # set reg_addr
  i2c.transfer(dev_addr, [read])
  i2c.close()
  
  print('read back is 0x{0:x}' .format(read.data))
  return read.data

#def minpod_check (i2c_bus_addr,dev_addr):
#  for i in range(228, 234):
#    minipod_reg_rd(i2c_bus_addr,dev_addr,0x01,i)
#
#def minipod_set(i2c_bus_addr, dev_addr,reg_value):
#  for i in range(228,234):
#    minipod_reg_wr(i2c_bus_addr,dev_addr,0x01,i,reg_value)
#configure the TCA6424 IO ports as inputor output
tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U16_ADDR,0x0C,0x49,0x92,0x24) #P07-P00 01001001; P17-P10 10010010; P27-P20 00100100 (0 is output; 1 is input)
#tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U16_ADDR,0x0D,0x92) #P17-P10 10010010 (0 is output; 1 is input)
#tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U16_ADDR,0x0E,0x24) #P27-P20 00100100 (0 is output; 1 is input)
tca6424_reg_rd(Z_IIC_BUS6,TCA6424_U16_ADDR,0x0C)
#tca6424_reg_rd(Z_IIC_BUS6,TCA6424_U16_ADDR,0x0D)
#tca6424_reg_rd(Z_IIC_BUS6,TCA6424_U16_ADDR,0x0E)
tca6424_reg_wr(Z_IIC_BUS6,TCA6424_U17_ADDR,0x0C,0x49,0x92,0x24) #P07-P00 01001001; P17-P10 10010010; P27-P20 00100100 (0 is output; 1 is input)
tca6424_reg_rd(Z_IIC_BUS6,TCA6424_U17_ADDR,0x0C)

tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U13_ADDR,0x0C,0x24,0x49,0x92) #P07-P00 00100100; P17-P10 01001001; P27-P20 10010010 (0 is output; 1 is input)
tca6424_reg_rd(Z_IIC_BUS7,TCA6424_U13_ADDR,0x0C)
tca6424_reg_wr(Z_IIC_BUS7,TCA6424_U14_ADDR,0x0C,0x49,0x92,0x24) #P07-P00 01001001; P17-P10 10010010; P27-P20 00100100 (0 is output; 1 is input)
tca6424_reg_rd(Z_IIC_BUS7,TCA6424_U14_ADDR,0x0C)

tca6424_reg_wr(Z_IIC_BUS8,TCA6424_U15_ADDR,0x0C,0xC9,0xFF,0x27) #P07-P00 11001001; P17-P10 11111111; P27-P20 00100111 (0 is output; 1 is input)
tca6424_reg_rd(Z_IIC_BUS8,TCA6424_U15_ADDR,0x0C)

