from scipy.optimize import linprog
import math

# Coefficients of the objective function (maximize profit)
c = [-168.33, -256.67]  # We negate to convert the maximization problem to minimization

# Coefficients of the inequality constraints
A = [
    [0.25, 0.333],    # Machine time constraint
    [0.333, 0.5]      # Craftsman time constraint
]

# Right-hand side of the inequality constraints
b = [40, 35]

# Bounds for each variable (non-negative and x >= 10)
x_bounds = (10, None)
y_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Print the result
if result.success:
    print(f"Optimal number of Product X: {math.ceil(result.x[0])}")
    print(f"Optimal number of Product Y: {math.ceil(result.x[1])}")
    print(f"Maximum profit: {-result.fun:.2f}")
else:
    print("No solution found.")
