# Unit 4 question 2 part 2
# Vertical Acceleration ODE

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def rocket_motion_ode(t, state):
    # Extract state variables
    x, v = state

    # Compute acceleration (assuming vertical motion)
    acceleration = (thrust - m*g) / m

    return [v, acceleration]

g = 9.81  # Acceleration due to gravity (m/s^2)
m = 1000  # Mass of the rocket (kg)
thrust = 20000  # Thrust of the rocket (N)
x0 = 0  # Initial position (m)
v0 = 0  # Initial velocity (m/s)
state0 = [x0, v0]  # initial state of position and velocity
time_span = (0, 100) # time in seconds

solution = solve_ivp(rocket_motion_ode, time_span, state0,t_eval=np.linspace(time_span[0], time_span[1], 1000))

plt.plot(solution.t, solution.y[0])
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Rocket Trajectory')
plt.grid(True)
plt.show()

