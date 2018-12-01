# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:53:13 2018

@author: Alessandro Hardjono
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit
from numpy.polynomial import polynomial as P



fileName = 'Data_Raw.txt'

x_unit = 'degrees(alpha)'
y_unit = 'degrees(beta)'
z_unit = 'voltage'

data = np.loadtxt(fileName, delimiter=",", comments="#")

#the X (plat) and Y (servo) values
anglePlat = data[:,0]
angleServo = data[:,1]

aP, aS = np.meshgrid(anglePlat, angleServo)

#the Z values
voltage1 = data[:,2]
voltage2 = data[:,3]
voltage3 = data[:,4]
voltage4 = data[:,5]

#print to check that the size of the lists are 3600
print(len(anglePlat))
print(len(angleServo))
print(len(voltage1))

#guess = (1,1,1)

voltage_fit = P.polyfit(angleServo, anglePlat, 3, full=True)

plt.clf()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
bx = fig.add_subplot(222, projection='3d')


#choose which one to uncomment depending on what to display
cset = ax.scatter(anglePlat,angleServo, voltage1, cmap=cm.coolwarm)
ax.plot_surface(anglePlat,angleServo,voltage1, cmap=cm.coolwarm)
#cset = ax.scatter(anglePlat,angleServo, voltage2, cmap=cm.coolwarm)
#cset = ax.scatter(anglePlat,angleServo, voltage3, cmap=cm.coolwarm)
#cset = ax.scatter(anglePlat,angleServo, voltage4, cmap=cm.coolwarm)

ax.clabel(cset, fontsize=9, inline=1)
plt.show()



