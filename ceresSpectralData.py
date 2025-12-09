# Unit 4 question 4 part 1

from astropy.io import fits
from specutils import Spectrum1D
file = fits.open('./ceres.fits')
file.info()

header = file[0].header
print(header[:5])


# represent the spectra data provided by the FITS file