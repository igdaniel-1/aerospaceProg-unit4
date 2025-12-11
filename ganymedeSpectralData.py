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
header = file[0].header
print('\nheader:',header[0:5])

print("\nnaxis:",header["NAXIS"])  # this is the data size
print("\nnaxis:",header["NAXIS1"])  # this is the data size of axis 1
print("\nCRVAL1:",header["CRVAL1"])
print("\nDATe:",header["DATE"])
print("\nBUNIT:",header["BUNIT"])  # what the hell is relative flux

# CRVAL1


# flux = np.random.randn(200) * u.Jy
# wavelength = np.arange(5100, 5300) * u.AA
# spectra = Spectrum1D(spectral_axis=wavelength, flux=flux)
# spectra = Spectrum1D.read(file)