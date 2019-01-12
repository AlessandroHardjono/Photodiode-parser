"""
@author: Alessandro Hardjono
Date: 12 Jan 2019
"""

import numpy as np
import matplotlib.pyplot as plt


fileName = "Data_raw.txt"


#the X (plat) and Y (servo) values
anglePlat = data[:,0]
angleServo = data[:,1]
aP, aS = np.meshgrid(anglePlat, angleServo)
alpha = np.zeros(len(anglePlat))
beta = np.zeros(len(angleServo))

#the Z values
v1 = data[:,2]
v2 = data[:,3]
v3 = data[:,4]
v4 = data[:,5]

volt1 = np.zeros(60,60)
volt2 = np.zeros(60,60)
volt3 = np.zeros(60,60)
volt4 = np.zeros(60,60)


for x in range(0,3600) :
    volt1[anglePlat[i]+31,angleServo[i]+31) = volt1[i]
    volt2[anglePlat[i]+31,angleServo[i]+31) = volt2[i]
    volt3[anglePlat[i]+31,angleServo[i]+31) = volt3[i]
    volt4[anglePlat[i]+31,angleServo[i]+31) = volt4[i]
    

#plotting
plt.clf()

plt.subplot(221)
plt.imshow(volt1, cmap = "heat")

plt.subplot(222)
plt.imshow(volt2, cmap = "heat")

plt.subplot(223)
plt.imshow(volt3, cmap = "heat")

plt.subplot(224)
plt.imshow(volt4, cmap = "heat")

plt.show()

