import time
from INA226 import INA226

i2c_addr = 0x40
ina226 = INA226(i2c_addr)

while True:
    v = ina226.get_voltage()
    c = ina226.get_current()
    p = ina226.get_power()
    print("V: ", v)
    print("C: ", c)
    print("P: ", p)
    time.sleep(1)
