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

fileName = 'Data_raw.txt'

x_unit = 'degrees(alpha)'
y_unit = 'degrees(beta)'
z_unit = 'voltage'

data = np.loadtxt(fileName, delimiter=",", comments="#")

#the X (plat) and Y (servo) values
anglePlat = data[:,0]
angleServo = data[:,1]
aP, aS = np.meshgrid(anglePlat, angleServo)
alpha = np.zeros(len(anglePlat))
beta = np.zeros(len(angleServo))
diff_alpha = np.zeros(len(anglePlat))

#the Z values
v1 = data[:,2]
v2 = data[:,3]
v3 = data[:,4]
v4 = data[:,5]

fit_coeff, stats = P.polyfit(angleServo, anglePlat, 3, full=True)

for i in range(len(anglePlat)):
    alpha[i] = (180/pi)*atan((WIDTH/(2*HEIGHT))*(((v1[i]+v2[i])-(v3[i]+v4[i]))/
            max((v1[i]+v2[i]),(v3[i]+v4[i]))))
    beta[i] =  (180/pi)*atan((WIDTH/(2*HEIGHT))*(((v1[i]+v4[i])-(v2[i]+v3[i]))/
            max((v1[i]+v4[i]),(v2[i]+v3[i]))))

for i in range(len(anglePlat)):
    diff_alpha[i] = alpha[i] - anglePlat[i]

#print to check that the size of the lists are what they are intended to be.
#print(len(anglePlat))
#print(len(angleServo))
#print(len(v1))
#print(len(fit_coeff))
#print(stats)

plt.clf()

fig = plt.figure()
ax1 = fig.add_subplot(221, projection='3d')
ax2 = fig.add_subplot(222, projection='3d')
ax3 = fig.add_subplot(223, projection='3d')
ax4 = fig.add_subplot(224, projection='3d')

ax1.set_title("Voltage1")
ax2.set_title("Voltage2")
ax3.set_title("Voltage3")
ax4.set_title("Voltage4")

ax1.set_xlabel("Platform Angle (degrees)")
ax1.set_ylabel("Servo Angle (degrees)")
ax2.set_xlabel("Platform Angle (degrees)")
ax2.set_ylabel("Servo Angle (degrees)")
ax3.set_xlabel("Platform Angle (degrees)")
ax3.set_ylabel("Servo Angle (degrees)")
ax4.set_xlabel("Platform Angle (degrees)")
ax4.set_ylabel("Servo Angle (degrees)")

# fig.xlabel("Platform angle (degrees)")
# fig.ylabel("Servo angle (degrees)")

#bx = fig.add_subplot(222, projection='3d')
#residual_fit = fig.add_subplot(111, projection='2d')


#choose which one to uncomment depending on what to display
#ax.plot_surface(anglePlat,angleServo,v1)
cset1 = ax1.scatter(anglePlat,angleServo, v1, cmap=cm.coolwarm)
cset2 = ax2.scatter(anglePlat,angleServo, v2, cmap=cm.coolwarm)
cset3 = ax3.scatter(anglePlat,angleServo, v3, cmap=cm.coolwarm)
cset4 = ax4.scatter(anglePlat,angleServo, v4, cmap=cm.coolwarm)

# ax1.clabel(cset1, fontsize=9, inline=1)


plt.tight_layout()
plt.show()

plt.plot(anglePlat, diff_alpha, color='r')
plt.show()



