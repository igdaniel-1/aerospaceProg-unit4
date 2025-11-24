# Unit 4 question 1 part 3
# Spacecraft Thruster Telemetry Visualization
# Objectives:
# Read in the spacecraft_thruster.csv file using csv and csv.reader
# Make an array titled thrust_values that contains only the thrust values of each row
# Plot the data of thrust_values on a line chart using matplotlib

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# data = []
thrust_values = []
date_values = []

with open('spacecraft_thruster.csv', mode='r') as f:
    data = csv.reader(f)

    for entry in data:
        if entry[2] == 'thrust':
            continue
        thrust_values.append(entry[2])


        #########
        #########
        #########
        # i want to access just the second count for the x axis of the graph
        date_obj = datetime.strptime(entry[0], '%Y-%m-%d %H:%M:%S.%f')
        date_values.append(date_obj[4])
        ##########
        #########
        #########



print("\ndates:", date_values[:10])

print("\nthrust:", thrust_values[:10])

# # plot the thrust values
# plt.plot(thrust_values[:10])
# plt.xlabel('Time')
# plt.ylabel('Thrust')
# plt.title('Aircraft Thrust')
# plt.grid(True)
# plt.show()