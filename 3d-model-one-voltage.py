# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:53:13 2018

@author: Alessandro Hardjono
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d

#fileName = 'C:\\Users\\aless\\Documents\\UBC Orbit\\ADCS-SunSensorData\\Sun_Sensor_Data\\DataRaw.txt'

fileName = 'Data_Raw.txt'

x_unit = 'degrees(alpha)'
y_unit = 'degrees(beta)'
z_unit = 'voltage'

data = np.loadtxt(fileName, delimiter=",", comments="#")


anglePlat = data[:,0]
angleServo = data[:,1]

#anglePlat, angleServo = np.meshgrid(anglePlat, angleServo)

voltage1 = data[:,2]
#voltage1 = voltage1.reshape((len(anglePlat), len(angleServo)))

voltage2 = data[:,3]
voltage3 = data[:,4]
voltage4 = data[:,5]

print(len(anglePlat))
print(len(angleServo))
print(len(voltage1))

#anglePlat, angleServo = np.meshgrid(anglePlat, angleServo)

plt.clf()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cset = ax.scatter(anglePlat,angleServo, voltage1, cmap=cm.coolwarm)
ax.clabel(cset, fontsize=9, inline=1)
plt.show()


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

