#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import time
import datetime
import signal
from INA226 import INA226

i2c_addr = 0x40
ina226 = INA226(i2c_addr)
V = []
C = []
P = []
ina226.initial_operation()

def make_log_file():
    detail = datetime.datetime.now()
    date = detail.strftime("%Y%m%d%H%M%S")
    filename = './csv/'+ date +'.csv'
    file = open(filename, 'a', newline='')
    csvWriter = csv.writer(file)
    csvWriter.writerow(['unix time', 'V', 'C', 'P'])
    return file, csvWriter

def logging(arg1, arg2):
    unix_time = int(time.time()*1000)
    v = ina226.get_voltage()
    c = ina226.get_current()
    p = ina226.get_power()

    csvWriter.writerow([unix_time, v, c, p])

def kill_signal_process(arg1, args2):
    pass

file, csvWriter = make_log_file()

if __name__ == '__main__':

    try:
        signal.signal(signal.SIGALRM, logging)
        signal.setitimer(signal.ITIMER_REAL, 1.0, 0.1)
        while True:
            pass

    except KeyboardInterrupt:
        file.close()
        signal.signal(signal.SIGALRM, kill_signal_process)
        signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
