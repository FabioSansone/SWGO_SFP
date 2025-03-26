#!/usr/bin/env python3
from SFP import SFP
from I2CSwitch import I2CSwitch

switch = I2CSwitch(i2c_bus=2, i2c_addr=0x70)
sfp = SFP(i2c_bus=2, i2c_addr=0x70, i2c_select=(lambda:switch.select(1),))

print("SFP #0")
if sfp.is_available():
   sfp.print()
else:
   print("not available")
print()

