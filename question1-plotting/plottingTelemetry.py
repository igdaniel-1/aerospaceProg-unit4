# Unit 4 question 1 part 2
# plotting tas (True Air Speed)

import json
import matplotlib.pyplot as plt

with open('adsb_dataset.json', 'r') as f:
        data = json.load(f)['trace']


# We want all flight logs that contain valid JSON data. 
# The way we detect for this is by checking index 8 and seeing if there is a JSON object present.
filtered_data = []
for aircraft in data:
    if aircraft[8] != None:
        filtered_data.append(aircraft)

# print(filtered_data[0])

airspeeds = []
for entry in filtered_data:
    if 'tas' in entry[8]:
        airspeeds.append(entry[8]['tas'])
print(airspeeds[:5])

# plot airspeeds
plt.plot(airspeeds)
plt.xlabel('Data Point Index')
plt.ylabel('Airspeed (knots)')
plt.title('Aircraft Airspeed')
plt.grid(True)
plt.show()