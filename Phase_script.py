#!/bin/python
# PhaseFunction.py
# Replicating Figure 5.6a 5.6b in Hapke 2012 book
# The phase functions and polarizations of a nonabsorbing (n=1.50+i0) and 
# absorbing sphere (n=1.50+i0.25) of X=100

import numpy as np
import matplotlib.pyplot as plt

# phase angle, g = pi -theta, is the complement of the scattering angle, theta
g = np.linspace(0,180,num=100)

phase_function = (3/4.)*(1+np.cos(g*(np.pi/180.))**2)

polarization_scattered_radiance = (np.sin(g*(np.pi/180.))**2)/(1+np.cos(g*(np.pi/180.))**2)

plt.subplot(2,1,1)
plt.plot(g, phase_function)
plt.ylabel('Phase(g)')

plt.subplot(2,1,2)
plt.plot(g, polarization_scattered_radiance)
plt.xlabel('g')
plt.ylabel('Polarization(g)')

plt.show()