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
# only one file is in the folder ATM
# need to download and add the other TIFF files
np.seterr(divide='ignore', invalid='ignore')
bands = glob("./satellite-bands/*B?*.tiff")
bands.sort()

data = []
for band in bands:
    with rio.open(band, 'r') as file:
        data.append(file.read(1))
stack_data = np.stack(data)
ep.plot_bands(stack_data, cmap = 'gist_earth', figsize = (20, 12), cols = 6, cbar = False)
# plt.show()

# stack the rgb data
rgb = ep.plot_rgb(stack_data, 
                  rgb=(3,2,1), 
                  figsize=(10, 16))
plt.show()