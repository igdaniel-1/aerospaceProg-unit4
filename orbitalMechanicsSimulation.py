# Unit 4 question 5 part 1
# 2D Orbital Mechanics Simulation

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def orbit_equations_de(state_vectors, t, G, M):
    # y[0] and y[1] represent the x and y positions respectively
    # y[2] and y[3] represent the x and y velocities respectively
    dxdt = state_vectors[2]
    dydt = state_vectors[3]
    dvxdt = -G * M * state_vectors[0] / (np.sqrt(state_vectors[0]**2 + state_vectors[1]**2))**3
    dvydt = -G * M * state_vectors[1] / (np.sqrt(state_vectors[0]**2 + state_vectors[1]**2))**3
    return [dxdt, dydt, dvxdt, dvydt]

# Define initial conditions and constants
# [ POS_X, POS_Y, V_X, V_Y ]
y0 = [1.0, 0.0, 0.0, 1.0]  # Initial position at (1, 0) and velocity (0, 1)
G = 1.0  # Gravitational constant
M = 1.0  # Mass of the central body

# Define time points for integration
t = np.linspace(0, 10, 1000)

# Perform numerical integration
solution = odeint(orbit_equations_de, y0, t, args=(G, M))
# how is the below different from the above?
# it differs in its data structure
# the returned solution is a tuple, [data, column]
# solution = orbit_equations_de(y0, t, G, M)

# Plot the orbit trajectory
plt.figure(figsize=(8, 6))
# what does the [:,n] syntax below change?
# all values in range (for x, then for y)
plt.plot(solution[:, 0], solution[:, 1])
# print('solution:',solution[:,0][:5])
# print('solution:',solution[:,1][:5])

plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Orbit Simulation')
plt.grid(True)
plt.axis('equal')
plt.show()