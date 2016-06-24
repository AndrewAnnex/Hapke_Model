#!/bin/python
import numpy as np
import matplotlib.pyplot as plt

Spectra_data_file = 'CO2_4260_Spectra.txt'
Spectra_data_set = np.loadtxt(Spectra_data_file, usecols=(0,1), unpack=True)
Wavelength = Spectra_data_set[0,:]
If = Spectra_data_set[1,:]

plt.plot(Wavelength, If)
#plt.plotfile('CO2_4260_Spectra.txt', delimeter = '  ', cols=(0,1), names=('Wavelength', 'If'), marker='o')
plt.show()






