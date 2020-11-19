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

# Board Temperature monitoring
print('----------Temperature monitoring of gFEX production board-----------------')
print('REFDES    Device      Temperature(C)    Description')
#set the I2C Mux to SENSOR_IIC_BUS 0x01
set_i2c_mux(TCA9548_U165_ADDR,Z_IIC_BUS1)

#12V power module BMR458 temperature
reg_value=pmbus_read(LTM4700_U107_ADDR,0x8D,2)
temperature=lin5_11ToFloat(reg_value)
print('U107       BMR458      {0:d}                12V DC/DC Converter' .format(trunc(temperature)))
reg_value=pmbus_read(LTM4700_U107_ADDR,0x88,2)
vin_voltage=lin5_11ToFloat(reg_value)
print('U107       LTM4700     {0:d}                INTVCC A DC/DC Converter' .format(trunc(vin_voltage)))
reg_value=pmbus_read(LTM4700_U107_ADDR,0xD3,1)
print(reg_value)
#pmbus_write(LTM4700_U107_ADDR,0xD3,0xb4)
reg_value=pmbus_read(LTM4700_U107_ADDR,0xD3,1)
print(reg_value)

#print('U107       LTM4700     {0:d}                INTVCC A DC/DC Converter' .format(reg_value))
reg_value=pmbus_read(LTM4700_U108_ADDR,0x8D,2)
temperature=lin5_11ToFloat(reg_value)
print('U108       BMR458      {0:d}                12V DC/DC Converter' .format(trunc(temperature)))
reg_value=pmbus_read(LTM4700_U109_ADDR,0x8D,2)
temperature=lin5_11ToFloat(reg_value)
print('U109       BMR458      {0:d}                12V DC/DC Converter' .format(trunc(temperature)))

