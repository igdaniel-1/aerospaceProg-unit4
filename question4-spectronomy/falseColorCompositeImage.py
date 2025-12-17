# Unit 4 question 4 part 4
# Generate a False Color Composite

import numpy as np
from glob import glob
import rasterio as rio
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import matplotlib as plt

# Import the same Sentinel Satellite bands using glob and sort them
np.seterr(divide='ignore', invalid='ignore')
bands = glob("./satellite-bands/*B?*.tiff")
bands.sort()

# Process the data using rasterio and then place it using a numpy stack
data = []
for band in bands:
    with rio.open(band, 'r') as file:
        data.append(file.read(1))
stack_data = np.stack(data)

# not sure if needed 
# ep.plot_bands(stack_data, cmap = 'gist_earth', figsize = (20, 12), cols = 6, cbar = False)

# Plot the False Color Composite using earthpy
# EarthPy documentation:
# For color infrared (CIR) composite images, you will plot the near-infrared (NIR), red, and green bands, 
# which are bands 5, 4, 2, respectively. The Python index values will be ...
# the original band number minus 1, thus, 4, 3, and 2 for NIR, red, and green, respectively.
rgb = ep.plot_rgb(stack_data, 
                  rgb=(4,3,2), 
                  figsize=(10, 16))
plt.show()