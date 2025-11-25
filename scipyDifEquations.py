# Unit 4 question 2 part 1
# Differential Equations using SciPy

import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 

def differential_equation(y,t): 
    dydt = -y * t + 5
    return dydt

# initial condition 
y0 = 1
  
# values of time 
t = np.linspace(0,5) 
  
# Solving ODE 
y = odeint(differential_equation, y0, t) 

# plot DE
plt.plot(t,y) 
plt.xlabel("Time") 
plt.ylabel("Y") 
plt.title("Visualizing dy/dt ODE")
plt.show()