import numpy as np
import matplotlib.pyplot as plt

# physical constants
g = 9.8
L = 2
mu = 0.1

# initial constraints
theta_0 = np.pi / 3  # 60 degrees
theta_dot0 = 0      # no initial angular velocity

# defining the DE
def thetaDoubleDot(theta, theta_dot):
    return -mu * theta_dot - (g/L) * np.sin(theta)

# solving the DE
def theta(t):
    theta = theta_0
    theta_dot  = theta_dot0
    delta_t = 0.01

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

def main():
    t = 1
    print("Theta at time", t, "seconds:",theta(t))

# main()

def plotter(t):
    time_scale = np.linspace(0,t,1)
    plt.figure(figsize=(t,3))
    # theta definition

    for second in range(t):
        print("second:", second, "theta:", theta(second))
        plt.plot(second, theta(second), label='Theta')
    plt.xlabel('Time')
    plt.ylabel('Theta')
    plt.title('Theta changes over time')
    plt.grid(True)
    plt.show()

# number passed into plotter is experiment duration in seconds 
plotter(10)