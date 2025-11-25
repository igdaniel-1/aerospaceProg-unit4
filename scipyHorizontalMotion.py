# Unit 4 question 2 part 3
# Modeling Rocket Horizontal Motion ODE

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Constants
m = 1000  # Mass of the rocket (kg)
T = 20000  # Thrust of the rocket (N)


def horizMotionDE(time, state):
    velocity = state[0]
    # Assume constant drag force for simplicity
    D = 500*time  # Drag force as a function of time (N)
    acceleration = (T-D)/m
    return [acceleration]

# Objectives:
# Set the initial horizontal velocity to be 0
# Set the time span to be 0 - 100 s
# Plot the ODE solution using matplotlib

def calcHorizontalMotion():
    # x0 = 0
    v0 = 0
    state0 = [v0]
    time_span = (0,100)
    solution = solve_ivp(horizMotionDE, time_span, state0, t_eval=np.linspace(0,100,1000))

    # y = f(t)
    plt.plot(solution.t, solution.y[0])
    plt.xlabel("Time (s)")
    plt.ylabel("Horizontal Velocity (m/s)")
    plt.title("Rocket Horizontal Motion")
    plt.grid(True)
    plt.show()

calcHorizontalMotion()