# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:53:13 2018

@author: Alessandro Hardjono
"""

import numpy as np
import matplotlib.pyplot as plt
from math import atan
from math import pi
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from numpy.polynomial import polynomial as P

WIDTH = 3
HEIGHT = 1.5

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
v1 = data[:,2]
v2 = data[:,3]
v3 = data[:,4]
v4 = data[:,5]

fit_coeff, stats = P.polyfit(angleServo, anglePlat, 3, full=True)

for i in range(len(anglePlat)):
    alpha = (180/pi)*atan((WIDTH/(2*HEIGHT))*(((v1[i]+v2[i])-(v3[i]+v4[i]))/
            max((v1[i]+v2[i]),(v3[i]+v4[i]))))


#print to check that the size of the lists are what they are intended to be.
#print(len(anglePlat))
#print(len(angleServo))
#print(len(v1))
#print(len(fit_coeff))
#print(stats)

plt.clf()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#bx = fig.add_subplot(222, projection='3d')


#choose which one to uncomment depending on what to display
cset = ax.scatter(anglePlat,angleServo, v1, cmap=cm.coolwarm)
#cset_fit = bx.
#ax.plot_surface(anglePlat,angleServo,v1, cmap=cm.coolwarm)
#cset = ax.scatter(anglePlat,angleServo, v2, cmap=cm.coolwarm)
#cset = ax.scatter(anglePlat,angleServo, v3, cmap=cm.coolwarm)
#cset = ax.scatter(anglePlat,angleServo, v4, cmap=cm.coolwarm)

ax.clabel(cset, fontsize=9, inline=1)
plt.show()



