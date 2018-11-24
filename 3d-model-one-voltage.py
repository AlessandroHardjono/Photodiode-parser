# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:53:13 2018

@author: Alessandro Hardjono
"""

import numpy as np
#import matplotlib.pyplot as plt
#import csv

#fileName = 'C:\\Users\\aless\\Documents\\UBC Orbit\\ADCS-SunSensorData\\Sun_Sensor_Data\\DataRaw.txt'

fileName = 'Data_Raw.txt'

data = np.loadtxt(fileName, delimiter=",", comments="#")

anglePlat = data[:,0]
angleServo = data[:,1]
voltage1 = data[:,2]
voltage2 = data[:,3]
voltage3 = data[:,4]
voltage4 = data[:,5]

limitV = 1000

"""
for i in anglePlat :
    if (voltage1[i] > limitV):
        voltage1[i] = 0
    elif (voltage2[i] > limitV):
        voltage2[i] = 0
    elif (voltage3[i] > limitV):
        voltage3[i] = 0
    elif (voltage4[i] > limitV):
        voltage4[i] = 0
"""


"""
AnglePlat = int8(csv.reader(filename,1,0,[1,0,3600,0]))
AngleServo = int8(csv.reader(filename,1,1,[1,1,3600,1]))
Voltage1 = csv.reader(filename,1,2,[1,2,3600,2])
Voltage2 = csv.reader(filename,1,3,[1,3,3600,3])
Voltage3 = csv.reader(filename,1,4,[1,4,3600,4])
Voltage4 = csv.reader(filename,1,5,[1,5,3600,5])
"""