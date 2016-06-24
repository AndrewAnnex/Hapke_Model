#Geometric_optics_region.py

import numpy as np
import matplotlib.pyplot as plt
from scipy import special
# phase angle, g = pi -theta, is the complement of the scattering angle, theta
g = np.linspace(0,180,num=1000)

# size parameter X = n*pi*a/lambda where a is the radius of spherical particle

#scattering_angle_theta = np.pi - g

# Phase function of geometric optic region uses bessel function of the first kind
# of order 1 with argument X*sin(theta)

#bessel_argument = X*np.sin(np.pi - g)

# def bessel_function_first_order(bessel_argument):
# 	bessel_function_angle_theta = special.j1(np.pi - g)
	#return bessel_function_angle_theta
def phase_function_geo(g):
	size_parameter_x = 100
	bessel_function_angle_theta = special.j1(np.pi - g*(np.pi/180.))
	diffractive_phase_function = size_parameter_x**2.*((2.*bessel_function_angle_theta)/(np.pi-g*(np.pi/180.)))**2.
	return diffractive_phase_function

#plt.subplot(2,1,1)
plt.plot(g, np.log10(phase_function_geo(g)))
plt.ylabel('Phase(g)')
plt.xlabel('g')

# plt.subplot(2,1,2)
# plt.plot(g, polarization_scattered_radiance)
# plt.xlabel('g')
# plt.ylabel('Polarization(g)')

plt.show()