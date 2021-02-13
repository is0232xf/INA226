#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import datetime
import signal
from INA226 import INA226

i2c_addr = 0x40
ina226 = INA226(i2c_addr))
V, C, P = []
count = 0

ina226.initial_operation()

def make_log_file(filename):
    detail = datetime.datetime.now()
    date = detail.strftime("%Y%m%d%H%M%S")
    filename = './csv/'+ date +'.csv'
    file = open(filename, 'a', newline='')
    csvWriter = csv.writer(file)
    csvWriter.writerow(['count', 'V', 'C', 'P'])
    return file, csvWriter

def logging(csvWriter):
    count = count + 0.1
    v = ina226.get_voltage()
    c = ina226.get_current()
    p = ina226.get_power()

    csvWriter.writerow([count, v, c, p])

def kill_signal_process(arg1, args2):
    pass

if __name__ == '__main__':
    file, csvWriter = make_log_file(filename)

    try:
        signal.signal(signal.SIGALRM, logging(csvWriter))
        signal.setitimer(signal.ITIMER_REAL, 0.5, 0.1)

    except KeyboardInterrupt:
        file.close()
        signal.signal(signal.SIGALRM, kill_signal_process)
        signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
