# unit 4 question 4 part 3
# Analyzing Satellite Images using earthpy

import numpy as np
from glob import glob
import rasterio as rio
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import matplotlib as plt

# Importing Band TIFF Data
np.seterr(divide='ignore', invalid='ignore')
bands = glob("./satellite-bands/*B?*.tiff")
bands.sort()

data = []
for band in bands:
    with rio.open(band, 'r') as file:
        data.append(file.read(1))
stack_data = np.stack(data)

# this is a visualizer of all the different bands
# ep.plot_bands(stack_data, cmap = 'gist_earth', figsize = (20, 12), cols = 6, cbar = False)
# plt.show()

# stack the rgb data
rgb = ep.plot_rgb(stack_data, 
                  rgb=(3,2,1), 
                  figsize=(10, 16))
plt.show()