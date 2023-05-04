import numpy as np
import matplotlib.pyplot as plt

T = list(np.arange(-3.0, 10.0, 2e-1))   #for temperatures between -3.0 and 10, with 0.2 precision.
V = list(np.arange(0.0, 2.0, 1e-4))     #for volumes between 0.0 and 2, with 0.0001 precision.

# according to the reduced form of the equation in Wikipedia
### https://en.wikipedia.org/wiki/Van_der_Waals_equation

a = 3.0   #constant
b = 1/3   #constant
R = 8.314 #j/mol

Vp = [] #for all the volume points in x axis
Pp = [] #for all the pressure points in y axis 

for t in T:
    for v in V:
        p = R * t / a / (v - b) - a / v ** 2
        Vp.append(v)
        Pp.append(p)
    
plt.plot(Vp, Pp, color="black")

# limit the frame
plt.xlim([0.3,2])
plt.ylim([-10.0,8.0])

plt.xlabel("V")
plt.ylabel("p")

plt.show()