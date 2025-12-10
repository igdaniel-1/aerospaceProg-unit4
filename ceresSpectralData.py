# Unit 4 question 4 part 1
# Ceres Spectra Analysis using SpecUtils

from astropy.io import fits
import astropy
from astropy import units as u
# from specutils import Spectrum1D
from specutils import Spectrum
from astropy.visualization import quantity_support
import matplotlib.pyplot as plt
import numpy as np

# NOTE from A.T.: we use quantity_support to numerically convert the values before plotting them using matplotlib
quantity_support() 

# tester
# flux = np.random.randn(200)*u.Jy
# wavelength = np.arange(5100, 5300)*u.AA
# spec1d = Spectrum(spectral_axis=wavelength, flux=flux)
# ax = plt.subplots()[1]
# ax.plot(spec1d.spectral_axis, spec1d.flux)
# ax.set_xlabel("Dispersion")
# ax.set_ylabel("Flux")
# plt.show()

# file = fits.open('./ceres.fits')
# file.info()
# print('\nsize:',file.size())
# header = file[0].header
# print('\n',header[0:5])
# # print(header[0:10])

# hdul = fits.open('./ceres.fits')
# fits_image_filename = fits.util.get_testdata_filepath('./ceres.fits')
with fits.open('./ceres.fits') as hdul:
    hdul.info()
    hdul.info()
    hdul.verify('fix')
    # data = np.array(hdul[0].data)
    data = hdul[0].data
    print('\ndata;',data)
# auto closes because of the 'with' convention

from specutils import Spectrum
# 
# ValueError: Spectral axis must be strictly increasing or decreasing.
wavelength = astropy.coordinates.SpectralQuantity(data, unit=u.AA)
print('\nwave:',wavelength)

flux = np.random.randn(313237)*u.Jy  #313237 is array size
# wavelength = data  #this needs to be converted to the quantity. spectralAxis data type
spec1d = Spectrum(spectral_axis=wavelength, flux=flux)
ax = plt.subplots()[1]
ax.plot(spec1d.spectral_axis, spec1d.flux)
ax.set_xlabel("Dispersion")
ax.set_ylabel("Flux")
plt.show()


# represent the spectra data provided by the FITS file
# ERROR
# HERE BELOW
# I think there's an issue reading from this file
# Something is coming up regarding the units?
# Maybe it's being read into the wrong format?
# ValueError: 'Relative Flux' did not parse as unit: At col 0, Relative is not a valid unit.  
# ....If this is meant to be a custom unit, define it with 'u.def_unit'. To have it recognized 
# ....inside a file reader or other code, enable it with 'u.add_enabled_units'. For details, 
# ....see https://docs.astropy.org/en/latest/units/combining_and_defining.html
# 
# spectra = Spectrum.read('./ceres.fits', 'fits')
# 
# ERROR HERE ABOVE

# MORE NOTES:
# to resolve the spectrum version issue and try to read the data from the fits file correctly
# https://specutils.readthedocs.io/en/stable/spectrum.html


# plot data

# fig, ax = plt.subplots()
# plt.title("1D Spectra Visualization of Ceres")
# FORMAT::: matplotlib.pyplot.step(x, y, *args, where='pre', data=None, **kwargs)
# ax.step(spectra.spectral_axis, spectra.flux)