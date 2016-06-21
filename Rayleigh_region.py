#!/bin/python
#Rayleigh_region.py

import numpy as np
import matplotlib.pyplot as plt

# phase angle, g = pi -theta, is the complement of the scattering angle, theta
g = np.linspace(0,180,num=100)


# Particle phase function eq.5.23 pg76 Hapke2012

def phase_function(phase_angle_g):
	return (3/4.)*(1+np.cos(g*(np.pi/180.))**2)

# Polarization of the scattered radiance eq.5.25 pg76 Hapke2012

def polarization_scattered_radiance(phase_angle_g):
	return (np.sin(g*(np.pi/180.))**2)/(1+np.cos(g*(np.pi/180.))**2)

# Plotting routine 

plt.subplot(2,1,1)
plt.plot(g, phase_function(g))
plt.ylabel('Phase(g)')

plt.subplot(2,1,2)
plt.plot(g, polarization_scattered_radiance(g))
plt.xlabel('g')
plt.ylabel('Polarization(g)')

plt.show()

