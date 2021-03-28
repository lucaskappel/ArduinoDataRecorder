# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:04:43 2020

@author: Lucas
"""

import serial
import time
import os
import datetime
import matplotlib.pyplot as pt
import numpy as np
ser = serial.Serial('COM3', 9600)
time.sleep(2)
minutes = 90

data = []
select = 1
state = ""
if select == 1:
    state = "on"

filename = os.getcwd()+'\\'+datetime.datetime.now().strftime("%Y_%m_%d_%H_" + str(minutes) + "min_" + state)+'.txt'
file_object = open(filename, "w+")

for i in range(0, 2*60*minutes):
    time.sleep(1)
    b=ser.readline()
    string_n = b.decode()
    data.append([i, float(string_n)])
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' : ' + string_n)
    file_object.write(str(i) + '\t' +string_n)
file_object.close()
ser.close()
data = np.transpose(data)
pt.plot(data[0], data[1], 'b-')
pt.xlabel('time [s]')
pt.ylabel('temperature [K]')
pt.savefig(filename.rstrip('.txt') + '.png', dpi=500)