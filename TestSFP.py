#!/usr/bin/env python3
from SFP import SFP
from I2CSwitch import I2CSwitch
from functools import partial

SWITCH_ADDR = 0x70
SFP_ADDR = 0x50
 

switch = I2CSwitch(i2c_bus=2, i2c_addr=SWITCH_ADDR)


sfp = SFP(i2c_bus=2, i2c_addr=SFP_ADDR, i2c_select=(partial(switch.select, 0),))
print(switch.get_channel_debug())

print("SFP #0")
if sfp.is_available():
   sfp.print()
else:
   print("not available")
print()

