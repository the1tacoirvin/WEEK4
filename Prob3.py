import numpy as np
from scipy import linalg
"""found from this link https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html"""
"""https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve.html#scipy.linalg.solve"""
# Define the matrix A1 and vector b1 for the first system
A1 = np.array([[3, 1, -1], [1, 4, 1], [2, 1, 2]])
b1 = np.array([2, 12, 10])

# Solve for x1, this function actually does the math to solve all the x values
x1 = linalg.solve(A1, b1)

# Print the solution for the first system
print("Solution for the first system:")
for i in range(len(x1)):
    #displays the values nicely for ya
    print(f"x{i+1} = {x1[i]}")

# Define the matrix A2 and vector b2 for the second system
A2 = np.array([[1, -10, 2, 4], [3, 1, 4, 12], [9, 2, 3, 4], [-1, 2, 7, 3]])
b2 = np.array([2, 13, 21, 37])

# Solve for x2, this function actually does the math to solve all the x values
x2 = linalg.solve(A2,b2)

# Print the solution for the second system
print("\nSolution for the second system:")
for i in range(len(x2)):
    # displays the values nicely for ya
    print(f"x{i+1} = {x2[i]}")
