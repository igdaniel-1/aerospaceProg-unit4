# Unit 4 question 4 part 1
# Ceres Spectra Analysis using SpecUtils

from astropy.io import fits
from specutils import Spectrum1D
from astropy.visualization import quantity_support
import matplotlib.pyplot as plt

file = fits.open('./ceres.fits')
# file.info()
# header = file[0].header
# print(header[:5])


# represent the spectra data provided by the FITS file
# ERROR
# HERE BELOW
# I think there's and issue reading from this file
# Something is coming up regarding the units?
# Maybe it's being read into the wrong format?
# ValueError: 'Relative Flux' did not parse as unit: At col 0, Relative is not a valid unit.  
# ....If this is meant to be a custom unit, define it with 'u.def_unit'. To have it recognized 
# ....inside a file reader or other code, enable it with 'u.add_enabled_units'. For details, 
# ....see https://docs.astropy.org/en/latest/units/combining_and_defining.html
spectra = Spectrum1D.read(file)
# ERROR HERE ABOVE


# plot data
# NOTE from A.T.: we use quantity_support to numerically convert the values before plotting them using matplotlib
# quantity_support() 
# fig, ax = plt.subplots()
# plt.title("1D Spectra Visualization of Ceres")
# FORMAT::: matplotlib.pyplot.step(x, y, *args, where='pre', data=None, **kwargs)
# ax.step(spectra.spectral_axis, spectra.flux)