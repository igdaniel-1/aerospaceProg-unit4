# Unit 4 question 1 exercise 5
# Modeling Black Body Radiation
# Objectives:
# Import numpy, BlackBody from astropy.modeling.models, units from astropy, and quantity_support from astropy.visualization
# Create a BlackBody model with 3000K as the temperature and store it within the black_body variable
# Create a numpy range from 2000 to 200000 mm and store it within the wavelengths variable
# Obtain the flux by running black_body(wavelengths) and store it within flux


import numpy as np
from astropy.modeling.models import BlackBody
from astropy import units as u
from astropy.visualization import quantity_support
import matplotlib.pyplot as plt

black_body = BlackBody(temperature=3000*u.K)
wavelengths = np.arange(2000, 200000) * u.AA
flux = black_body(wavelengths)

with quantity_support():
    plt.figure()
    plt.semilogx(wavelengths, flux)
    plt.axvline(black_body.nu_max.to(u.AA, equivalencies=u.spectral()).value, ls='--')
    plt.show()