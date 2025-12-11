# Unit 4 question 4 part 2
# Visualizing the Spectra of Ganymede

# Objectives:
# Import the FITS file for Ganymede (ganymede.fits) using fits from astropy.io
# Print out general info and header data about the FITS file
# Use the Spectrum1D function from specutils to interpret the data
# Plot the spectra using matplotlib

from astropy.io import fits
# import astropy
from astropy import units as u
from specutils import Spectrum1D
# from specutils import Spectrum
from astropy.visualization import quantity_support
import matplotlib.pyplot as plt
import numpy as np

file = fits.open('./ganymede.fits')
file.info()
print('\nheader:',file[0].header[0:5])