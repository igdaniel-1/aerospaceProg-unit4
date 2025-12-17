# Unit 4 final project
# Rocket Equation Numerical Solver

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.integrate import solve_ivp 

# Define rocket parameters
# Effective exhaust velocity (m/s), AKA specifc impulse:
# ...a measure of how efficiently an engine generates thrust. 
# ...measured in units of velocity (m/s or ft/s), or time (s).
v_e = 3000    
m_initial = 100  # Initial total mass of the rocket (kg)
delta_m = 0.1  # Mass flow rate (kg/s)

# Define time range for integration
t_span = (0, 10)

# arguments: initial mass, final mass
def rocket_equation(t_span, v_e):   
    # m(t) = m_0 - delta_m*t
    m_f = m_initial - delta_m*t_span

    deltaVelocity = v_e * np.emath.log(m_initial/m_f)  
    return deltaVelocity


# t_eval = np.linspace(0, 10, 1000)
v_0 = 0
state0 = [v_0]
# FORMAT: solution = solve_ivp(functionName, time_span, state0, t_eval=np.linspace(0,100,1000))
solution = solve_ivp(rocket_equation, t_span, [0], dense_output=True)
# solution = solve_ivp(rocket_equation, t_span, state0, )
t_eval = np.linspace(0, 10, 1000)
velocity = solution.sol(t_eval)
# print('\nvelocity:',velocity)

# plotting
plt.figure(figsize=(10, 6))
# plots t_eval and velocity[0]
plt.plot(t_eval, velocity[0])

# labels
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.title('Rocket Equation')
plt.grid(True)
plt.axis('equal')
plt.show()
