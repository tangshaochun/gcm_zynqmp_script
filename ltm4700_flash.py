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

def pmbus_send(dev_addr,reg_addr):
  i2c = I2C("/dev/i2c-0")
  write = I2C.Message([reg_addr])
  i2c.transfer(dev_addr, [write])
  i2c.close()

#set the I2C Mux to SENSOR_IIC_BUS 0x01
set_i2c_mux(TCA9548_U165_ADDR,Z_IIC_BUS1)

#Configure comp of LTM4700

pmbus_send(LTM4700_U107_ADDR,0x15)
pmbus_send(LTM4700_U108_ADDR,0x15)
pmbus_send(LTM4700_U109_ADDR,0x15)
pmbus_send(LTM4700_U110_ADDR,0x15)
pmbus_send(LTM4700_U184_ADDR,0x15)
pmbus_send(LTM4678_U6_ADDR,0x15)
pmbus_send(LTM4678_U7_ADDR,0x15)
