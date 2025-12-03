import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import sys

# BUG LOG: 
# 
# There's an issue trying to call the solve_ivp function of the theta values
### The error portion of the code I believe is:
# theta_0 = np.pi / 3
# theta_values = solve_ivp(thetaDoubleDot, [0,t], theta_0, t_eval=time_scale)
# solver = method(fun, t0, y0, tf, vectorized=vectorized, **options)
# 
### The error is as follows:
# raise ValueError("`y0` must be 1-dimensional.")
# 
# I don't know why it's reading theta_0 as a multi-dimensional object
# The type is float, the length is 1


# physical constants
g = 9.8
L = 2
mu = 0.1

# initial constraints
theta_0 = np.pi / 3  # 60 degrees
theta_dot0 = 0      # no initial angular velocity
delta_t = 0.01

# defining the DE
def thetaDoubleDot(theta, theta_dot):
    return -mu * theta_dot - (g/L) * np.sin(theta)

# solving the DE
def theta(t):
    theta = theta_0
    theta_dot  = theta_dot0
    

    # how theta changes with respect to time
    for time in np.arange(0,t,delta_t):
        theta_double_dot = thetaDoubleDot(theta, theta_dot)

        theta += theta_dot * delta_t
        theta_dot += theta_double_dot * delta_t
        # print("theta:", theta)
        # plotting
        # plt.plot(time, theta)
        # add double dot theta to graph 

    return theta

def valueAtTime(t):
    print("Theta at time", t, "seconds:",theta(t))


def plotter(t):
    time_scale = np.linspace(0,t,1)
    # time_scale = np.linspace(0,t,delta_t)
    print('theta_0:',theta_0)

    # value for theta over interval [0,t)
    theta_values = solve_ivp(thetaDoubleDot, [0,t], 3, t_eval=time_scale)

    plt.figure(figsize=(t,3))
    # theta definition

    for second in range(len(theta_values.t)):
        print("second:", second, "theta:", theta(second))
        plt.plot(time_scale, theta_values.y[:,second], label='Theta')
    plt.xlabel('Time')
    plt.ylabel('Theta')
    plt.title('Theta changes over time')
    plt.grid(True)
    plt.show()


# testing and execution
# number passed into plotter is experiment duration in seconds 
# plotter(10)
