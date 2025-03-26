from smbus2 import SMBus
import time

class I2CSwitch:

    selmap = [0x01, 0x02, 0x04, 0x08]

    def __init__(self, i2c_bus, i2c_addr):
        self.i2c_addr = i2c_addr
        self.bus = SMBus(i2c_bus)
    
    def reset(self):
        self.bus.write_byte_data(self.i2c_addr, 0x00, 0x00)

    def select(self, channel):
        if channel not in range(4):
            raise IndexError("channel index must be inside [0...3] range")
        self.bus.write_byte_data(self.i2c_addr, 0x00, self.selmap[channel])
        time.sleep(0.1)

    def get_channel(self):
        return self.selmap.index(self.bus.read_byte_data(self.i2c_addr, 0x00))
   
    def get_channel_debug(self):
        return self.bus.read_byte_data(self.i2c_addr, 0x00)

