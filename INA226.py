#!/usr/bin/python
# -*- coding: utf-8 -*-

import smbus

class INA226:
    def __init__(self, addr):
        self.i2c = smbus.SMBus(1)

        self.VOLTAGE_REGISTER = 0x02
        self.CURRENT_REGISTER = 0x04
        self.POWER_REGISTER = 0x03
        self.CALIBRATION_REGISTER = 0x05

        self.SENSOR_ADDR = addr

        self.voltage = 0.0
        self.current = 0.0
        self.power = 0.0

    def initial_operation(self):
        self.i2c.write_i2c_block_data(self.SENSOR_ADDR, self.CALIBRATION_REGISTER, [0x0a, 0x00])

    def bit_operation(self, bit_data):
        result = ( (bit_data << 8) & 0xFF00 ) + (bit_data >> 8)
        return result

    def get_voltage(self):
        v_word = self.i2c.read_word_data(self.SENSOR_ADDR, self.VOLTAGE_REGISTER)
        v_result = self.bit_operation(v_word)
        self.voltage = v_result * 1.25 / 1000
        return self.voltage

    def get_current(self):
        c_word = self.i2c.read_word_data(self.SENSOR_ADDR, self.CURRENT_REGISTER)
        c_result = self.bit_operation(c_word)
        self.current = c_result * 1.0 / 1000
        return self.current

    def get_power(self):
        p_word = self.i2c.read_word_data(self.SENSOR_ADDR, self.POWER_REGISTER)
        p_result = self.bit_operation(p_word)
        self.power = p_result * 25.0 / 1000
        return self.power
