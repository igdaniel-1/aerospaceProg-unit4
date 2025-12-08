import numpy as np
from pde import CartesianGrid, solve_laplace_equation 

# create grid
cart_grid = CartesianGrid([[0, 2 * np.pi]] * 2, 64)
boundaries = [{"value": "sin(y)"}, {"value": "sin(x)"}]

result = solve_laplace_equation(cart_grid, boundaries)
result.plot()
# result.show()