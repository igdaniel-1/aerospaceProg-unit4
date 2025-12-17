# Unit 4 question 3 part 1
# How the temperature u(x,t) of a one-dimensional rod 
# varies over time as heat diffuses through the material

# u(x,t) is the temperature at position x and time t
# α thermal diffusivity of the material
# du/dt rate of change of temperature with respect to time
# d^2u/dx^2 spatial curvature of the temperature profile

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

L = 1  # Length of the rod
alpha = 0.01  # Thermal diffusivity
T_initial = lambda x: np.sin(np.pi * x)  # Initial temperature distribution
T_left_boundary = 0  # Temperature at left boundary
T_right_boundary = 0  # Temperature at right boundary

def heat_equation_pde(t, T):
    dTdx2 = np.gradient(np.gradient(T))  # Second spatial derivative
    return alpha * dTdx2

x = np.linspace(0, L, 100)
T0 = T_initial(x)               # T0 is the temperature and Y-value
sol = solve_ivp(heat_equation_pde, [0, 1], T0, t_eval=np.linspace(0, 1, 100))

plt.figure(figsize=(10, 6))
for i in range(len(sol.t)):
    plt.plot(x, sol.y[:, i], label=f't = {sol.t[i]:.2f}')
plt.xlabel('Position (x)')
plt.ylabel('Temperature (T)')
plt.title('Temperature Distribution Over Time (1D Heat Equation)')
plt.grid(True)
plt.show()