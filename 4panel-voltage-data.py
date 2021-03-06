"""
@author: Alessandro Hardjono
Date: 12 Jan 2019
"""

import numpy as np
import matplotlib.pyplot as plt


fileName = "Sunsensor Data Large Hole.txt"
DATA_SIZE = 3600
data = np.loadtxt(fileName, delimiter=",", comments="#")

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

print(len(v1))

#setting up the plot
volt1 = np.zeros((60,60))
volt2 = np.zeros((60,60))
volt3 = np.zeros((60,60))
volt4 = np.zeros((60,60))

#plotting the data for each point
for i in range(0,DATA_SIZE) :
    volt1[int(anglePlat[i]+30),int(angleServo[i]+30)] = v1[i]
    volt2[int(anglePlat[i]+30),int(angleServo[i]+30)] = v2[i]
    volt3[int(anglePlat[i]+30),int(angleServo[i]+30)] = v3[i]
    volt4[int(anglePlat[i]+30),int(angleServo[i]+30)] = v4[i]
    

#plotting
plt.clf()

plt.subplot(221)
plt.imshow(volt4, cmap = "plasma")
plt.xlabel("Angle Platform (degrees)")
plt.ylabel("Angle Servo (degrees")

plt.subplot(222)
plt.imshow(volt1, cmap = "plasma")
plt.xlabel("Angle Platform (degrees)")
plt.ylabel("Angle Servo (degrees")

plt.subplot(223)
plt.imshow(volt3, cmap = "plasma")
plt.xlabel("Angle Platform (degrees)")
plt.ylabel("Angle Servo (degrees")

plt.subplot(224)
plt.imshow(volt2, cmap = "plasma")
plt.xlabel("Angle Platform (degrees)")
plt.ylabel("Angle Servo (degrees")

#plt.title("Voltage Heat Map")

plt.tight_layout()

plt.show()

