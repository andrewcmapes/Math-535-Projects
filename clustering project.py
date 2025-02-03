# File for exploring clustering algorithms
import numpy as np

def scatter_points(n: int=100, grid: list=[0,10], dim=2) -> list:
    """
    Scatter Points is a function that will generate a list of arrays that have random values.

    PARAMETERS:
        n. TYPE: int
            n is the number of arrays desired
        grid. TYPE: list
            grid is the list of boundaries for the random values the dimensions of the array take on
        dim. TYPE: int
            dim is the dimension of the arrays desired
    """
    points = []
    for i in range(n):
        points.append(np.random.randint(low=grid[0], high=grid[-1], size=(dim,1)))
    return points

x = scatter_points()

def kmeans(x: list, k: int, iterations: int = 10):
    dim, _ = x[0].shape
    first_reps = scatter_points(n=k, dim=dim)
    # Currently in progress
    pass

print(kmeans(x, 3), "\n", x[0])