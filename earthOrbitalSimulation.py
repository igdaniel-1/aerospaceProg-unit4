# Unit 4 question 5 part 2
# 2D Orbital Mechanics Simulation of Earth and a celestial body

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Create a function that takes in state_vectors, t, G, M and returns dxdt, dydt, dvxdt, dvydt
def orbit_equations_de(state_vectors, t, G, M):
    # this is the same function from 'orbitalMechanicsSimulation.py'
    # y[0] and y[1] represent the x and y positions respectively
    # y[2] and y[3] represent the x and y velocities respectively
    dxdt = state_vectors[2]
    dydt = state_vectors[3]
    dvxdt = -G * M * state_vectors[0] / (np.sqrt(state_vectors[0]**2 + state_vectors[1]**2))**3
    dvydt = -G * M * state_vectors[1] / (np.sqrt(state_vectors[0]**2 + state_vectors[1]**2))**3
    
    return [dxdt, dydt, dvxdt, dvydt]

# Define the initial value for altitude to be 400e3
altitude = 400e3
# Define the initial value for velocity to be 7800
velocity = 7800
# Define the gravitational constant to be 6.67430e-11
G = 6.67430e-11  # may have to store diff for sci notation
# Define the Mass of Earth to be 5.972e24
M = 5.972e24
# state_vectors
# Initial position at (1, 0) and velocity (0, 1)
state_vectors = [1.0, 0.0, 0.0, 1.0]  
# placeholder value for now: Define time points for integration
t = np.linspace(0, 10, 1000)


# Perform numerical integration using odeint
solution = odeint(orbit_equations_de, state_vectors, t, args=(G, M))

# Visualize the simulation using matplotlib
plt.figure(figsize=(5,5)) #random size to be changed later
# all values in x and y
plt.plot(solution[:,0], solution[:,1])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Orbit Simulation of Earth')
plt.grid(True)
plt.axis('equal')
plt.show()