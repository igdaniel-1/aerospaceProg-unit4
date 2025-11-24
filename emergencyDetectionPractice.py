# Unit 4 question 1 part 1

import json
import matplotlib.pyplot as plt

# this program reads from a database to see if any flights were recorded as having emergencies
# emergencies are then returned

with open('adsb_dataset.json', 'r') as f:
        data = json.load(f)['trace']


# We want all flight logs that contain valid JSON data. 
# The way we detect for this is by checking index 8 and seeing if there is a JSON object present.
filtered_data = []
emergencies = []
for aircraft in data:
    if aircraft[8] != None:
        filtered_data.append(aircraft)
        # print("\nTHIS ONE:",aircraft)
        emergency = aircraft[8].get('emergency')
        if (emergency!=None)and(emergency!='none'):
            emergencies.append([aircraft[0], emergency])

    # else:
    #     print("\nno json data aircraft:", aircraft)

# print(filtered_data[0])
# aircraft = filtered_data[0][8]
# print(f"Flight {aircraft['flight']} Airspeed is {aircraft['tas']} knots")
# print(aircraft)

print("\nemergencies:", emergencies)