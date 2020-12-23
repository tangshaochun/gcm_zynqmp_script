#!/usr/bin/env python
from __future__ import print_function
from math import trunc
from time import sleep
import sys

from periphery import I2C
# all hw addresses are defined in here
from constants import *
from configurations import board

def set_i2c_mux(dev_addr,channel):
  i2c = I2C("/dev/i2c-0")
  i2c.transfer(dev_addr, [I2C.Message([channel])])
  i2c.close()

#convert a LinearFloat5_11 formatted word into a floating point value
def lin5_11ToFloat(wordValue):
  binValue = int(wordValue,16)
  binValue=binValue>>8 | (binValue << 8 & 0xFF00)
  #wordValue = ' '.join(format(x, 'b') for x in bytearray(wordValue))
  exponent = binValue>>11      #extract exponent as MS 5 bits
  mantissa = binValue & 0x7ff  #extract mantissa as LS 11 bits

  #sign extended exponent
  if exponent > 0x0F: exponent |= 0xE0
  if exponent > 127: exponent -= 2**8
  #sign extended mantissa
  if mantissa > 0x03FF: mantissa |= 0xF800
  if mantissa > 32768: mantissa -= 2**16
  # compute value as
  return mantissa * (2**exponent)

def pmbus_read(dev_addr,reg_addr,n_bytes):
  i2c = I2C("/dev/i2c-0")
  write = I2C.Message([reg_addr])
  read = I2C.Message([0x0]*n_bytes, read=True)
  i2c.transfer(dev_addr, [write, read])
  i2c.close()
  return bytes(bytearray(read.data)).encode('hex')

def pmbus_write(dev_addr,reg_addr,reg_value):
  i2c = I2C("/dev/i2c-0")
  i2c.transfer(dev_addr, [I2C.Message([reg_addr,reg_value])])   # write the value to the reg_addr
  i2c.close()

#set the I2C Mux to SENSOR_IIC_BUS 0x01
set_i2c_mux(TCA9548_U165_ADDR,Z_IIC_BUS1)

#Configure comp of LTM4700
regvalue=0xf5
pmbus_write(LTM4700_U107_ADDR,0x00,0xff)
pmbus_write(LTM4700_U107_ADDR,0xD3,regvalue)
pmbus_write(LTM4700_U108_ADDR,0x00,0xff)
pmbus_write(LTM4700_U108_ADDR,0xD3,regvalue)
pmbus_write(LTM4700_U109_ADDR,0x00,0xff)
pmbus_write(LTM4700_U109_ADDR,0xD3,regvalue)
pmbus_write(LTM4700_U110_ADDR,0x00,0xff)
pmbus_write(LTM4700_U110_ADDR,0xD3,regvalue)
pmbus_write(LTM4700_U184_ADDR,0x00,0xff)
pmbus_write(LTM4700_U184_ADDR,0xD3,regvalue)
pmbus_write(LTM4678_U6_ADDR,0x00,0xff)
pmbus_write(LTM4678_U6_ADDR,0xD3,0x94)
pmbus_write(LTM4678_U7_ADDR,0x00,0xff)
pmbus_write(LTM4678_U7_ADDR,0xD3,0x94)
#pmbus_write(LTM4678_U8_ADDR,0xD3,0x94)

#Configure comp of LTM4700
#pmbus_write(LTM4700_U107_ADDR,0xD4,0xc6)
#pmbus_write(LTM4700_U108_ADDR,0xD4,0xc6)
#pmbus_write(LTM4700_U109_ADDR,0xD4,0xc6)
#pmbus_write(LTM4700_U110_ADDR,0xD4,0xc6)
#pmbus_write(LTM4700_U184_ADDR,0xD4,0xc6)

#Configure under voltage response of  LTM4700
pmbus_write(LTM4700_U107_ADDR,0x45,0x00)
pmbus_write(LTM4700_U108_ADDR,0x45,0x00)
pmbus_write(LTM4700_U109_ADDR,0x45,0x00)
pmbus_write(LTM4700_U110_ADDR,0x45,0x00)
pmbus_write(LTM4700_U184_ADDR,0x45,0x00)

